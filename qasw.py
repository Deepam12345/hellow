import streamlit as st

# Title
st.title("My First Streamlit App")

# Text
st.write("Welcome to Streamlit!")

# Header
st.header("User Details")

# Text Input
name = st.text_input("Enter your name")

# Number Input
age = st.number_input("Enter your age", min_value=1, max_value=100)

# Button
if st.button("Submit"):
    st.success(f"Hello {name}! You are {age} years old.")