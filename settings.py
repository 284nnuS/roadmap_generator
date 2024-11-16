import os
from dotenv import load_dotenv

load_dotenv("./config/.env")

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")
CHAT_COMPLETIONS_MODEL = os.getenv('CHAT_COMPLETION_NAME')
OPENAI_API_KEY  = os.getenv("OPENAI_API_KEY")

print(AZURE_OPENAI_ENDPOINT)
print(AZURE_OPENAI_KEY)
print(AZURE_API_VERSION)
print(CHAT_COMPLETIONS_MODEL)