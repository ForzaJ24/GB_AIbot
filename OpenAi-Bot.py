import openai
import os
import json

prompt = input("Prompt: ")
openai.api_key = os.getenv("API_key")

response = openai.image.create(
    prompt=prompt,
    n=1,
    size='512x512'
)

with open('data.json','w') as file:
    json.dump(response,file,indent=4,ensure_ascii=False)
