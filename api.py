"""
FastAPI Backend for Mobile App Integration
Exposes the LangGraph workflow as a REST API.

Run with:
    uvicorn api:app --reload
"""

import os
import traceback
from typing import List, Optional
from dotenv import load_dotenv

from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

from workflow import create_workflow
from state_schema import create_initial_state
from retriever import SUPPORTED_LEVELS

# --- CONFIGURATION ---
load_dotenv()
model = os.getenv("GEMINI_MODEL")
app = FastAPI(
    title="Çözüm AI Asistan API",
    description="Mobile app integration for Çözüm Koleji Veli Asistanı",
    version="1.0.0"
)

# CORS Configuration (Allow all for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific mobile app domains/schemes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global instances (reused across requests)
# Note: In a real production app with multiple workers, you might need external Redis for checkpointer
llm_instance = None
checkpointer_instance = None
workflow_app = None

def get_workflow():
    """Singleton pattern to initialize resources once."""
    global llm_instance, checkpointer_instance, workflow_app
    
    if workflow_app is None:
        # Disable LangSmith tracing to avoid 403 errors
        os.environ["LANGCHAIN_TRACING_V2"] = "false"
        
        google_api_key = os.getenv("GOOGLE_API_KEY")
        if not google_api_key:
            raise ValueError("GOOGLE_API_KEY needed in .env")
            
        # Using gemini-.5-flash as gemini-pro is deprecated
        model_name = model
        
        llm_instance = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=google_api_key,
            temperature=0.4,
        )
        
        # In-memory checkpointer (resets on server restart)
        # For persistence across restarts, use AsyncPostgresSaver or RedisSaver
        checkpointer_instance = InMemorySaver()
        
        workflow_app = create_workflow(llm_instance, checkpointer_instance)
        print("✅ Workflow initialized")
        
    return workflow_app, checkpointer_instance

# --- MODELS ---

class ChatRequest(BaseModel):
    query: str = Field(..., description="User's question")
    thread_id: str = Field(..., description="Unique session ID for the user/conversation")
    level: str = Field(..., description="Active education level "
    )

class ChatResponse(BaseModel):
    answer: str
    thread_id: str
    intent: Optional[str] = None
    level: str

# --- ENDPOINTS ---

@app.on_event("startup")
async def startup_event():
    get_workflow()

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "cozum-ai-api"}

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Process a chat message through the LangGraph workflow.
    """
    try:
        workflow, checkpointer = get_workflow()
        
        # Configuration for thread-based memory
        config = {"configurable": {"thread_id": request.thread_id}}
        
        # Get existing history
        try:
            snapshot = workflow.get_state(config)
            existing_messages = snapshot.values.get("messages", []) if snapshot else []
        except Exception:
            existing_messages = []
            
        # Prepare inputs
        messages = existing_messages + [HumanMessage(content=request.query)]
        active_level = request.level if request.level else 'anaokulu'
        
        initial_state = create_initial_state(
            user_query=request.query,
            active_level=active_level,
            messages=messages,
            compress_context=False # Default to full quality for API
        )
        
        # Execute workflow
        result = workflow.invoke(initial_state, config)
        
        final_answer = result.get("final_answer", "Üzgünüm, bir yanıt oluşturulamadı.")
        intent = result.get("intent")
        
        return ChatResponse(
            answer=final_answer,
            thread_id=request.thread_id,
            intent=intent,
            level=active_level
        )
        
    except Exception as e:
        print("Error processing request:")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
