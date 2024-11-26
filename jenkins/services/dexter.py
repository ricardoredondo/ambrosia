# This is the interface with OPEN AI and ChatGPT
# This class holds the promtp and the calls to CHATGPT

import os
import openai

from langchain.prompts import PromptTemplate

class Dexter:
    def __init__(self, llm_name):
        openai.api_key  = os.environ['OPENAI_API_KEY']
        self.llm_name = llm_name

    def ask(self, similar_vectors):
        print("")

    def prompt_question(self, vectors):
        template = """Comportese como un experto en nutrición y asuma que la persona que pregunta no tiene conocimientos previos en nutrición ni salud gastro-intestinal. Utilice el siguiente contexto para responder a la pregunta junto con cualquier información que usted conozca. Provea tanta información como sea posible, pero mantenga las respuestas tan concisas como sea posible. Al tratarse de alimentos provea alternativas saludables que apliquen para una dieta saludable.
        {context}
        Pregunta: {question}
        Respuesta:"""



    