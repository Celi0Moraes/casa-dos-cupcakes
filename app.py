from flask import Flask, render_template, abort, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "casa-dos-cupcakes-chave-desenvolvimento"

cupcakes = [
    {
        "id": 1,
        "nome": "Chocolate",
        "descricao": "Cupcake de chocolate com cobertura cremosa.",
        "preco": "R$ 8,00",
        "imagem": "images/chocolate.png"
    },
    {
        "id": 2,
        "nome": "Morango",
        "descricao": "Cupcake delicado com sabor de morango.",
        "preco": "R$ 8,00",
        "imagem": "images/morango.png"
    },
    {
        "id": 3,
        "nome": "Baunilha",
        "descricao": "Cupcake clássico com massa leve de baunilha.",
        "preco": "R$ 7,00",
        "imagem": "images/baunilha.png"
    },
    {
    "id": 4,
    "nome": "Red Velvet",
    "descricao": "Cupcake red velvet com cobertura de cream cheese.",
    "preco": "R$ 11,00",
    "imagem": "images/redvelvet.png"
    },
    {
    "id": 5,
        "nome": "Chocolate Belga",
        "descricao": "Cupcake premium com chocolate belga e cobertura especial.",
        "preco": "R$ 12,00",
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

    carrinho = session.get("carrinho", [])

    carrinho.append(id)

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

    ids_carrinho = session.get("carrinho", [])

    itens = [
        cupcake
        for cupcake in cupcakes
        if cupcake["id"] in ids_carrinho
    ]

    return render_template(
        "pedidos.html",
        itens=itens
    )

if __name__ == "__main__":
    app.run(debug=True)