"""Send a request to the OpenAI API and print the response.

This script demonstrates how to call the OpenAI API using the requests library.
"""


import os
from dotenv import load_dotenv
import requests

load_dotenv()

user_input = input("Ask your question here : ")

api_key = os.getenv('API_KEY')

if not api_key:
    raise ValueError("API_KEY not found in environment variables")

API_URL = "https://api.openai.com/v1/responses"

KEY = f'Bearer {api_key}'

# print(KEY)

headers = {
    "Content-Type": "application/json",
    "Authorization": KEY
}

body = {
    "model": "gpt-4o-mini",
    "instructions": "You are a helpful assistant.",
    "input": user_input
}

response = requests.post(API_URL, headers=headers, json=body, timeout=10)

response_data = response.json()

text = response_data["output"][0]["content"][0]['text']
print(text)
