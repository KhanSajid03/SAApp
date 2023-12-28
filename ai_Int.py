from openai import OpenAI
from igpls import ai_key
import requests, json , os


client = OpenAI(
    api_key=ai_key
)


reponse = client.chat.completions.create(
    model="gpt-3.5",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
)

print(reponse)