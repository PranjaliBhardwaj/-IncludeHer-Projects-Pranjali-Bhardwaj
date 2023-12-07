import os
import openai
from config import key

from openai import OpenAI

client = OpenAI()
openai.api_key = key

response = openai.images.generate(
    model="dall-e-3",
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=6,
)

image_url = response.data[0].url
print(image_url)
