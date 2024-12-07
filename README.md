# ProjetoRedes

O **Projeto Redes** é uma aplicação web construída com **Flask** e **Flask-Login**, que permite o cadastro e login de usuários. Os dados dos usuários são armazenados em um banco de dados **SQLite**. A aplicação oferece uma interface simples para registro de novos usuários, autenticação com email e senha, e uma página de dashboard acessível apenas para usuários autenticados.

## Instruções de Instalação

### 1. Criar um Ambiente Virtual

#### No Windows

1. Abra o terminal ou o prompt de comando.
2. Navegue até o diretório do projeto:
   ```bash
   cd caminho/para/o/seu/projeto
   ```
3. Crie um ambiente virtual com o comando:
   ```bash
   python -m venv env
   ```
4. Ative o ambiente virtual:
   ```bash
   .\env\Scripts\activate.bat
   ```

#### No Linux

1. Abra o terminal.
2. Navegue até o diretório do projeto:
   ```bash
   cd caminho/para/o/seu/projeto
   ```
3. Crie um ambiente virtual com o comando:
   ```bash
   python3 -m venv env
   ```
4. Ative o ambiente virtual:
   ```bash
   source env/bin/activate
   ```

### 2. Instalar as Dependências

Depois de ativar o ambiente virtual, instale as dependências do projeto:

### No Windows

```bash
pip install -r requirements-windows.txt
```

### No Linux

```bash
pip install -r requirements-linux.txt
```