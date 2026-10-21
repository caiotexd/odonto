from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Clinica(db.Model):
    __tablename__ = 'clinicas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    
    # Relacionamentos
    usuarios = db.relationship('Usuario', backref='clinica', lazy=True)
    pacientes = db.relationship('Paciente', backref='clinica', lazy=True)

    def __repr__(self):
        return f'<Clinica {self.nome}>'


class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    
    # Chave estrangeira para isolamento multi-tenant
    clinica_id = db.Column(db.Integer, db.ForeignKey('clinicas.id'), nullable=False)

    def set_password(self, password):
        self.senha_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.senha_hash, password)

    def __repr__(self):
        return f'<Usuario {self.email}>'


class Paciente(db.Model):
    __tablename__ = 'pacientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), nullable=True)
    telefone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    
    # --- ANAMNESE E ALERTAS MÉDICOS ---
    alergias = db.Column(db.Text, nullable=True)
    hipertenso = db.Column(db.Boolean, default=False)
    diabetico = db.Column(db.Boolean, default=False)
    gestante = db.Column(db.Boolean, default=False)
    medicamentos_em_uso = db.Column(db.Text, nullable=True)
    observacoes_medicas = db.Column(db.Text, nullable=True)

    # Chave estrangeira para a clínica
    clinica_id = db.Column(db.Integer, db.ForeignKey('clinicas.id'), nullable=False)

    def __repr__(self):
        return f'<Paciente {self.nome}>'