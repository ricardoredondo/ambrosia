import os
from flask import Flask, session, g
from dotenv import load_dotenv, find_dotenv
from flask_cors import CORS

from controllers.api_controller import api_bp
from controllers.service_controller import service_bp
# from pathlib import Path
from services.vector_db import VectorDB
from services.dexter import Dexter



_ = load_dotenv(find_dotenv()) # read local .env file
# env_path = Path('..') / '.env'
# _ = load_dotenv(dotenv_path=env_path) 


app = Flask(__name__)
app.secret_key = os.environ['SERVER_KEY']  # Replace with a secure key

# Enable CORS for all routes
CORS(app)


# Register blueprints
app.register_blueprint(api_bp)
app.register_blueprint(service_bp)

# Initialize custom objects
with app.app_context():
    app.config['VERSION']   = "0.0.2"
    app.config['LLM_NAME']  = "gpt-4o"
    app.config['VDB']       = VectorDB(app.config['LLM_NAME'])

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to Ambrosia. Just a quick RAG application. '

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080 , debug=True)
    