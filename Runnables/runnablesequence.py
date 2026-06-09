from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
prompt = PromptTemplate(
    template="You are a helpful assistant. Answer the following question: {question}", input_variables=["question"])
prompt2 = PromptTemplate(
    template="explain the joke: {joke}", input_variables=["joke"])
output_parser = StrOutputParser()
runnable = RunnableSequence(
    prompt, model, output_parser, prompt2, model, output_parser)
result = runnable.invoke({"question": "tell me a joke?"})
print(result)
