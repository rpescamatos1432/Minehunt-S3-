from flask import Flask, render_template_string, request

app = Flask(__name__)

# Lista para armazenar os dados dos usuários registrados
user_data = []

# HTML completo com CSS e JavaScript
html_home = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Servidor Minehunt</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }

        header {
            background: #4CAF50;
            color: white;
            padding: 20px;
            text-align: center;
        }

        h1, h2 {
            transition: color 0.3s ease;
        }

        h2:hover {
            color: #FFD700; /* Gold */
        }

        section {
            margin: 20px;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s;
            margin: 5px;
        }

        button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }

        .info {
            margin: 20px 0;
        }
    </style>
</head>
<body>

<header>
    <h1>Bem-vindo ao Servidor Minehunt</h1>
    <p>Onde matar te dá poder! Roubas corações, perdes corações e lutas pelo topo!</p>
</header>

<section id="about">
    <h2>Sobre o servidor</h2>
    <p>Neste servidor de anarquia, ao matar outro jogador, você rouba um coração dele, o que aumenta seu poder. Mas cuidado: se você for morto, perderá um coração. Essa dinâmica cria um ambiente de constante tensão e estratégia, onde cada decisão pode ser a diferença entre a vida e a morte.</p>
    <p>O servidor tem regras simples: jogue, mate, sobreviva. A comunidade é acolhedora, e todos os jogadores têm um espaço para crescer e se tornar mais fortes. Prepare-se para batalhas épicas e alianças inesperadas!</p>
</section>

<section class="info">
    <h2>Características do Servidor</h2>
    <ul>
        <li>🌍 Mundo aberto e dinâmico</li>
        <li>⚔️ Arena PvP para batalhas emocionantes</li>
        <li>🏰 Criação de cidades e alianças</li>
        <li>💰 Sistema econômico para comprar e vender itens</li>
    </ul>
</section>

<section class="info">
    <h2>Regras do Servidor</h2>
    <ul>
        <li>Respeito mútuo entre jogadores.</li>
        <li>Comportamento apropriado no chat.</li>
        <li>Reportar bugs à administração.</li>
        <li>Não compartilhar informações de conta.</li>
    </ul>
</section>

<button onclick="window.location.href='/register'">Registrar</button>
<button onclick="window.location.href='/show_users'">Ver Usuários Registrados</button>

</body>
</html>
"""

html_register = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registrar - Servidor Minehunt</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }

        header {
            background: #4CAF50;
            color: white;
            padding: 20px;
            text-align: center;
        }

        form {
            margin: 20px;
            padding: 20px;
            background: #e2e2e2;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        label {
            display: block;
            margin: 10px 0 5px;
        }

        input {
            width: calc(100% - 22px);
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s;
        }

        button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
    </style>
</head>
<body>

<header>
    <h1>Registrar no Servidor Minehunt</h1>
</header>

<section id="register">
    <form method="POST" action="/register">
        <label for="name">Nome:</label>
        <input type="text" id="name" name="name" required>

        <label for="age">Idade:</label>
        <input type="number" id="age" name="age" required>

        <label for="interests">Gostos:</label>
        <input type="text" id="interests" name="interests" required>

        <label for="nickname">Nick:</label>
        <input type="text" id="nickname" name="nickname" required>

        <button type="submit">Registrar</button>
    </form>
</section>

<button onclick="window.location.href='/'">Voltar para a Página Inicial</button>

</body>
</html>
"""

html_users = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Usuários Registrados - Servidor Minehunt</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }

        header {
            background: #4CAF50;
            color: white;
            padding: 20px;
            text-align: center;
        }

        section {
            margin: 20px;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        li {
            margin: 10px 0;
            padding: 10px;
            background: #e2e2e2;
            border-radius: 4px;
        }

        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.2s;
            margin: 5px;
        }

        button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
    </style>
</head>
<body>

<header>
    <h1>Usuários Registrados</h1>
</header>

<section>
    <h2>Lista de Usuários</h2>
    <ul>
        {% for user in users %}
        <li>{{ user.nickname }} - {{ user.name }}, {{ user.age }} anos. Gostos: {{ user.interests }}</li>
        {% endfor %}
    </ul>
</section>

<button onclick="window.location.href='/'">Voltar para a Página Inicial</button>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_home)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        interests = request.form['interests']
        nickname = request.form['nickname']
        
        user_data.append({
            'name': name,
            'age': age,
            'interests': interests,
            'nickname': nickname
        })
        return render_template_string(html_home)  # Redireciona para a página inicial após o registro
    return render_template_string(html_register)

@app.route('/show_users')
def show_users():
    return render_template_string(html_users, users=user_data)

if __name__ == '__main__':
    app.run(debug=True)