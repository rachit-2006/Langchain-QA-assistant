import streamlit as st
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint,HuggingFacePipeline
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder,PromptTemplate
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

st.title("🧠 LangChain Q&A Assistant")

# if chat history is empty, then start a new list of chat history

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="you are a smart question answer bot ")
    ]




# Model name selection
model_name = st.selectbox("Choose Groq Model:", ["Groq-LLaMA2","Llama 4 Scout 17B 16E","Kimi K2 Instruct"])
    

# User input
user_input = st.text_input("Ask a question:")
st.write("Hey, How can I help you?")
if user_input:
    # === BACKEND LOGIC STARTS HERE ===
    #st.session_state.chat_history.append(AIMessage("Hey, How can I help you?"))
    
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    # 1. Load selected model
    # TODO: Write logic to load the selected model dynamically based on dropdown

    
    if(model_name=="Groq-LLaMA2"):
        model=ChatGroq(
            model="Llama-3.3-70b-Versatile",
        ) 
    elif(model_name=="Llama 4 Scout 17B 16E"):
        model=ChatGroq(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
        )
    elif(model_name=="Kimi K2 Instruct"):
        model=ChatGroq(
            model="moonshotai/kimi-k2-instruct",
    )     
    

    # 2. Create prompt using PromptTemplate or ChatPromptTemplate
    # TODO: Write logic to construct the appropriate prompt
# created a template that contains chat history using chat prompt template #

    
    chat_template=ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name='chat_history'),
        ('human','{query}')
    ])
    prompt=chat_template.invoke({'chat_history':st.session_state.chat_history,'query':user_input})

    # 3. Maintain previous chat history (optional: use MessagesPlaceholder equivalent)
    # TODO: Implement chat memory logic

    # st.session_state.chat_history is a list which stores our chat history #


    # 4. Parse the output
    # TODO: Use output parser to clean and display 
    


    # 5. Display the response
    # TODO: Show the final answer to the user
    response=model.invoke(prompt)
    st.session_state.chat_history.append(AIMessage(content=response.content))
    #st.write(response.content)
    for message in st.session_state.chat_history:
        st.write(message.content)
    #st.write(st.session_state.chat_history)


    
