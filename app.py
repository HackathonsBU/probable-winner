from flask import Flask, request
from openai import OpenAI

client = OpenAI(api_key = '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')
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




