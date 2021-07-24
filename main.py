import discord
import os
from textblob import TextBlob, exceptions
from web_server import serve

client = discord.Client()
keenan = ["Tovarish#7985","carnage_roger#8850"]
ERROR_CODE = 'ERROR'

def translate(text,to_lang)->str:
  text_blob = TextBlob(text)
  try:
    translation = text_blob.translate(to=to_lang)
  except exceptions.NotTranslated:
    translation = 'Sorry, original message was not translated!'
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
    try:
      detected_language = detect_lang(message_text)
    except exceptions.TranslatorError:
      detected_language = ERROR_CODE      
    print(f'[LOG] Detected language: {detected_language}')
    if message.content.lower().startswith('!keen'):
      if detected_language != ERROR_CODE:
        message_text = message.content[5:]
        translated_text = translate(text=message_text,to_lang='ru')
        await message.channel.send(f'```{translated_text}```')
        print(f'[LOG] Text that was translated: {message_text}')
      else:
        await message.channel.send(f'```Sorry, but text to be translated needs to be at least 3 characters long.```')
    elif (detected_language != "en" or detected_language == ERROR_CODE) and str(message.author) in keenan:
      if detected_language != ERROR_CODE:
        translated_text = translate(text=message_text,to_lang='en')
        await message.channel.send(f'```{translated_text}```')
        print(f'[LOG] Text that was translated: {message_text}')
      else:
        await message.channel.send(f'```Sorry, but text to be translated needs to be at least 3 characters long.```')
      
serve()
client.run(os.getenv('TOKEN'))