import anthropic


def get_ai_feedback(user_answer: str, correct_answer: str, context: str) -> str:
    try:
        client = anthropic.Anthropic()
        r = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            messages=[{"role": "user", "content": f"""You are a Cambridge C1/C2 English examiner giving feedback to a Spanish-speaking student.

Context / exercise: {context}
Model answer: {correct_answer}
Student's answer: {user_answer}

Give concise feedback in 3–5 sentences:
1. Is the answer correct, partially correct, or incorrect?
2. If not fully correct, explain why and what the correct structure is.
3. A specific tip for this type of Cambridge exercise.
4. If partially correct, acknowledge what the student did well.

Be encouraging but precise. Write in English. No markdown, plain text only."""}],
        )
        return r.content[0].text
    except Exception as e:
        return f"AI feedback unavailable: {str(e)}"
