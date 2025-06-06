from fastapi import FastAPI
from pydantic import BaseModel
from analyzer import analyze_feedback

app = FastAPI()

class FeedbackRequest(BaseModel):
    feedback: str

@app.post("/analyze/")
def analyze(req: FeedbackRequest):
    result = analyze_feedback(req.feedback)
    return {"result": result}
