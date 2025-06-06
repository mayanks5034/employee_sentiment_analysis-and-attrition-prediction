# Employee Sentiment Analysis & Attrition Prediction (AI-Powered)

🎯 An AI solution that analyzes employee feedback using LLMs to detect:
- 🔍 Sentiment (Positive / Negative / Neutral)
- 🚨 Attrition Risk (High / Medium / Low)
- 💡 Recommendations to boost engagement

📁 Built as part of the AI/ML Assessment  
👨‍💻 By: Mayank Singh

---

## 🧠 How It Works

- Uses OpenAI's GPT-3.5 or Gemini (Google AI Studio)
- Accepts feedback text input
- Returns sentiment, risk level, and HR suggestion
- Deployed via FastAPI on Render for real-time access

---

## 🚀 API Usage

### Endpoint:
`POST /analyze/`

### Request Body:
```json
{
  "feedback": "I feel disconnected from the team..."
}
### Response:
{
  "result": "Sentiment: Negative\nAttrition Risk: High\nRecommendation: Schedule a 1:1 meeting..."
}
