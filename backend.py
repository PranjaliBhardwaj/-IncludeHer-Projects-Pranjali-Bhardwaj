from flask import Flask, jsonify, request, render_template
from config import key
import openai

openai.api_key = key

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generateimages/<prompt>')
def generate(prompt):  # Add the prompt parameter here
    print("prompt:", prompt)  # Proper indentation
    response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=6,
    )
    print(response)  # Proper indentation
    return jsonify(response)

app.run(host='0.0.0.0', port=81)


