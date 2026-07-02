from pydantic import BaseModel

class ResearchRequest(BaseModel):
    topic: str

class ResearchResponse(BaseModel):
    searched_results: str
    scraped_content: str
    Report: str
    Feedback: str