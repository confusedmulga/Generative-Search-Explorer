import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.5,
    model_name="gpt-3.5-turbo"
)

prompt_template = PromptTemplate(
    input_variables=["context", "query"],
    template="""
You are a helpful AI assistant. Use the following context to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""
)

def generate_answer(context_docs, query):
    context = "\n\n".join(context_docs)
    prompt = prompt_template.format(context=context, query=query)
    response = llm.predict(prompt)
    return response
