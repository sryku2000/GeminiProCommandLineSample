import textwrap
import google.generativeai as genai

from IPython.display import Markdown
# Used to securely store your API key

GOOGLE_API_KEY='Your_API_Key_Goes_Here'

genai.configure(api_key=GOOGLE_API_KEY)

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

def main():
    print("Welcome to the Gemini-Pro chat room!")
    print("Enter 'exit' to leave the chat room")
    while True:
        user_input = input("You: ")
        if user_input == "exit":
            break
        response = chat.send_message(user_input)
        print("Gemini-Pro: ", response.text)
if __name__ == "__main__":
    main()