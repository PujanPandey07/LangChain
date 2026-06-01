from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
# uing this method the values were not substituted in template so we change chat_prompt template
'''chat_template = ChatPromptTemplate([
    SystemMessage(content="You are a helpful assistant for {domain}."),
    HumanMessage(content="History about the capital of {country}?")
])'''
chat_template = ChatPromptTemplate([
    ('system', "You are a helpful assistant for {domain}."),
    ('human', "History about the capital of {country}?")
])

prompt = chat_template.invoke({"domain": "geography", "country": "France"})
print(prompt)
