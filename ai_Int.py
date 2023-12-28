from openai import OpenAI
from igpls import ai_key
import requests, json , os


client = OpenAI(
    api_key=ai_key
)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4",
)

print(chat_completion)