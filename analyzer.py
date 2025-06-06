import openai

openai.api_key = "YOUR_API_KEY"  # Replace with your OpenAI key

def analyze_feedback(feedback_text):
    prompt = f"""
You are an AI assistant analyzing employee feedback.

Given each feedback line, identify:
1. Sentiment: Positive, Neutral, or Negative
2. Risk of Attrition: High, Medium, Low
3. Engagement Recommendation: 1–2 lines

--- Feedback ---
{feedback_text}
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response["choices"][0]["message"]["content"]
