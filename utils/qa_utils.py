from transformers import pipeline
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import HuggingFacePipeline
from langchain.chains.question_answering import load_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

def build_vectorstore(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(text)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_texts(chunks, embedding=embeddings)

def get_qa_chain():
    llm_pipeline = pipeline(
        "text-generation",
        model="gpt2",
        max_new_tokens=200,     # ✅ Fixes the long input error
        do_sample=True,
        temperature=0.7
    )
    llm = HuggingFacePipeline(pipeline=llm_pipeline)
    return load_qa_chain(llm, chain_type="stuff")

