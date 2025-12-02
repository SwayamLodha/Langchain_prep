import os
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings, ChatHuggingFace, HuggingFaceEndpoint
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

# ---------------------------
# ENVIRONMENT SETUP
# ---------------------------
os.environ["HF_TOKEN"] = "your HuggingFace Access Token"

# ---------------------------
# STEP 1a - YOUTUBE TRANSCRIPT FETCH
# ---------------------------
video_id = "Gfr50f6ZBvo"  # Only the ID

try:
    # If you don’t care which language, this returns the “best” one
    fetched_transcript = YouTubeTranscriptApi().fetch(video_id, languages=['en'])
    transcript_list = fetched_transcript.to_raw_data()
    # Flatten it to plain text
    transcript = " ".join(chunk["text"] for chunk in transcript_list)
    print(transcript)

except TranscriptsDisabled:
    print("No captions available for this video")

# ---------------------------
# STEP 1b - SPLITTING TEXT
# ---------------------------
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.split_text(transcript)
print(f"Total chunks created: {len(chunks)}")

# ---------------------------
# STEP 1c - EMBEDDING + VECTOR DB
# ---------------------------
print("Embedding and indexing...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.from_texts(chunks, embeddings)
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

# ---------------------------
# STEP 2 & 3 - CREATE LLM + PROMPT
# ---------------------------
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceTB/SmolLM3-3B",
    task="text-generation",
    huggingfacehub_api_token=os.environ["HF_TOKEN"],
)

model = ChatHuggingFace(llm=llm)

prompt = PromptTemplate(
    template=(
        "You are a helpful assistant.\n"
        "Answer ONLY from the provided transcript context.\n"
        "If insufficient context, say you don't know.\n\n"
        "{context}\n\n"
        "Question: {question}"
    ),
    input_variables=['context', 'question']
)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

parallel_chain = RunnableParallel({
    "context": retriever | RunnableLambda(format_docs),
    "question": RunnablePassthrough()
})

parser = StrOutputParser()
chain = parallel_chain | prompt | model | parser

# ---------------------------
# TEST QUERIES
# ---------------------------
print("\n🔹 Ask Questions About The Video")
while True:
    user_q = input("\nYour Question (or type 'exit'): ")
    if user_q.lower() == "exit":
        break

    answer = chain.invoke(user_q)
    print("\nAnswer →\n", answer)
