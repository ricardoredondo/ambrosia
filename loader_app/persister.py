import openai
import os
import time
import fnmatch

from dotenv import load_dotenv, find_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings



class Persister:

    def __init__(self, splits, output_folder):
        self.splits = splits
        self.output_folder = output_folder
        self.current_folder = os.path.join(self.output_folder, "current")
        self.embedding = OpenAIEmbeddings()

        # TODO:  Do I need this? I need a Python Guru here. 
        _ = load_dotenv(find_dotenv()) # read local .env file
        openai.api_key  = os.environ['OPENAI_API_KEY']


    def run(self):
        if not os.path.exists(self.current_folder):
            os.makedirs(self.current_folder, mode=0o777)
        else:
            self.backup()
        self.persist()


    def persist(self):
        print("Persist...")

        print(f"{self.current_folder}")
        vectordb = Chroma.from_documents(
            documents=self.splits,
            embedding=self.embedding,
            persist_directory=self.current_folder
        )
        print(vectordb._collection.count())
        vectordb.persist()
        print("Done")

    def backup(self):
        print("Backup...")
        current_time = int(time.time())
        bkup_path = f"{self.current_folder}_{current_time}"
        
        if os.path.exists(bkup_path): # Lets get rid of this cuz... reasons
            os.rmdir(bkup_path) 
        os.rename(self.current_folder, bkup_path)
        os.makedirs(self.current_folder, mode=0o777)