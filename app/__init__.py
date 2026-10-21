import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave-dev-segura')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor, faça login para acessar esta página.'
    login_manager.login_message_category = 'warning'

    # Registra Blueprints
    from app.routes import auth_bp, pacientes_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(pacientes_bp)

    # Importa os models dentro do contexto para criar as tabelas
    with app.app_context():
        from app.models import Usuario, Paciente, Clinica
        
        @login_manager.user_loader
        def load_user(user_id):
            return Usuario.query.get(int(user_id))
            
        db.create_all()

    return app