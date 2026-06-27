import os
import time

from dotenv import load_dotenv
from openai import OpenAI

from config.settings import MAX_RETRIES

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def chat(model, messages):

    last_exception = None

    for attempt in range(MAX_RETRIES):

        try:

            response = client.chat.completions.create(
                model=model,
                messages=messages
            )

            return response.choices[0].message.content

        except Exception as e:

            last_exception = e

            print(f"Retry {attempt + 1}/{MAX_RETRIES}")

            time.sleep(2)

    raise last_exception