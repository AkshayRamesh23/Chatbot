from langchain.schema.messages import messages_to_dict
import json

def extract_messages_from_buffer_mem(messages): # input something like st.session_state.conversation
    """
    Returns a json string of the messages in the conversation
    INPUT is something like 'st.session_state.conversation'
    """
    extracted_messages = messages.memory.chat_memory.messages
    ingest_to_db = messages_to_dict(extracted_messages)
    return json.dumps(ingest_to_db)
    
            