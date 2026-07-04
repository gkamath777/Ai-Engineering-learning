# Import Libraries and the api_key
import os
from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY")
# )

# chat_completion = client.chat.completions.create(
#     model="llama-3.1-8b-instant",
#     messages=[
#         {"role": "user", "content": "Hello, Groq!"}
#     ]
# )

# print(chat_completion.choices[0].message.content)

# def respond_ai(message, history):
#     messages = [{"role": "system", "content": "You are a helpful assistant."}] + history + [{"role": "user", "content": message}]
#     #client = Groq(api_key=GROQ_API_KEY)
#     client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#     response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         messages=messages
#     )

#     reply = response.choices[0].message.content
#     return reply





def respond_ai(message, history):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    # Clean Gradio history before sending it to Groq with the simple format
    for item in history:
        if isinstance(item, dict):
            role = item.get("role")
            content = item.get("content")

            if role in ["user", "assistant"] and content:
                messages.append({
                    "role": role,
                    "content": content
                })

    # Add the latest user message
    messages.append({
        "role": "user",
        "content": message
    })

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    reply = response.choices[0].message.content
    return reply


gr.ChatInterface(fn=respond_ai).launch()

