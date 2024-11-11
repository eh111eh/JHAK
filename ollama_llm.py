key = "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"

from openai import OpenAI

def language_model_chat(text, prompt):
    client = OpenAI(api_key=key)
    completion = client.chat.completions.create(model="gpt-4o", messages=[{"role": "system","content": prompt}, {"role": "user", "content": text}])
    return completion.choices[0].message.content

# print(openai_chat("what is the day today", "you are a chat bot"))


# import ollama


# def language_model_chat(user_input, PROMPT=None):
#     model = "llama3.1:latest"
#     stream = ollama.chat(
#         model=model,
#         messages=[
#             {"role": "system", "content": PROMPT},
#             {"role": "user", "content": user_input},
#         ],
#         stream=True,
#     )

#     output = ""
#     for chunk in stream:
#         output += chunk["message"]["content"]
#     return output


if __name__ == "__main__":
    INIT_PROMPT = """You are a helpful AI assistant named Neu. Your responses should be conversational, friendly, and natural-sounding, 
                as if you're chatting with a friend. Don't make your language formal, so use things like "I'm" instead of I am, 
                or "We'll" instead of "We will". Keep your responses very short and quick. Use no dashs in your replies.
                Youy will be given the full conversational history, but only output your answer, and nothing else.
                Keep responses less than 10 words. No emojis.
                """

    while True:
        user_input = input("User Input: ")
        print(user_input)
        llm_output = language_model_chat(user_input, INIT_PROMPT)
        print(llm_output)



