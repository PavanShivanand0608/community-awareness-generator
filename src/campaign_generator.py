
import json
import os

from dotenv import load_dotenv
from openai import OpenAI, APIStatusError

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found in .env file")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

MODEL_NAME = "baidu/ernie-5.5-flash-preview:free"


def generate_campaign(problem: str, sdg_id: int) -> dict:

    if not isinstance(problem, str):
        raise ValueError("Problem must be text.")

    if not problem.strip():
        raise ValueError("Problem cannot be empty.")

    if len(problem.strip()) < 20:
        raise ValueError("Problem must contain at least 20 characters.")

    if not isinstance(sdg_id, int) or isinstance(sdg_id, bool) or sdg_id not in range(1, 18):
        raise ValueError("SDG ID must be between 1 and 17.")

    prompt = f"""
    You are an expert community awareness campaign creator.

    Community problem: {problem}
    Predicted Sustainable Development Goal: SDG {sdg_id}

    Generate a practical and engaging awareness campaign.

    Return ONLY a valid JSON object with these six fields:
    {{
        "campaign_title": "A short campaign title",
        "slogan": "A memorable awareness slogan",
        "campaign_description": "A short campaign description",
        "social_media_caption": "An engaging social media caption",
        "target_audience": ["Audience 1", "Audience 2"],
        "suggested_actions": ["Action 1", "Action 2", "Action 3"]
    }}

    Use simple, positive language suitable for the public.
    Make the campaign relevant to the given problem.
    Do not invent statistics or unsupported facts.
    """

    # Call OpenRouter and print detailed provider errors if they occur
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1000
        )

    except APIStatusError as error:
        print("OpenRouter status code:", error.status_code)
        print("OpenRouter detailed error:", error.response.text)
        raise

    generated_text = response.choices[0].message.content

    if not generated_text:
        raise ValueError("The AI model returned an empty response.")

    generated_text = generated_text.strip()

    if generated_text.startswith("```"):
        generated_text = generated_text.split("\n", 1)[1]
        generated_text = generated_text.rsplit("```", 1)[0].strip()

    try:
        campaign = json.loads(generated_text)
    except json.JSONDecodeError as error:
        raise ValueError(
            "The AI model did not return valid campaign JSON."
        ) from error

    required_fields = [
        "campaign_title",
        "slogan",
        "campaign_description",
        "social_media_caption",
        "target_audience",
        "suggested_actions"
    ]

    if not isinstance(campaign, dict):
        raise ValueError("The AI response must be a JSON object.")

    if not all(field in campaign for field in required_fields):
        raise ValueError("The AI response is missing required campaign fields.")

    if not isinstance(campaign["target_audience"], list):
        raise ValueError("Target audience must be a list.")

    if not isinstance(campaign["suggested_actions"], list):
        raise ValueError("Suggested actions must be a list.")

    return campaign
