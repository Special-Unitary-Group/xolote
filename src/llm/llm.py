import os
from pathlib import Path

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.schema import Document
from dotenv import load_dotenv
from switch import prompt_templates

load_dotenv()

all_pages: list[Document] = []

DIRPATH = os.path.abspath("..\\..\\data\\pdfs\\")

for filename in os.listdir(DIRPATH):
    filepath = os.path.join(DIRPATH, filename)

    # skip non-PDF files
    if not os.path.isfile(filepath) or not filepath.endswith(".pdf"):
        continue

    loader = PyPDFLoader(filepath)
    pages = loader.load_and_split(CharacterTextSplitter())

    all_pages.extend(pages)

embeddings = OpenAIEmbeddings()
vectors = FAISS.from_documents(all_pages, embeddings)

model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k")

prompt = PromptTemplate(
    input_variables=["contents"],
    template=prompt_templates("Ranking")
)

chain = LLMChain(llm=model, prompt=prompt)


def search_similar(query: str, k=3) -> list[str]:
    similars = vectors.similarity_search(query, k=k)

    return [s.page_content for s in similars]


def reply(query: str) -> str:
    similars = search_similar(query)

    return chain.run(contents=similars)
