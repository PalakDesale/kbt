import streamlit as st
st.title("simple chat bot")

Question = st.text_input("Ask a question")

if st.button("Ask"):
    st.write("You asked:", Question)
    st.write("Sorry, I am just a simple chat bot and cannot answer questions yet.") 