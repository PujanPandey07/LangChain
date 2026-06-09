from langchain_community.document_loaders import TextLoader
from lancgchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
parser = StrOutputParser()
prompt = PromptTemplate(
    template="Provide a summary of the following poem: {poem}", input_variables=["poem"])
model = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.9, )
loader = TextLoader("cricket.txt", encoding="utf8")
result=model.invoke("poem"=)
docs = loader.load()
print(docs)
