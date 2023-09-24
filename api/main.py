from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import load_chain
from pydantic import BaseModel

openai_api_key="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"
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#Importing the data vectos
embeddings = OpenAIEmbeddings()
vectors = FAISS.load_local("vector_index", embeddings)
#--------------------------

#Decode Vectors
def search_similar(query: str):
    similars = vectors.similarity_search(query, k=3)
    
    return [s.page_content for s in similars]
#--------------------------

#Declaring the chain for /enviar/
model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
prompt = PromptTemplate(
    input_variables=["contents", "query"],
    template="""
        You are an expert academic researcher that enjoys helping other researchers, like myself.
        Based on the following content from research papers that I am familiar with and I know are related to my question:         
        {contents}
        {query}
        """
)
chain_enviar = LLMChain(llm=model, prompt=prompt)
#--------------------------

#Declaring the chain for /ranked/
model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
prompt = PromptTemplate(
    input_variables=["contents", "query"],
    template="""
        Based on the following contents:

            {contents}

            Give me a list of the provided papers ranked by relevance according to {query}."""
)
chain_ranked = LLMChain(llm=model, prompt=prompt)
#--------------------------


@app.post("/enviar/")
async def procesar_datos(input_data: str = Form(...)):
    similars = search_similar(input_data)
    response = chain_enviar.run(contents=similars, query=input_data)
    return {"response": response}


@app.post("/ranked/")
async def procesar_datos(input_data: str = Form(...)):
    similars = search_similar(input_data)
    response = chain_ranked.run(contents=similars, query=input_data)
    response.split("\n")
    return {"response": response}