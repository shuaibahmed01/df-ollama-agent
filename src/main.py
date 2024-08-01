import pandas as pd
import streamlit  as st
from langchain.agents import AgentType
from langchain.experimental.agents import create_pandas_dataframe_agent
from langchain_ollama import ChatOllama

# streamlit web app configuration
st.set_page_config(
    page_title = "Dataframe Agent",
    page_icon = "💬",
    layout = "centered"
)



def read_data(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    else:
        return pd.read_excel(file)

# streamlit page title
st.title("🤖 AI Dataframe Agent")

# initialize chat history in streamlit session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []