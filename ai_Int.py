import openai as ai_int
from igpls import ai_key

ai_int.api_key = ai_key
existing_prompt = ""
model_engine = "text-davinci-003"

completion = ai_int.Completion.create(
    engine = model_engine, 
    prompt = existing_prompt,
    max_tokens=1024,
    n=1,
    stop = None,
    temperature=0.5, 
)

response = completion.choices[0].text
print(response)