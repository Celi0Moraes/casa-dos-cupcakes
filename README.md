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
- Página de detalhes dos produtos
- Carrinho de compras
- Alteração de quantidade no carrinho
- Remoção de produtos
- Esvaziamento do carrinho
- Cálculo do valor total do pedido
- Cadastro de usuários
- Login e logout
- Controle de sessão do usuário
- Dados de entrega
- Seleção da forma de pagamento
- Pagamento demonstrativo via PIX
- Pagamento demonstrativo via cartão
- Finalização do pedido
- Página de contato
- Interface responsiva simples
- Publicação online no Render

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

## Evolução do projeto – PIT I para PIT II

O projeto Casa dos Cupcakes teve início no Projeto Integrador Transdisciplinar I (PIT I), no qual foi realizado o levantamento e a organização dos requisitos para uma solução destinada à venda de cupcakes. Nessa etapa foram elaboradas histórias de usuário, mapa de afinidade, backlog priorizado e a definição de requisitos e tarefas.

A proposta inicial considerava o desenvolvimento de um aplicativo móvel. Durante o PIT II, o projeto foi revisado e adaptado para uma aplicação web responsiva, permitindo sua utilização tanto em computadores quanto em dispositivos móveis.

## Revisão dos requisitos

A partir do planejamento realizado no PIT I, foram selecionados e desenvolvidos os requisitos considerados adequados para a versão atual da solução.

### Requisitos implementados

- Visualização dos cupcakes com imagem, descrição e preço
- Visualização dos detalhes dos produtos
- Cadastro de usuários
- Login e logout
- Carrinho de compras
- Alteração da quantidade dos produtos
- Remoção de produtos do carrinho
- Cálculo do valor total do pedido
- Preenchimento dos dados de entrega
- Seleção da forma de pagamento
- Pagamento demonstrativo via PIX
- Pagamento demonstrativo via cartão
- Finalização e confirmação do pedido
- Página de contato
- Interface responsiva para diferentes tamanhos e orientações de tela

### Requisitos não implementados nesta versão

Alguns requisitos previstos no planejamento inicial não foram incluídos na versão atual do sistema, permanecendo como possibilidades de expansão futura:

- Administração e edição dos produtos da vitrine
- Filtros e pesquisa de cupcakes
- Seção de cupcakes mais vendidos
- Histórico e acompanhamento de pedidos
- Painel administrativo de pedidos
- Salvamento de dados de pagamento
- Avisos de promoções
- Comentários e avaliações
- Agendamento e previsão de entrega
- Acompanhamento da entrega

## Melhorias realizadas no PIT II

Durante o desenvolvimento do PIT II, o projeto deixou de ser apenas uma especificação e passou a possuir uma solução funcional. Foram desenvolvidos o front-end e o back-end da aplicação, persistência de usuários em banco de dados, controle de sessão, fluxo de compra e interface responsiva.

A solução também foi publicada online na plataforma Render, permitindo o acesso e a realização dos testes por usuários em diferentes dispositivos.