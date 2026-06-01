from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage
chat_template = ChatPromptTemplate(
    [('system', "You are a helpful assistant for {domain}."),
     MessagesPlaceholder(variable_name="history"),
     ('human', "{refund}?")]
)
history = []
with open("chat_histroy.txt", "r") as f:
    history.extend(f.readlines())
prompt = chat_template.invoke(
    {"domain": "geography", "history": history, "refund": "my refund"})
print(prompt)
