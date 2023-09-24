from fastapi import FastAPI
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

#Declaring the chain
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
chain = LLMChain(llm=model, prompt=prompt)
#--------------------------

def reply(query: str):
    """query: str (user input)"""
    similars = search_similar(query)
    response = chain.run(contents=similars, query=query)
    return response


class Item(BaseModel):
    name: str

@app.get("/")
async def root():
    return {"message": f"""{reply("What are photonics?")}"""}

