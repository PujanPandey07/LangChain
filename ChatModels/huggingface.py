import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# Fixed: temperature and max_new_tokens are now passed directly
llm = HuggingFaceEndpoint(
    repo_id="de",
    task="text-generation",
    temperature=0.7,
    max_new_tokens=512
)

model = ChatHuggingFace(llm=llm)
response = model.invoke("What is the capital of France?")
print(response.content)
