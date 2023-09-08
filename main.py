import streamlit as st
import subprocess

# Define a function to run the Streamlit app
def run_streamlit_app():
    subprocess.run(["streamlit", "run", "app.py"])

# Create a Streamlit sidebar
st.sidebar.title("Streamlit Launcher")

# Add a button to launch the Streamlit app
if st.sidebar.button("Launch App"):
    st.sidebar.text("Launching Streamlit app...")
    run_streamlit_app()
