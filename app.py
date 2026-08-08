from flask import Flask, render_template, abort, session, redirect, url_for, request
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "casa-dos-cupcakes-chave-desenvolvimento"

cupcakes = [
    {
        "id": 1,
        "nome": "Chocolate",
        "descricao": "Cupcake de chocolate com cobertura cremosa.",
        "preco": 8.00,
        "imagem": "images/chocolate.png"
    },
    {
        "id": 2,
        "nome": "Morango",
        "descricao": "Cupcake delicado com sabor de morango.",
        "preco": 8.00,
        "imagem": "images/morango.png"
    },
    {
        "id": 3,
        "nome": "Baunilha",
        "descricao": "Cupcake clássico com massa leve de baunilha.",
        "preco": 7.00,
        "imagem": "images/baunilha.png"
    },
    {
    "id": 4,
    "nome": "Red Velvet",
    "descricao": "Cupcake red velvet com cobertura de cream cheese.",
    "preco": 11.00,
    "imagem": "images/redvelvet.png"
    },
    {
    "id": 5,
        "nome": "Chocolate Belga",
        "descricao": "Cupcake premium com chocolate belga e cobertura especial.",
        "preco": 12.00,
        "imagem": "images/chocolatebelga.png"
    },
]

def inicializar_banco():
    conexao = sqlite3.connect("usuarios.db")

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


inicializar_banco()

@app.context_processor
def contador_carrinho():
    carrinho = session.get("carrinho", {})
    quantidade_carrinho = sum(carrinho.values())

    return {
    "quantidade_carrinho": quantidade_carrinho,
    "usuario_nome": session.get("usuario_nome")
}

@app.route("/")
def inicio():

    return render_template(
        "index.html",
        cupcakes=cupcakes
    )

@app.route("/contato")
def contato():
    return render_template(
        "contato.html",
        usuario_nome=session.get("usuario_nome")
    )

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if "usuario_id" in session:
        return redirect(url_for("inicio"))


    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        senha_hash = generate_password_hash(senha)

        conexao = sqlite3.connect("usuarios.db")

        try:
            conexao.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                (nome, email, senha_hash)
            )

            conexao.commit()

        except sqlite3.IntegrityError:
            conexao.close()
            return render_template(
                "cadastro.html",
                erro="Este e-mail já está cadastrado."
)

        conexao.close()

        return redirect(url_for("inicio"))

    return render_template("cadastro.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if "usuario_id" in session:
        return redirect(url_for("inicio"))

    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        conexao = sqlite3.connect("usuarios.db")
        conexao.row_factory = sqlite3.Row

        usuario = conexao.execute(
            "SELECT * FROM usuarios WHERE email = ?",
            (email,)
        ).fetchone()

        conexao.close()

        if usuario and check_password_hash(usuario["senha"], senha):
            session["usuario_id"] = usuario["id"]
            session["usuario_nome"] = usuario["nome"]

            return redirect(url_for("inicio"))

        return render_template(
            "login.html",
            erro="E-mail ou senha incorretos."
)

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("usuario_id", None)
    session.pop("usuario_nome", None)

    return redirect(url_for("inicio"))

@app.route("/adicionar/<int:id>")
def adicionar(id):

    carrinho = session.get("carrinho", {})

    if not isinstance(carrinho, dict):
        carrinho = {}

    id_str = str(id)

    if id_str in carrinho:
        carrinho[id_str] += 1
    else:
        carrinho[id_str] = 1

    session["carrinho"] = carrinho

    return redirect(url_for("detalhes", id=id))

@app.route("/adicionar-rapido/<int:id>")
def adicionar_rapido(id):

    carrinho = session.get("carrinho", {})

    if not isinstance(carrinho, dict):
        carrinho = {}

    id_str = str(id)

    if id_str in carrinho:
        carrinho[id_str] += 1
    else:
        carrinho[id_str] = 1

    session["carrinho"] = carrinho

    return redirect(url_for("inicio") + "#cupcakes")

@app.route("/cupcake/<int:id>")
def detalhes(id):

    cupcake = next(
        (c for c in cupcakes if c["id"] == id),
        None
    )

    if cupcake is None:
        abort(404)

    return render_template(
        "cupcake.html",
        cupcake=cupcake
    )

@app.route("/carrinho")
def pedidos():

    carrinho = session.get("carrinho", {})

    itens = []
    total = 0

    for cupcake in cupcakes:
        id_str = str(cupcake["id"])

        if id_str in carrinho:
            item = cupcake.copy()
            item["quantidade"] = carrinho[id_str]
            item["subtotal"] = item["preco"] * item["quantidade"]

            total += item["subtotal"]

            itens.append(item)

    return render_template(
        "pedidos.html",
        itens=itens,
        total=total
)

@app.route("/entrega", methods=["GET", "POST"])
def entrega():

    if "usuario_id" not in session:
        return redirect(url_for("login"))

    carrinho = session.get("carrinho", {})

    if not carrinho:
        return redirect(url_for("pedidos"))

    if request.method == "POST":
        return redirect(url_for("pagamento"))

    return render_template(
        "entrega.html",
        usuario_nome=session.get("usuario_nome")
    )

@app.route("/pagamento")
def pagamento():

    if "usuario_id" not in session:
        return redirect(url_for("login"))

    carrinho = session.get("carrinho", {})

    if not carrinho:
        return redirect(url_for("pedidos"))

    return render_template(
        "pagamento.html",
        usuario_nome=session.get("usuario_nome")
    )

@app.route("/pagamento/pix")
def pagamento_pix():

    if "usuario_id" not in session:
        return redirect(url_for("login"))

    carrinho = session.get("carrinho", {})

    if not carrinho:
        return redirect(url_for("pedidos"))

    return render_template(
        "pagamento_pix.html",
        usuario_nome=session.get("usuario_nome")
)

@app.route("/pagamento/cartao", methods=["GET", "POST"])
def pagamento_cartao():

    if "usuario_id" not in session:
        return redirect(url_for("login"))

    carrinho = session.get("carrinho", {})

    if not carrinho:
        return redirect(url_for("pedidos"))

    if request.method == "POST":
        return redirect(url_for("finalizar_pedido"))

    return render_template(
        "pagamento_cartao.html",
        usuario_nome=session.get("usuario_nome")
    )

@app.route("/finalizar-pedido")
def finalizar_pedido():

    if "usuario_id" not in session:
        return redirect(url_for("login"))

    carrinho = session.get("carrinho", {})

    if not carrinho:
        return redirect(url_for("pedidos"))

    session["carrinho"] = {}

    return render_template(
        "pedido_finalizado.html",
        usuario_nome=session.get("usuario_nome")
)

@app.route("/aumentar/<int:id>")
def aumentar(id):

    carrinho = session.get("carrinho", {})

    id_str = str(id)

    if id_str in carrinho:
        carrinho[id_str] += 1

    session["carrinho"] = carrinho

    return redirect(url_for("pedidos"))

@app.route("/diminuir/<int:id>")
def diminuir(id):

    carrinho = session.get("carrinho", {})

    id_str = str(id)

    if id_str in carrinho:
        carrinho[id_str] -= 1

        if carrinho[id_str] <= 0:
            del carrinho[id_str]

    session["carrinho"] = carrinho

    return redirect(url_for("pedidos"))

@app.route("/remover/<int:id>")
def remover(id):

    carrinho = session.get("carrinho", {})

    id_str = str(id)

    if id_str in carrinho:
        del carrinho[id_str]

    session["carrinho"] = carrinho

    return redirect(url_for("pedidos"))

@app.route("/esvaziar")
def esvaziar():

    session["carrinho"] = {}

    return redirect(url_for("pedidos"))

if __name__ == "__main__":
    app.run(debug=True)