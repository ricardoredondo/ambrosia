import os
import fnmatch
import openai

from dotenv import load_dotenv, find_dotenv
# from langchain_community.document_loaders import PyPDFLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from persister import Persister

class MainLoader:
    def __init__(self, files, source_folder, output_folder):
        self.files = files
        self.output_folder = output_folder
        self.source_folder = source_folder
        _ = load_dotenv(find_dotenv()) # read local .env file
        openai.api_key  = os.environ['OPENAI_API_KEY']

    def run(self):
        docs = self.load_documents()
        splits = self.split_file_content(docs)
        self.persist(splits)

    def persist(self, splits):
        Persister(splits, self.output_folder).run()

    def split_file_content(self, docs):
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 1500,
            chunk_overlap = 150
        )

        splits = text_splitter.split_documents(docs)
        return splits

    def load_documents(self):
        docs = []
        for mfile in self.files:
            if fnmatch.fnmatch(mfile.lower(), f"*.pdf"):
                docs.extend(self.loader_pdf(mfile)) 
                
            if fnmatch.fnmatch(mfile.lower(), f"*.txt"):
                # TODO: Load the TXT file
                print("  -> This is a TXT file")
        return docs

    def loader_pdf(self, file):
        print(f"-> PDFLoader: {self.full_path(file)}")
        loader = PyPDFLoader(self.full_path(file))
        return loader.load()
        
    def load_txt(self, file):
        print(f"TXTLoader: {self.full_path(file)}")
        print(f"TXTLoader Is not implemented yet")
        # TODO: Load the TXT document

    #  Build the Document's full path
    def full_path(self, file):
        return os.path.join(self.source_folder, file)
        
