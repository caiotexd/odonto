from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import Clinica, Usuario, Paciente

auth_bp = Blueprint('auth', __name__)
pacientes_bp = Blueprint('pacientes', __name__)

# ================================
# ROTAS DE AUTENTICAÇÃO
# ================================

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('pacientes.lista'))

    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and usuario.check_password(senha):
            login_user(usuario)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('pacientes.lista'))
        else:
            flash('E-mail ou senha incorretos.', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('pacientes.lista'))

    if request.method == 'POST':
        nome_clinica = request.form.get('nome_clinica')
        nome_usuario = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        if not nome_usuario or not nome_clinica or not email or not senha:
            flash('Por favor, preencha todos os campos obrigatórios.', 'danger')
            return render_template('auth/register.html')

        if Usuario.query.filter_by(email=email).first():
            flash('E-mail já cadastrado.', 'warning')
            return render_template('auth/register.html')

        # Criar Clínica
        nova_clinica = Clinica(nome=nome_clinica)
        db.session.add(nova_clinica)
        db.session.flush()

        # Criar Usuário vinculado à Clínica
        novo_usuario = Usuario(
            nome=nome_usuario,
            email=email,
            clinica_id=nova_clinica.id
        )
        novo_usuario.set_password(senha)

        db.session.add(novo_usuario)
        db.session.commit()

        flash('Conta criada com sucesso! Faça login para continuar.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu do sistema.', 'info')
    return redirect(url_for('auth.login'))


# ================================
# ROTAS DE PACIENTES (MULTI-TENANT)
# ================================

@pacientes_bp.route('/')
@pacientes_bp.route('/pacientes')
@login_required
def lista():
    # Retorna apenas os pacientes da clínica do usuário logado
    pacientes = Paciente.query.filter_by(clinica_id=current_user.clinica_id).all()
    return render_template('pacientes/lista.html', pacientes=pacientes)


@pacientes_bp.route('/pacientes/novo', methods=['GET', 'POST'])
@login_required
def novo():
    if request.method == 'POST':
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        
        # Anamnese
        alergias = request.form.get('alergias')
        hipertenso = bool(request.form.get('hipertenso'))
        diabetico = bool(request.form.get('diabetico'))
        gestante = bool(request.form.get('gestante'))
        medicamentos_em_uso = request.form.get('medicamentos_em_uso')
        observacoes_medicas = request.form.get('observacoes_medicas')

        if not nome:
            flash('O nome do paciente é obrigatório.', 'danger')
            return render_template('pacientes/novo.html')

        novo_paciente = Paciente(
            nome=nome,
            cpf=cpf,
            telefone=telefone,
            email=email,
            alergias=alergias,
            hipertenso=hipertenso,
            diabetico=diabetico,
            gestante=gestante,
            medicamentos_em_uso=medicamentos_em_uso,
            observacoes_medicas=observacoes_medicas,
            clinica_id=current_user.clinica_id
        )

        db.session.add(novo_paciente)
        db.session.commit()

        flash('Paciente cadastrado com sucesso!', 'success')
        return redirect(url_for('pacientes.lista'))

    return render_template('pacientes/novo.html')