import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import warnings
warnings.filterwarnings("ignore")
import os 
os.environ["OPENAI_API_KEY"] = "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"
st.title("Ayansh Streamlit!")

background_image = "images/jnv.jpg"
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image:url('{background_image}');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
template = PromptTemplate(
    template="Answer this question{question}",
    input_variables=["question"]
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history= []
# question = st.text_input("Ask your question:")
question = st.chat_input("Please type your query here...")
# question = "Give some welcome message " if question==None else question
if question is not None and question !="exit":
    chain = template | ChatOpenAI(max_tokens=50)
    answer = chain.invoke(question)
    st.session_state.chat_history.append((question, answer.content))
else:
    st.write("Welcome...")

# Display all previous Q&A pairs
for i, (q, a) in enumerate(st.session_state.chat_history):
    st.write(f"Que : {q}")
    st.write(f"Ans : {a}")