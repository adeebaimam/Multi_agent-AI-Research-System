from fastapi import FastAPI, HTTPException

from pipeline import run_research_agent
from model import ResearchRequest, ResearchResponse

app = FastAPI(
    title="ResearchMind API",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "ResearchMind API",
        "version": "1.0.0"
    }
    

@app.post("/research", response_model=ResearchResponse)
def research(request: ResearchRequest):

    try:
        result = run_research_agent(request.topic)

        return ResearchResponse(
            searched_results=result["searched_results"],
            scraped_content=result["scraped_content"],
            Report=result["Report"],
            Feedback=result["Feedback"]
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )