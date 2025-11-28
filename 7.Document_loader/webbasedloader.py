from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(web_path= "https://en.wikipedia.org/wiki/Space")

doc = loader.load()
print(doc)