import random

responses = {
    "greeting": ["Hello! How can I assist you?", "Hi there! What can I do for you?"],
    "goodbye": ["Goodbye! Have a great day!", "Bye! Take care!"],
    "thanks": ["You're welcome!", "No problem!"],
    "faq": {
        "what is your name": "I am ChatBot, your virtual assistant.",
        "how can I help you": "You can ask me questions or tell me what you need help with!",
    },
    "joke": """Here is a Joke for you! Sophia is heading out to the grocery store.\nA programmer tells her: get a litre of milk, and if they have eggs, get 12. 
Sophia returns with 13 litres of milk. The programmer asks her why? so, Sophia replies: 'Because they had eggs'.""",
    "fallback": ["I'm sorry, I don't understand that.", "Can you please rephrase?"],
}

def bot_reply(output):
        print(output)

def chat_bot():
    bot_reply(random.choice(responses["greeting"])+" ")

    while True:
        user_input = input().lower().strip().replace("?", "")
        if user_input in responses["faq"]:
            bot_reply(responses["faq"][user_input])
        elif any(word in user_input for word in ["hi", "hello"]):
            bot_reply(random.choice(responses["greeting"]))
        elif any(word in user_input for word in ["thanks", "thank you"]):
            bot_reply(random.choice(responses["thanks"]))
        elif any(word in user_input for word in ["bye", "goodbye"]):
            bot_reply(random.choice(responses["goodbye"]))
            break
        elif "joke" in user_input:
            bot_reply(responses["joke"])
        elif any(word in user_input for word in ["do", "can you?"]):
            bot_reply("Sorry I can't do that.")
        else:
            bot_reply(random.choice(responses["fallback"]))

chat_bot()
