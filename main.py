import discord
import os
from textblob import TextBlob
from web_server import serve

client = discord.Client()
keenan = ["Tovarish#7985","carnage_roger#8850"]

def translate(text,to_lang)->str:
  text_blob = TextBlob(text)
  translation = text_blob.translate(to=to_lang)
  return str(translation)

def detect_lang(text):
  language = TextBlob(text)
  return language.detect_language()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message_text = message.content
    detected_language = detect_lang(message_text)
    print(f'[LOG] Detected language: {detected_language}')
    if detected_language != "en" and str(message.author) in keenan:
      translated_text = translate(text=message_text,to_lang='en')
      await message.channel.send(f'The detected language is {detected_language} from {message.author} and its English translation is ```{translated_text}```')
    elif detected_language == "en" and message.content.lower().startswith('!keenan'):
      message_text = message.content.split("!keen ",1)[1]
      translated_text = translate(text=message_text,to_lang='ru')
      await message.channel.send(f'The detected language is {detected_language} from {message.author} and its Russian translation is ```{translated_text}```')
      
serve()
client.run(os.getenv('TOKEN'))