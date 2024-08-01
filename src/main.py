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

# initiate df in session state
if "df" not in st.session_state:
    st.session_state.df = None

# file upload widget
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "xls"])

if uploaded_file:
    st.session_state.df = read_data(uploaded_file)
    st.write("Dataframe Preview:")
    st.dataframe(st.session_state.df.head())


# display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# input field for users message
user_prompt = st.chat_input("Ask Dataframe Agent...")

if user_prompt:
    # add user message to chat history and display it
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})
    
    # loading the LLM
    llm = ChatOllama(model = "gemma:2b", temperature=0 )