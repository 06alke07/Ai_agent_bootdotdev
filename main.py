import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI, chat

def main():
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None:
        raise RuntimeError("Api key is not found or expired. Check a provider")
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="Chabot")
    args = parser.parse_args()
    messages = [{"role": "user", "content": args.user_prompt},]
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages
    )
    
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
