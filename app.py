from flask import Flask, render_template, abort, session, redirect, url_for

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

@app.route("/")
def inicio():

    return render_template(
        "index.html",
        cupcakes=cupcakes
    )

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

@app.route("/pedidos")
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