key = "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"

from openai import OpenAI

def openai_chat(text, prompt):
    client = OpenAI(api_key=key)
    completion = client.chat.completions.create(model="gpt-4o", messages=[{"role": "system","content": prompt}, {"role": "user", "content": text}])
    return completion.choices[0].message.content

print(openai_chat("what is the day today", "you are a chat bot"))