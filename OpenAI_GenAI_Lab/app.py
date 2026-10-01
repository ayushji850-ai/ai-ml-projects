import os
from dotenv import load_dotenv
from prompts.methods import METHODS
from providers_openai import OpenAIProvider

load_dotenv()

METHODS_LIST=list(METHODS.keys())

def main():
    print("="*60)
    print("GenAI Prompt Lab — OpenAI")
    print("="*60)
    for i,m in enumerate(METHODS_LIST,1):
        print(f"{i}. {m}")
    try:
        method=METHODS_LIST[int(input("\nChoose method: "))-1]
    except (ValueError,IndexError):
        print("Invalid method."); return

    topic=input("Enter topic/question: ").strip()
    if not topic:
        print("Topic cannot be empty."); return

    try:
        provider=OpenAIProvider()
        prompt=METHODS[method](topic)
        print("\nSending request...")
        answer=provider.generate(prompt)
        print("\n"+"="*60)
        print("Provider: OpenAI")
        print("Method:",method)
        print("="*60)
        print(answer)
    except Exception as e:
        print("\nERROR:",e)
        print("Check .env, model ID, API access, package installation, and network.")

if __name__=="__main__":
    main()
