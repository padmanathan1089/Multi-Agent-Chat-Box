import streamlit as st
from langgraph_workflow import app as workflow_app

st.set_page_config(
    page_title="Multi-Agent AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Multi-Agent AI Chatbot")
st.caption("Ask questions from the Employee Handbook or ask general AI questions.")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input box (fixed at bottom, like ChatGPT)
question = st.chat_input("Ask your question...")

if question:
    # Show user message immediately
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = workflow_app.invoke({
                "question": question,
                "answer": ""
            })
            answer = result["answer"]
            st.markdown(answer)

    # Save AI response to history
    st.session_state.messages.append({"role": "assistant", "content": answer})

# Optional: clear chat button in sidebar
with st.sidebar:
    st.header("Options")
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()