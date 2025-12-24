from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())
GROQ_API_KEY = os.environ["GROQ_API_KEY"]

from langchain.chat_models import init_chat_model

model = init_chat_model(model="openai/gpt-oss-20b", model_provider="groq")

resp=model.invoke('hello how are you!')
print(resp.content)


model = ChatGroq(model_name="openai/gpt-oss-20b")
resp=model.stream('write short essay on India')

# streaming the model output
for chunk in resp:
    print(chunk.content, end='', flush=True)
