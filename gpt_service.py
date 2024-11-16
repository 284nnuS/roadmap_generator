from openai import AzureOpenAI, OpenAI
from settings import *

class GPTSerivce:

    def __init__(self):
        self.client = AzureOpenAI(
                azure_endpoint = AZURE_OPENAI_ENDPOINT, 
                api_key= AZURE_OPENAI_KEY,  
                api_version= AZURE_API_VERSION
            )

    def generate_text(self, system_prompt, user_prompt):
        response = self.client.chat.completions.create(
            model = CHAT_COMPLETIONS_MODEL,
            messages = [
                {"role":"system", "content": system_prompt},
                {"role":"user","content": user_prompt}
            ],
            temperature=0,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return response.choices[0].message.content