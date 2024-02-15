from flask import Flask
from dotenv import dotenv_values
load_dotenv()
import os
app = Flask(__name__)

@app.route('/')
def hello():
    return f'HelloWorld {os.getenv("SECRET NAME")}'