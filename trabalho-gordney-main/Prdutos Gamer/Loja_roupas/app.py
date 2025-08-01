from flask import Flask, render_template

app = Flask(__name__)

# Dados de exemplo para os produtos
produtos = [
    {"id": 1, "nome": "Mouse Gamer Preto", "preco": 49.90, "imagem": "mouse.jpg"},
    {"id": 2, "nome": "Teclado Mecanico Gamer", "preco": 129.90, "imagem": "tecladoGamer.jpg"},
    {"id": 3, "nome": "Headset Gamer HyperX", "preco": 199.90, "imagem": "HeadsetGamer.jpg"},
    {"id": 4, "nome": "MONITOR SAMSUNG ODYSSEY ARK", "preco": 299.90, "imagem": "telinha.jpg"},
    {"id": 5, "nome": "Placa de Video GTX 1050 4GB", "preco": 1050.50, "imagem": "gtx1050.jpg"},

]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produtos')
def mostrar_produtos():
    return render_template('produtos.html', produtos=produtos)

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)