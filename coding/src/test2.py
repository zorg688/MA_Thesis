from openai import OpenAI
import os


client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Translate this sentence to English: Hallo, dies ist nur ein Test."
        }
    ]
)

print(completion.choices[0].message)


