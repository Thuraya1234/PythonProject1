#Code to integrate ChatGPT API with python ......
import openai
#load and set our key 
k = open("key.txt", "r")
openai.api_key = k.read().strip("\n")

messages = [
    {"role": "system", "content": "You are a software engineer,use words with some emojis"},
]
#....................................  
while True:
    message = input("User : ")
    if not(message == "thanks"):
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    else:
        break
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
   
    