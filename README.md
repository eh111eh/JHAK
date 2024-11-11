# JHAK

Our educational chatbot is designed to help users learn new concepts and test their understanding.

(schematic diagram of the model)

The system consists of three LLM-based agents: ***Teacher***, ***Student***, and ***Marker***.

- **Teacher**: This agent helps users learn new concepts by answering their questions. User questions are provided as voice input, which is converted to text in a pipeline. The Teacher, composed of an LLM, engages in a conversation with the user and, at the end, generates a summary of the interaction. This summary is then passed to the next agent, the Student.

- **Student**: Based on the summary provided by the Teacher, the Student agent assesses the user’s understanding by asking follow-up questions. From this conversation, the Student generates another summary note that reflects the user's level of comprehension.

- **Marker**: The Marker compares the two summaries—one from the Teacher and one from the Student—to evaluate the user’s understanding of the topic. If there are any gaps in understanding, the Marker provides feedback to help the user address them.

Maslow's Hierarchy of Needs
