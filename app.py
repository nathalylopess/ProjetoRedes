from flask import Flask, render_template \
    , url_for, request, redirect, flash, get_flashed_messages

from flask_login import LoginManager \
    , login_required, login_user, logout_user

from models import User, obter_conexao

login_manager = LoginManager()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUPERMEGADIFICIL'
login_manager.init_app(app)

# quando precisar saber qual o usuario conecato
# temos como consultar ele no banco
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['pass']
        
        user = User.get_by_email(email)

        if user and user.senha == senha:
            login_user(user)
            return redirect(url_for('dash'))
        else:
            flash('E-mail ou senha inválidos.')  # Mensagem de erro

    return render_template('login.html')
    

@app.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['pass']
        
        # Verifica se ambos os campos estão preenchidos
        if not email or not senha:
            flash("Por favor, preencha todos os campos.")  # Mensagem de erro
            return redirect(url_for('register')) 
        
        # Verifica se o email já está cadastrado
        conexao = obter_conexao()
        SELECT = 'SELECT * FROM usuarios WHERE email=?'
        user_exists = conexao.execute(SELECT, (email,)).fetchone()
        conexao.close()
        
        if user_exists:
            flash("Este email já está cadastrado.")  # Mensagem de erro
            return redirect(url_for('register'))  # Redireciona de volta para a página de registro
        
        # Insere o novo usuário no banco de dados
        conexao = obter_conexao()
        INSERT = 'INSERT INTO usuarios(email,senha) VALUES (?,?)'
        conexao.execute(INSERT, (email, senha))
        conexao.commit()
        conexao.close()

        # Recupera o usuário recém-criado
        user = User.get_by_email(email)

        # Faz login automático após o registro
        if user:
            login_user(user)

        # Redireciona para o dashboard
        return redirect(url_for('dash'))

    return render_template('register.html')

@app.route('/dash')
@login_required
def dash():
    usuarios = User.get_all()
    return render_template('dash.html', usuarios=usuarios)


@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))


