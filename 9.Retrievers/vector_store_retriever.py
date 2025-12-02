from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

embedding_model = OpenAIEmbeddings()

vectorStore = Chroma.from_documents(
    documents=documents,
    embedding=embedding_model,
    collection_name= "My_collection"
)

retriever = vectorStore.as_retriever(search_kwargs= {"k":2})
query = "What is chroma used for?"
result = retriever.invoke(query)
print("\n-----------Result 1-----------\n")
print(result[0].page_content)
print("\n-----------Result 2-----------\n")
print(result[0].page_content)