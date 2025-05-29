"""Send a request to the OpenAI API and print the response.

This script demonstrates how to call the OpenAI API using the Python SDK.
"""
import os

from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()

key = os.getenv("API_KEY")

client = OpenAI(api_key=key)


history = []

while True:

    user_input = input("Ask your question here: ")

    if user_input == "":
        print("Exiting the program.")
        break

    history.append({"role": "user", "content": user_input})

    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="You are a helpful assistant.",
        input=history
    )

    text = response.output_text
    
    print(text)

    history.append({"role": "assistant", "content": text})
