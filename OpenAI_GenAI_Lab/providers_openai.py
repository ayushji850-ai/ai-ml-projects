import os
from openai import OpenAI

class OpenAIProvider:
    def __init__(self):
        key=os.getenv("OPENAI_API_KEY")
        model=os.getenv("OPENAI_MODEL")
        if not key: raise RuntimeError("OPENAI_API_KEY is missing in .env")
        if not model: raise RuntimeError("OPENAI_MODEL is missing in .env")
        self.client=OpenAI(api_key=key)
        self.model=model

    def generate(self,prompt):
        response=self.client.responses.create(model=self.model,input=prompt)
        return response.output_text
