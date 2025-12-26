from fastapi import FastAPI
from app.models import Candidate, Role, MatchResult, Feedback
from app.logic import match_candidate_to_role
from app.feedback_store import feedback_db

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/match", response_model=MatchResult)
def match(candidate: Candidate, role: Role):
    return match_candidate_to_role(candidate, role)


@app.post("/feedback")
def submit_feedback(feedback: Feedback):
    feedback_db.append(feedback.dict())
    return {"message": "feedback saved"}
