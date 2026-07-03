import streamlit as st
from langgraph_workflow import app

st.set_page_config(
    page_title="Multi-Agent AI Chatbot",
    page_icon="🤖",
)

st.title("🤖 Multi-Agent AI Chatbot")
st.write("Ask questions from the Employee Handbook or ask general AI questions.")

question = st.text_input("Enter your question")

if st.button("Ask"):

    if question.strip():

        with st.spinner("Thinking..."):

            result = app.invoke({
                "question": question,
                "answer": ""
            })

        st.success("Answer")

        st.write(result["answer"])