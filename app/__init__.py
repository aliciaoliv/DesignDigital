from flask import Flask
from .rotas import configurar_rotas

def create_app():
    app = Flask(__name__)
    
    app.config.from_prefixed_env() 
    
    configurar_rotas(app)
    
    return app