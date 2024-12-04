# This is the interface with OPEN AI and ChatGPT
# This class holds the promtp and the calls to CHATGPT

import os
import openai

from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA


class Dexter:
    def __init__(self, llm_name, vectordb):
        openai.api_key  = os.environ['OPENAI_API_KEY']
        self.llm_name   = llm_name
        self.llm        = ChatOpenAI(model_name=self.llm_name, temperature=0)
        self.vectordb   = vectordb


    def ask(self, query):
        print("Asking.....")

        qa_chain = RetrievalQA.from_chain_type(
            self.llm,
            retriever=self.vectordb.as_retriever(),
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt()}
        )
        result = qa_chain({"query": query})
        return result["result"]


    def prompt(self):
        # template ="""Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always say "thanks for asking!" at the end of the answer. 
        # {context}
        # Question: {question}
        # Helpful Answer:"""


        template = """
        Asuma su nombre como Ambrosia, una aplicación de chatbot de salud enfocada en responder preguntas relacionas a dietas antinflamatorias.
        
        Comportese como un experto en nutrición y asuma que la presona que pregunta no tiene conocimientos previos en nutrición ni salud astro intestinal, por lo que las respuestas deben ser concisas y presentarse en un lenguaje sencillo de entender.
        
        Haga uso del siguiente contexto para responder a la pregunta. Si el contexto no es suficiente para responder a la pregunta, puede hacer uso de su conocimiento en nutrición para responder a la pregunta.
        
        Provea tanta información como sea posible, pero mantenga las respuestas fáciles de entender. Al tratarse de alimentos provea alternativas saludables que apliquen para una dieta saludable y que sea compatible con un plan antinflamatorio, apto para el tratamiento de candidiasis y SIBO.
        
        Contexto: {context}
        
        Pregunta: {question}
        
        Respuesta:"""
        return PromptTemplate.from_template(template)




    