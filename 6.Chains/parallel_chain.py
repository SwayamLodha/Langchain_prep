from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatOpenAI()
model2 = ChatAnthropic(model_name='claude-3-7-sonnet-20250219')

prompt1= PromptTemplate(
    template = "Generate important notes about {topic}.",
    input_variables = ["topic"]
)
prompt2= PromptTemplate(
    template="Generate a quiz based on {topic}",
    input_variables = ["topic"]
)
prompt3= PromptTemplate(
    template="Merge the quiz: {quiz} with the notes: {notes} to create a comprehensive study guide.",
    input_variables = ["quiz","notes"]
)
parser = StrOutputParser()

parallelchain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallelchain | merge_chain

result = chain.invoke({'topic': 'Solar system'})
print(result)
chain.get_graph().print_ascii()