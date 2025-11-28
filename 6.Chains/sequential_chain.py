from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI()
prompt1= PromptTemplate(
    template = "Generate a detailed report about {topic}.",
    input_variables = ["topic"]
    )

prompt2= PromptTemplate(
    template="Exactract 5 key points from the following report:\n{report}",
    input_variables = ["report"]
)

parser = StrOutputParser()
chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({"topic":"artificial intelligence"})
print(result)
chain.get_graph().print_ascii()