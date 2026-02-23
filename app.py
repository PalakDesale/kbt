import streamlit as st

st.title("basic calculator app")
# Use integer inputs (step=1, format as integer) and cast to int to avoid floats
num1 = int(st.number_input("Enter first number", step=1, format="%d"))
num2 = int(st.number_input("Enter second number", step=1, format="%d"))
operation = st.selectbox("Select operation", ("+", "-", "*", "/"))

if st.button("Calculate"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            # Integer division to avoid float results
            result = num1 // num2
        else:
            result = "Error: Division by zero"
    st.write("Result:", result)