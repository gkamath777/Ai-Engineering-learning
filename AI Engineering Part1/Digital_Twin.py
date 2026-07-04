# IMPORT LIBRARIES AND LOAD ENVIRONMENT VARIABLES

import gradio as gr
import os
import groq
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq()

if GROQ_API_KEY is None:
    raise Exception("API key is missing.")


# ADD AI FUNCTIONALITY

def respond_ai(message, history):
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

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

    messages.append({
        "role": "user",
        "content": message
    })

    client = Groq(api_key=GROQ_API_KEY)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    reply = response.choices[0].message.content
    return reply


gr.ChatInterface(fn=respond_ai).launch(inbrowser=True)
