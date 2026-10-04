from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()

parser = StrOutputParser()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct", # can improve
    task="text-generation"
)  

prompt = PromptTemplate(
    template = "You are a helpful assistant. Assit the user based on query: {query}", # can improve
    input_variables = ["query"] 
)

model = ChatHuggingFace(llm=llm)

chain = prompt | model | parser

while True:
    print("YOUR PESRONAL AI ASSISTANT")
    ques = input("You:")

    if ques in ["exit", "quit", "bye"]:
        print("Exiting the chat...")
        break

    else:
        result = chain.invoke({"query": ques})
        print("Ai:",result)    
