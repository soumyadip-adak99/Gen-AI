import streamlit as st
import pandas as pd

st.write("Hello world")

st.title("First app")
st.write("This is my first app")
st.header("Welcome to streamlit")
st.subheader("This is a sub header")
st.text("This is a text")

# button, Chekcboxes and sliders

if st.button("Click me"):
    st.write("Buttom was clicked")

agree = st.checkbox("I agree")
if agree:
    st.write("You agreed")


level = st.slider("Select a level: ", 1, 20, 5)
st.write(level)

uploaded_file = st.file_uploader("Upload a File", type=["csv", "txt"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())