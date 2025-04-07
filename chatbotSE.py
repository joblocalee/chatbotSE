from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

client = OpenAI()

initial_message = [
    {
        "role": "system", 
        "content": "Your name is Sruthi. You are a faculty in Software Engineering.You are an expert in Software Engineering topics like SDLC, Software Lifecycle Models, Software Requirement Analysis, Software Designing etc. Deal with the users professionally. You are a helpful assistant. Always ask questions to the users to help them with their topic. Your response shouldn't exceed 250 words unless you are required to. Finally provide a summary of the topic for a quick revisal.",
    },
    {
        "role": "assistant", 
        "content": "Hi there!, I am Sruthi, your expert faculty in Software Engineering. How can I help you today?",
    }
]

def get_response_from_llm(messages):
    completion = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages
    )
    return completion.choices[0].message.content

if "messages" not in st.session_state:
    st.session_state.messages = initial_message

st.title("Software Engineering Bot")

for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

user_message = st.chat_input("Ask anything")
if user_message:
    new_message = {
        "role": "user", 
        "content": user_message,
    }
    st.session_state.messages.append(new_message)
    with st.chat_message(new_message["role"]):
        st.markdown(new_message["content"])

    response = get_response_from_llm(st.session_state.messages)
    if response:
        response_message = {
            "role": "assistant", 
            "content": response,
        }
        st.session_state.messages.append(response_message)
        with st.chat_message(response_message["role"]):
            st.markdown(response_message["content"])

