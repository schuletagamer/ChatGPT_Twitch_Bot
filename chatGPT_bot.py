import os # for importing env vars for the bot to use
#from twitchio.ext import commands
import openai
import pyttsx3
from gtts import gTTS
import playsound
from twitchio.ext import commands

oauth_token = "jqrddt3o3lf4qiorva03mw642wbjbb"
client_id = "v3oogqwxgxqdodjavn78078nkaq6k3"
bot_account = 'schuletinha'
channel_name = 'Schuletagamer'

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

start_sequence = "\nChatGPT"
restart_sequence = "\nChat: "

prompt = "Você é um chatbot assistente do streamer Schuletagamer da Twitch e está respondendo às solicitações do usuário enquanto se faz passar pelo streamer fazendo parte da comunidade e age como um visualizador independente e é legal com todos criando uma atmosfera natural, envolvente, engraçado e agradável tentando fazer uma piada aqui e ali mas, não se envolve em conversas sobre política ou religião e é respeitoso com todos."
chat_log = prompt

def ask(question, chat_log=None):
    prompt_text = f"{chat_log}{restart_sequence}: {question}{start_sequence}:"
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt_text,
    temperature=0.98,
    max_tokens=218,
    top_p=1,
    frequency_penalty=0.47,
    presence_penalty=0.6,
    stop=['\n'],
    )
    
    answer = response['choices'][0]['text']
    return str(answer)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None: 
        chat_log = prompt 

        return f"{chat_log}{restart_sequence} {question}{start_sequence}{answer}"

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 180)
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def read_chat(text):
    speak(str(text))


def chatGPT(message):
    incoming_msg = message
    answer = ask(incoming_msg, chat_log)
    append_interaction_to_chat_log(incoming_msg, answer, chat_log)

    print(str(answer))
    speak(str(answer))

