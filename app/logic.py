from app.models import Candidate, Role, MatchResult
from app.ml_model import model



def match_candidate_to_role(candidate: Candidate, role: Role) -> MatchResult:
    matched_skills = set(candidate.skills) & set(role.required_skills)

    skill_score = len(matched_skills) / len(role.required_skills)

    experience_score = 1.0 if candidate.years_experience >= role.min_experience else (
        candidate.years_experience / role.min_experience
    )

    final_score = round((skill_score * 0.7 + experience_score * 0.3), 2)

    explanation = (
        f"Matched {len(matched_skills)} out of {len(role.required_skills)} required skills. "
        f"Experience score considered."
    )

    return MatchResult(
        candidate_id=candidate.id or 0,
        role_id=role.id or 0,
        score=final_score,
        explanation=explanation
    )

