from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import pipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

# ✅ LOCAL PIPELINE MODE (no HF endpoint issues)
llm1_pipeline = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.2"
)

llm2_pipeline = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)

model1 = HuggingFacePipeline(pipeline=llm1_pipeline)
model2 = HuggingFacePipeline(pipeline=llm2_pipeline)

prompt1 = PromptTemplate.from_template(
    "Generate short notes about {topic}"
)

prompt2 = PromptTemplate.from_template(
    "Generate 5 questions about {topic}"
)

parser = StrOutputParser()

chain = RunnableParallel(
    notes=prompt1 | model1 | parser,
    questions=prompt2 | model2 | parser
)

result = chain.invoke({"topic": "Quantum Computing"})

print(result)
chain.get_graph().print_ascii()
