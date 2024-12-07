from flask import Flask, render_template \
    , url_for, request, redirect

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

    return render_template('login.html') #adicionar uma flag que tem no flask de tipo: "Você não tem cadastro"
    

@app.route('/register', methods=['POST', 'GET'])
def register():

    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['pass']
        conexao = obter_conexao()
        INSERT = 'INSERT INTO usuarios(email,senha) VALUES (?,?)'
        conexao.execute(INSERT, (email, senha))
        conexao.commit()
        conexao.close()
        return redirect(url_for('index'))

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


