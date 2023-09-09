import streamlit as st
st.title("End-to-End Encryption")
user = st.text_input("Enter a Message")
st.write(swap_letters(user))
