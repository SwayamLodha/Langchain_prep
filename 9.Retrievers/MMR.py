from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

documents = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more.")
]

# Initialize OpenAI embeddings
embedding_model = OpenAIEmbeddings()

# Step 2: Create the FAISS vector store from documents
vectorstore = FAISS.from_documents(
    documents=documents,
    embedding=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type = "mmr",
    search_kwargs= {"k":2, "lambda_mult": 1} # k = top results, lambda_mult = relevance-diversity balance
    )

query = "What is Langchain?"
result = retriever.invoke(query)


print("\n-----------Result 1-----------\n")
print(result[0].page_content)
print("\n-----------Result 2-----------\n")
print(result[0].page_content)