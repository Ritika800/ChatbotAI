import random
import re

user_inputs = ["hi", "hello", "how are you?", "what's your name?", "how old are you?" ,  "Are you a robot?","How are you feeling today?",  "What do you do with my data / Do you save what I say?" ]
bot_responses = ["Hi!", "Hello!", "I'm good, thanks!", "I'm a chatbot.", "I am 24 years old","Yes I am a robot" ,"I am emotionless" , "I have saved your all data" ]

def generate_response(user_input):
    for i, pattern in enumerate(user_inputs):
        if re.search(pattern, user_input):
            return bot_responses[i]
    return random.choice(["I'm sorry, I don't understand.", "Can you please rephrase that?"])

while True:
    user_input = input("User: ")
    
    if re.search(r"(bye|goodbye|exit)", user_input, re.IGNORECASE):
        print("Bot: Goodbye!")
        break
    
    print("Bot:", generate_response(user_input))