import random
import pyttsx3 as pytalk

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
voiceFound = False
try:
    voice = pytalk.init()
    voices = voice.getProperty('voices')
    voice.setProperty('voice', voices[1].id)
    voice.setProperty('rate', 135)
    voiceFound = True
    print("voice activated!")
except:
    print("""couldn't find voice module \ndownload python library "pyttsx3" for voices""")

def bot_reply(output):
    if voiceFound:
        voice.say(output)
        print(output)
        voice.runAndWait()
    else:
        print(output)

def chat_bot():
    bot_reply(random.choice(responses["greeting"])+" ")

    while True:
        user_input = input().lower().strip().replace("?", "")
        if "joke" in user_input:
            bot_reply(responses["joke"])
        elif user_input in responses["faq"]:
            bot_reply(responses["faq"][user_input])
        elif any(word in user_input for word in ["hi", "hello"]):
            bot_reply(random.choice(responses["greeting"]))
        elif any(word in user_input for word in ["thanks", "thank you"]):
            bot_reply(random.choice(responses["thanks"]))
        elif any(word in user_input for word in ["bye", "goodbye"]):
            bot_reply(random.choice(responses["goodbye"]))
            break
        elif any(word in user_input for word in ["do", "can you?"]):
            bot_reply("Sorry I can't do that.")
        elif user_input == "deactivate":
            print("voice deactivated!")
            voiceFound = False
        elif user_input == "activate":
            print("voice activated!")
            voiceFound = True
        else:
            bot_reply(random.choice(responses["fallback"]))

chat_bot()