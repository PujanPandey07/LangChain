from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional, Literal

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# Schema for structured output


class ReviewSummary(BaseModel):
    key_themes: list[str] = Field(
        description="The key themes mentioned in the review")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["positive", "negative", "neutral"] = Field(
        description="The sentiment of the review (positive, negative, or neutral)", default="neutral")
    pros: Optional[list[str]] = Field(
        default=None, description="The positive aspects mentioned in the review")
    cons: Optional[list[str]] = Field(
        default=None, description="The negative aspects mentioned in the review")


structured_model = model.with_structured_output(ReviewSummary)


result = structured_model.invoke(
    "If you like discovering new flavors, this is the place. The selection of local beers at Mandala Cafe is impressive, especially the local tharra. Great sharing plates too, perfect for a casual night out.i pujan pandey have been impressed by thier warm welcomeness and kindness.they should improve their hygiene and the food delivery time was so large.")

print(result)
print(f"Summary: {result.summary}")
print(f"Sentiment: {result.sentiment}")
print(f"Key Themes: {result.key_themes}")
print(f"Pros: {result.pros}")
print(f"Cons: {result.cons}")
