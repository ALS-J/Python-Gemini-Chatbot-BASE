#Input in your terminal 
#If windows: python -m pip install dotenv
#           python -m pip install -U google-genai

import os
from dotenv import find_dotenv, load_dotenv 
from google import genai

dvPath = find_dotenv()
load_dotenv(dvPath)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

Running = True

while Running == True:
    ChatModel = genai.Client()

    ChatMessage = input("How may I assist you?: ")

    Chat = ChatModel.interactions.create(
        model="", #Input any model https://ai.google.dev/gemini-api/docs/models 
        input=ChatMessage
    )

    print(f"Response:{Chat.output_text}")

    if(ChatMessage == "Quit"):
        Running = False