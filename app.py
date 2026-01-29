import streamlit as st
st.title("Мнение за Pythom")
answer = st.radio("Харесваш ли Python?",("да", "не"))

if answer == "да":
 st.write("Супер! ")
else:
 st.write("Няма проблем, ще го харесаш!")
