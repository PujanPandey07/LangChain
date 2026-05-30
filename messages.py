from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
messages = [
    SystemMessage(
        "You are a helpful assistant that provides information about research papers."),
    HumanMessage("What is the capital of France?")

]
result = model.invoke(messages)
messages.append(AIMessage(result.content))
print(messages)
