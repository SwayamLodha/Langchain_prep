from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = 'college doc',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
    )

doc = loader.load()
print(doc[3].metadata)
print(doc[3].page_content)
