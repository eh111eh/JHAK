key = ""

from openai import OpenAI

def openai_chat(text, prompt):
    client = OpenAI(api_key=key)
    completion = client.chat.completions.create(model="gpt-4o", messages=[{"role": "system","content": prompt}, {"role": "user", "content": text}])
    return completion.choices[0].message.content

print(openai_chat("what is the day today", "you are a chat bot"))