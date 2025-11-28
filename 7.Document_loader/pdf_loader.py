from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('7.Document_loader\Company Wide Code of Business Conduct and Ethics - July 2025_sign_download_preview.pdf')

doc = loader.load()
print(doc[0].page_content)