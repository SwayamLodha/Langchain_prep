from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=2, lang='en')

query = "Pollution in Delhi"

docs = retriever.invoke(query)
print("\n-----------Result 1-----------\n")
print(docs[0].page_content)
print("\n-----------Result 2-----------\n")
print(docs[0].page_content)