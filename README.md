# Casa dos Cupcakes

Projeto desenvolvido para a disciplina Projeto Integrador Transdisciplinar II do curso de Engenharia de Software.

## Sobre o projeto

A Casa dos Cupcakes é uma loja virtual desenvolvida com Python e Flask.

O sistema permite que o usuário:

- visualizar os cupcakes disponíveis;
- acessar a página de detalhes de cada produto;
- adicionar produtos ao carrinho;
- aumentar ou diminuir a quantidade;
- remover produtos;
- esvaziar o carrinho;
- visualizar o valor total do pedido.

## Tecnologias utilizadas

- Python
- Flask
- HTML5
- CSS3
- Jinja2

## Estrutura do projeto

```
casa-dos-cupcakes/
│
├── app.py
├── requirements.txt
├── README.md
├── static/
│   ├── css/
│   └── images/
└── templates/
    ├── index.html
    ├── cupcake.html
    └── pedidos.html
```

## Como executar

1. Clone o repositório.

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o projeto:

```bash
python app.py
```

4. Abra o navegador em:

```
http://127.0.0.1:5000
```

## Funcionalidades implementadas

- Página inicial
- Lista de cupcakes
- Página de detalhes
- Carrinho de compras
- Alteração de quantidade
- Remoção de produtos
- Esvaziar carrinho
- Total do pedido
- Interface responsiva simples

---

Projeto desenvolvido para fins acadêmicos.

## Hospedagem

A aplicação está publicada online utilizando a plataforma Render.

- Plataforma: Render
- Tipo de serviço: Web Service
- Runtime: Python 3
- Servidor de aplicação: Gunicorn
- Branch de publicação: main

### Acesso à aplicação

https://casa-dos-cupcakes.onrender.com