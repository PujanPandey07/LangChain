from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
chat_history = []
system_message = SystemMessage(
    "You are a helpful assistant that provides information about research papers.")
chat_history.append(system_message)
while True:

    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        human_message = HumanMessage(user_input)

        chat_history.append(human_message)
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(chat_history + [HumanMessage(user_input)])
    ai_message = AIMessage(response.content)
    chat_history.append(ai_message)
    print(f"Gemini: {response.content}")

print(f"{chat_history:}")
