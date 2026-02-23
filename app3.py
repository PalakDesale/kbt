import streamlit as st

st.markdown("""
<style>
            .stButton>button {
                background-color: green;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }   
</style>
            
""", unsafe_allow_html=True)


import streamlit as st

st.title("welcome to basic streamlit app")

age=st.slider("What is your age?", 0, 100, 25)
city=st.selectbox("Select your city", ["nashik", "pune", "mumbai", "nagpur","aurangabad"])

if st.button("Submit"):
    st.write(f"Your age is: {age}")