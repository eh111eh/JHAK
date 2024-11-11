# TriLearn

Team: JHAK <br/>
Team members: [Jenson Joseph](https://github.com/JJsupercoder), Hwayeon Kang, [Amir Miresmaeili](https://github.com/amirfarjam), [Ke Wang](https://github.com/Vicky-0256)

What is the most effective way to learn and develop a deep understanding? What's the secret to unlocking our potential? The answer is, ***[The Feynman Technique](https://fs.blog/feynman-technique/)***.

Richard Feynman, a Nobel laureate in Physics, was not only a brilliant scientist but also a master at simplifying complex topics. His key insight: complexity and jargon often hide gaps in understanding.

Feynman’s learning technique consists of four steps:

1. Select a concept to learn.
2. Teach it to a child.
3. Review and refine your understanding.
4. Organize your notes and revisit them regularly.

Our educational chatbot is designed to apply ***the Feynman Technique***, helping users learn new concepts and test their understanding.

<img width="632" alt="Screenshot 2024-11-11 at 20 05 04" src="https://github.com/user-attachments/assets/4aa748ae-3791-42a8-8c77-176260eb97f5">

The system consists of three LLM-based agents: ***Teacher***, ***Student***, and ***Marker***.

- **Teacher**: This agent helps users learn new concepts by answering their questions. User questions are provided as voice input, which is converted to text in a pipeline. The Teacher, composed of an LLM, engages in a conversation with the user and, at the end, generates a summary of the interaction. This summary is then passed to the next agent, the Student.

- **Student**: Based on the summary provided by the Teacher, the Student agent assesses the user’s understanding by asking follow-up questions. From this conversation, the Student generates another summary note that reflects the user's level of comprehension.

- **Marker**: The Marker compares the two summaries—one from the Teacher and one from the Student—to evaluate the user’s understanding of the topic. If there are any gaps in understanding, the Marker provides feedback to help the user address them.

## Project Structure
```
├── whisper_speech_recognition.py   # ASR module
├── neuphonic_texttospeech.py       # TTS module
├── ollama_llm.py                   # LLM chat module
├── main.py                         # Main integration program
├── README.md                       # Documentation
└── requirements.txt                # Dependencies
```
