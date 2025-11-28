from langchain_community.document_loaders import TextLoader

loader = TextLoader('7.Document_loader/text_loader_demo.txt', encoding='utf-8')
result = loader.load()
print(result[0])