from app.models import Candidate, Role
from app.logic import match_candidate_to_role


candidate = Candidate(
    id=1,
    name="John Doe",
    email="john@example.com",
    skills=["python", "fastapi", "sql"],
    years_experience=3
)

role = Role(
    id=1,
    title="Backend Developer",
    required_skills=["python", "sql", "docker"],
    preferred_skills=["fastapi"],
    min_experience=2
)

result = match_candidate_to_role(candidate, role)

print("Score:", result.score)
print("Explanation:", result.explanation)
