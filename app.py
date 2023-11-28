from flask import Flask, request
from openai import OpenAI
import os

# Load OpenAI API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise ValueError("OpenAI API key not found in environment variables.")

client = OpenAI(api_key=openai_api_key)
app = Flask(__name__)

@app.route("/symptom_predict/<word>")
def matching_symptoms(word):
    # Use GPT-3 turn-based chat to find matching symptoms

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert in plant disease diagnosis."},
            {"role": "user", "content": word},
        ],
        max_tokens=50,
    )

    gpt3_response = completion.choices[0].message.content
    print(completion.choices[0].message.content)

    # Convert ChatCompletionMessage to dictionary

    return {"symptom": gpt3_response}

if __name__ == "__main__":
    app.run(debug=True)
