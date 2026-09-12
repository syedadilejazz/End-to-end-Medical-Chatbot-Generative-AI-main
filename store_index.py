from src.helper import load_pdf_file,text_spliter,download_embedding_model
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import os
from dotenv import load_dotenv

load_dotenv()
PINECONE_API_KEY=os.environ.get("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

extracted_data = load_pdf_file("data")
text_chunks = text_spliter(extracted_data)
embedding_model = download_embedding_model()

pc=Pinecone(api_key=PINECONE_API_KEY)
index_name="medicalbot"

pc.create_index(name=index_name, dimension=384, metric="cosine",
                 spec=ServerlessSpec(cloud="aws",region="us-east-1"))

#First time run this lines to store data into Pinecone Vector Store
#Run again when data added or changes
docsearch = PineconeVectorStore.from_documents(documents=text_chunks,
                                                embedding=embedding_model, 
                                                index_name=index_name
                                                )


