from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from typing import TypedDict, Annotated

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# Schema for structured output


class ReviewSummary(TypedDict):
    key_themes: Annotated[list[str], "The key themes mentioned in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str,
                         "The sentiment of the review (positive, negative, or neutral)"]


structured_model = model.with_structured_output(ReviewSummary)


result = structured_model.invoke(
    "If you like discovering new flavors, this is the place. The selection of local beers at Mandala Cafe is impressive, especially the local tharra. Great sharing plates too, perfect for a casual night out.")

print(result)
print(f"Summary: {result['summary']}")
print(f"Sentiment: {result['sentiment']}")
print(f"Key Themes: {result['key_themes']}")
