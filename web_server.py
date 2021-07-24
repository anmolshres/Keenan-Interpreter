from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am Keenan Interpreter bot! Add me to your server with this link: https://discord.com/api/oauth2/authorize?client_id=868328713002057758&permissions=2148002880&scope=bot"

def run():
  app.run(host='0.0.0.0',port=8080)

def serve():
    t = Thread(target=run)
    t.start()