import openai
import os

from dotenv import load_dotenv, find_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

class VectorDB:
    def __init__(self):
        print("===>>>> VectorDB Constructor")
        openai.api_key  = os.environ['OPENAI_API_KEY']

        # TODO. Change this to a ENV
        persist_directory = "/storage_data"
        current_folder = os.path.join(persist_directory, "current")
        
        embedding = OpenAIEmbeddings()
        self.vectordb = Chroma(
            persist_directory=current_folder,
            embedding_function=embedding
        )
        print(f"Collection count: {self.vectordb._collection.count()}")

    def fetch(self, query):
        vectors = self.vectordb.similarity_search(query, k=5)
        return vectors