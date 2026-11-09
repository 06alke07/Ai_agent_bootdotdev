import argparse
import os
import json
import sys
from dotenv import load_dotenv
from openai import OpenAI, chat
from prompts import system_prompt
from functions.call_functions import available_functions, call_function

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
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]
    for _ in range(20):
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )
        message = response.choices[0].message
        messages.append(message)
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
            #print(response.choices[0].message.content)
            if not message.tool_calls:
                print (message.content)
                return 
            for tool_call in message.tool_calls:
                #call_function(tool_call)
                result_message = call_function(tool_call, verbose=True)
                messages.append(result_message)
                
        else:
            if not message.tool_calls:
                print (message.content)
                return
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call)
                messages.append(result_message)
               
    sys.exit("achipka")




if __name__ == "__main__":
    main()
