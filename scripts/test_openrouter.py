
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError("OpenRouter API key not found in .env file")

# Connect to OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

# Send a simple test prompt
response = client.chat.completions.create(
    model="google/gemma-4-26b-a4b-it:free",
    messages=[
        {
            "role": "user",
            "content": "Write a short awareness slogan about quality education."
        }
    ],
    max_tokens=100
)

print("OpenRouter connection successful!")
print("\nGenerated response:")
print(response.choices[0].message.content)
