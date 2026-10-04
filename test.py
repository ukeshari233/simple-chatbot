from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI()

model_response = model.invoke("what is llm ")

print(model_response.content)