from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
prompt1 = PromptTemplate(
    template="Give a detailed explanation of {topic}",
    input_variables=["topic"]
)
prompt2 = PromptTemplate(template="Summarize the following explanation in 5 sentences: {explanation}",
                         input_variables=["explanation"])
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
parser = StrOutputParser()
chain = prompt1 | model | parser | prompt2 | model | parser
result = chain.invoke({"topic": "quantum computing"})
print(result)
chain.get_graph().print_ascii()
