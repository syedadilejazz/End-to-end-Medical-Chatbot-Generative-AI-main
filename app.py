from flask import Flask, render_template, jsonify,request
from src.helper import download_embedding_model
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAI
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY=os.environ.get("PINECONE_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

embedding_model = download_embedding_model()
index_name="medicalbot"
docsearch = PineconeVectorStore.from_existing_index(
                                                embedding=embedding_model, 
                                                index_name=index_name
                                                ) 
retriever=docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})
llm=OpenAI(temperature=0.4, max_tokens=500)

prompt=ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "{input}")
    
])


question_answer_chain=create_stuff_documents_chain(llm,prompt)
rag_chain=create_retrieval_chain(retriever, question_answer_chain)


@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/get",methods=["GET","POST"])
def chat():
    msg=request.form["msg"]
    input=msg
    print(input)
    response=rag_chain.invoke({"input": input})
    print("Response : ",response["answer"])
    return str(response["answer"])

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)

    




