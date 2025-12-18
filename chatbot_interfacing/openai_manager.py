import os
from dotenv import load_dotenv
from openai import OpenAI


# Fetch OpenAI API Key
def setup():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")
        return

    client = OpenAI(api_key=api_key)
    return client


# Handle prompting and response gathering
def prompt_openai(client: OpenAI, model: str, prompt: str) -> str:
    gpt_response = client.responses.create(
        model=model,
        input=prompt
    )
    return gpt_response.output_text

