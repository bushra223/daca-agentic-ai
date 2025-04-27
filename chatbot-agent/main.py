import os
from agents import Agent,Runner,OpenAIChatCompletionsModel,AsyncOpenAI
import chainlit as cl
from dotenv import load_dotenv,find_dotenv

#check to find the .env file 

_: bool= load_dotenv(find_dotenv())

GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")
if(GEMINI_API_KEY is None):
    raise ValueError("GEMINI_API_KEY not found in .env file. Please set it.")

#model
openai_client=AsyncOpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/openai/",api_key=GEMINI_API_KEY)



greeting_agent=Agent(
    name="greeting_agent",
    instructions="You are a helpful assistant. You will greet the user and ask them how you can help them.",
    model=OpenAIChatCompletionsModel(
            model="gemini-2.0-flash",openai_client=openai_client),
)
#agent loop

@cl.on_message




