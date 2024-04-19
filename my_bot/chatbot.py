import panel as pn
import ollama

pn.config.theme = "default"

ollama.pull("llama3")

def generate_response(contents: str, user: str, chat_interface: pn.chat.ChatInterface):
    chat_history = chat_interface.serialize(format="transformers",)
    response = ollama.chat(model='llama3', stream=True, messages=chat_history)
    message = ""
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        message += token
        yield message

chat_interface = pn.chat.ChatInterface(callback=generate_response)
chat_interface.send("Hi! How can i help you?", user="Assistant", avatar="🤖", respond=False)

chatbot = pn.Column(
    pn.pane.Markdown("# Llama3 🐪 Chatbot"),
    chat_interface,
    styles={"padding": "15px", 'border': '1px solid white',}
)

chatbot.servable()