import gradio as gr


def respond(message, history):
    response = f"you said: {message}\
        \n And I say I love learning AI engineering"
    return response

gr.ChatInterface(fn=respond).launch()