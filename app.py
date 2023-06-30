from flask import Flask, request
import requests as req
import os

app = Flask(__name__)

# Path to the API key file
api_key_file = r"C:\Users\woutv\Documents\lablab_AI\Contextual_App\API_KEY.txt"

# Check if the file exists
if os.path.exists(api_key_file):
    # Read the API key from the file
    with open(api_key_file, "r") as file:
        API_KEY = file.read().strip()
else:
    # Raise an error if the file is not found
    raise FileNotFoundError("API key file not found")

@app.route("/")
def get_answer():
    context = request.args.get('context')
    question = request.args.get('question')

    url = "https://api.ai21.com/studio/v1/experimental/answer"

    payload = {
        "context": context,
        "question": question
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f'Bearer {API_KEY}'
    }

    response = req.post(url, json=payload, headers=headers)
    return response.text

if __name__ == "__main__":
    app.run()
