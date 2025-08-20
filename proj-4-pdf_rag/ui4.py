import gradio as gr
from pdf_rag import get_response
import json
import os


with open(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "branding.json"))
) as f:
    branding = json.load(f)["brand"]

with gr.Blocks(theme="default", title=branding["organizationName"]) as demo:
    gr.HTML(
        f"""<div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <img src="{branding["logo"]["title"]}" alt="{branding["organizationName"]}" style="height: 100px;">
            </div>"""
    )
    gr.ChatInterface(
        fn=get_response,
        chatbot=gr.Chatbot(
            height=500,
            avatar_images=(None, branding["chatbot"]["avatar"]),
            type="messages",
        ),
        title=branding["organizationName"],
        description=branding["slogan"],
        type="messages",
        examples=[
            ["What is Here and Now AI"],
            ["Who are the founders"],
            ["what does the company do"],
            ["when was it founded"],
        ],
    )

if __name__ == "__main__":
    demo.launch()