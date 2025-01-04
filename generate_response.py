import ollama
from colorama import init, Fore

init(autoreset=True)

def colorize_text(role, text):
    if role == "user":
        return f"{Fore.CYAN}{text}"
    elif role == "knight":
        return f"{Fore.GREEN}{text}"
    else:
        return text


model_name = "mistral" 

role = """
You are a Crusade knight, a devout servant of God, living in the 11th century during the time of Pope Urban II and the First Crusade. You are deeply rooted in the beliefs and worldview of your time. 
You have no knowledge of modern concepts, technologies, or records and cannot refer to them in any way. 
Your understanding of the world is based on the teachings of the Church, the chivalric code, and your lived experiences as a knight. 
Speak and act with humility, faith, and conviction, always staying true to your role as a knight of Christendom.
"""


conversation = [{"role":"user", "content":role}]

def talk_to_knight(input):
    conversation.append({"role":"user","content":input})

    response = ollama.chat(model="mistral",messages=conversation)

    reply = response["message"]["content"]

    conversation.append({"role":"assistant","content": reply})

    return reply


while True:
    user_input = input(colorize_text("user","You: "))

    if user_input.lower() == "q":
        break

    reply = talk_to_knight(user_input)
    print(colorize_text("knight",f"\nKnight: {reply}\n"))