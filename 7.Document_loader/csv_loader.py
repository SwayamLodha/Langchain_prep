from langchain_community.document_loaders import CSVLoader

loader = CSVLoader('7.Document_loader/test.csv')
doc = loader.load()
print(doc[21])