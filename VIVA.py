import streamlit as st
st.title("interactive syreamlit app")
name=st.text_input("enter your name:")
if st.buttokn("submit"):
  st.write(f"hello,{name} : welcome to streamlit.")
