from pydantic import BaseModel
from typing import List, Optional


class Candidate(BaseModel):
    id: Optional[int] = None
    name: str
    email: Optional[str] = None
    skills: List[str]
    years_experience: float
    resume_text: Optional[str] = None


class Role(BaseModel):
    id: Optional[int] = None
    title: str
    required_skills: List[str]
    preferred_skills: Optional[List[str]] = None
    min_experience: float


class MatchResult(BaseModel):
    candidate_id: int
    role_id: int
    score: float
    explanation: str

class Feedback(BaseModel):
    candidate_id: int
    role_id: int
    approved: bool
    comment: Optional[str] = None
