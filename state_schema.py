"""
State Schema - LangGraph State Tanımı
Tüm workflow boyunca kullanılan state yapısı
"""

from typing import TypedDict, List, Optional, Annotated
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages


class ChatState(TypedDict):
    """
    LangGraph workflow state.
    
    LangGraph multi-node mimarisinde tüm node'lar arasında paylaşılan state.
    Her node bu state'i okuyabilir ve güncelleyebilir.
    """
    # Conversation messages (LangGraph manages this with add_messages)
    messages: Annotated[List[BaseMessage], add_messages]
    
    # User query
    user_query: str
    
    # Intent detection result
    intent: Optional[str]  # "greeting", "education", "event", "price", "unknown"
    intent_confidence: Optional[float]
    intent_reasoning: Optional[str]
    
    # Active education level
    active_level: str  # "anaokulu", "ilkokul", "ortaokul", "lise" (default: "anaokulu")
    
    # Context compression control
    compress_context: bool  # True = compress retrieved context, False = use full context
    
    # Retrieved context from FAISS/tools
    retrieved_context: Optional[str]
    
    # Final answer
    final_answer: Optional[str]
    
    # Error handling
    error: Optional[str]


def create_initial_state(
    user_query: str,
    active_level: str = "anaokulu",
    messages: List[BaseMessage] = None,
    compress_context: bool = False  # Default: compress OFF (full context for quality)
) -> ChatState:
    """
    Yeni conversation için initial state oluşturur.
    
    Args:
        user_query: Kullanıcının sorusu
        active_level: Seçili eğitim kademesi (varsayılan: "anaokulu")
        messages: Conversation history (LangChain messages)
        compress_context: Context compression açık mı? (True = compress, False = full)
    
    Returns:
        ChatState: Initial state
    """
    if messages is None:
        messages = []
        
    return ChatState(
        messages=messages,
        user_query=user_query,
        intent=None,
        intent_confidence=None,
        intent_reasoning=None,
        active_level=active_level,
        compress_context=compress_context,
        retrieved_context=None,
        final_answer=None,
        error=None
    )
