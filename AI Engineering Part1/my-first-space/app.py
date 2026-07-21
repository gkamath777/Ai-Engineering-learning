import os
import gradio as gr


def respond(message, history):
    response = (
        f"You said: {message}\n"
        "And I say: I love learning AI engineering!"
    )
    return response


demo = gr.ChatInterface(fn=respond)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )