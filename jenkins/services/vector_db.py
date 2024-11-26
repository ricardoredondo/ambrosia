import openai
import os

from dotenv import load_dotenv, find_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo


class VectorDB:
    def __init__(self, llm_name):
        # TODO. This constructor should be refactored to use the ENV variables
        # TODO: We should have just one instance of the VectorDB
        print("===>>>> VectorDB Constructor")
        openai.api_key  = os.environ['OPENAI_API_KEY']
        self.llm_name = 'gpt-3.5-turbo-instruct'                    # ONLY this Model works for SelfQueryRetriever
        # self.llm_name = 'gpt-4o'                                  # Note: Models are only for SelfQueryRetriever
                                                                    
        persist_directory = "/storage_data"                         # TODO. Change this to a ENV
        current_folder = os.path.join(persist_directory, "current") # TODO. Change this to a ENV
        
        # Initializing the ChromaDB instance 
        embedding = OpenAIEmbeddings()
        self.vectordb = Chroma(
            persist_directory=current_folder,
            embedding_function=embedding
        )
        print(f"Collection count: {self.vectordb._collection.count()}")

    def fetch(self, query):
        # NOTE: Here we can change the Search to be a different kind of retrival:
        # * SelfQueryRetriever
        # * SimilaritySearchRetriever

        # document_content_description = "Document content"
        # metadata_field_info = [
        #     AttributeInfo(
        #         name="source",
        #         description="The lecture the chunk is from, should be one of `docs/cs229_lectures/MachineLearning-Lecture01.pdf`, `docs/cs229_lectures/MachineLearning-Lecture02.pdf`, or `docs/cs229_lectures/MachineLearning-Lecture03.pdf`",
        #         type="string",
        #     ),
        #     AttributeInfo(
        #         name="page",
        #         description="The page from the lecture",
        #         type="integer",
        #     ),
        # ]

        # print(f"===============> {self.llm_name}")

        # llm = OpenAI(model=self.llm_name, temperature=0)
        # retriever = SelfQueryRetriever.from_llm(
        #     llm,
        #     self.vectordb,
        #     document_content_description,
        #     metadata_field_info,
        #     verbose=True
        # )

        # docs = retriever.get_relevant_documents(query)

        docs = self.vectordb.similarity_search(query, k=5)
        return docs