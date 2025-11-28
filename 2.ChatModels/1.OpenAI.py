from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model = "gpt-4-turbo")  # OpenAI API key is required which is paid

result = model.invoke("What is the capital of India?")

print(result)