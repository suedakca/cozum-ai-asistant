"""
Retrieve Node
FAISS'ten eğitim bilgilerini çeker
"""

from state_schema import ChatState
from retriever import get_retrieved_documents, SUPPORTED_LEVELS


def retrieve_node(state: ChatState) -> ChatState:
    """
    Retrieve node - FAISS'ten dokümanları çeker.
    
    Args:
        state: Current conversation state
    
    Returns:
        Updated state with retrieved context
    """
    query = state["user_query"]
    active_level = state.get("active_level", "anaokulu")
    
    print(f"\n📚 [RETRIEVE NODE] FAISS'ten doküman getiriliyor...")
    print(f"   Query: '{query}'")
    print(f"   Level: {active_level}")
    
    # Retrieve documents from FAISS
    retrieved_docs = get_retrieved_documents(
        query,
        k=4,
        levels=[active_level],
        force_recreate=False,
        silent=True  # Production mode
    )
    
    # Format documents for LLM
    if not retrieved_docs:
        context = "Bilgi bulunamadı. Bu konuda dokümanlarımızda bilgi yok."
        print(f"   ⚠️  Hiç doküman bulunamadı!")
    else:
        context_parts = []
        for doc, score in retrieved_docs:
            level = doc.metadata.get('level', 'N/A').upper()
            title = doc.metadata.get('title', 'Başlıksız')
            content = doc.page_content
            
            context_parts.append(
                f"**[{level}] {title}**\n{content}"
            )
        
        context = "\n\n---\n\n".join(context_parts)
        print(f"   ✅ {len(retrieved_docs)} doküman bulundu")
    
    # Update state
    state["retrieved_context"] = context
    
    return state
