from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
response = model.invoke("What is the capital of France?")

print(response.content)
