Personal Trainer 💪

Sistema desenvolvido em Python para gerar treinos e recomendações de dieta personalizadas com base em dados informados pelo usuário, como idade, peso, altura e objetivo físico.

O projeto foi criado para simular o funcionamento de um assistente de planejamento de treino e alimentação, auxiliando no cálculo de necessidades calóricas e organização de rotinas de treino.

📌 Funcionalidades

Cálculo de taxa metabólica basal (TMB)

Estimativa de necessidade calórica diária

Geração de planos de treino

Sugestão de estrutura de dieta

Interface simples via terminal ou web

Organização modular do código

🧱 Estrutura do Projeto
personal-trainer-ia
│
├── app.py              # Arquivo principal do sistema
├── web_app.py          # Interface web do sistema
├── treino.py           # Lógica de geração de treinos
├── dieta.py            # Lógica de recomendações de dieta
├── calculos.py         # Cálculos metabólicos e calóricos
├── memoria.py          # Estrutura para armazenamento de dados
│
├── templates/
│   └── index.html      # Interface HTML
│
├── static/
│   └── style.css       # Estilo da interface
│
├── requirements.txt    # Dependências do projeto
└── README.md
⚙️ Requisitos

Python 3.8 ou superior

Instale as dependências:

pip install -r requirements.txt
🚀 Como executar
Executar versão principal
python app.py
Executar interface web
python web_app.py

Depois abra no navegador:

http://localhost:5000
🧮 O que o sistema calcula

O programa utiliza fórmulas tradicionais de nutrição para:

calcular metabolismo basal

estimar gasto energético

ajustar calorias conforme objetivo

Objetivos suportados:

perda de peso

manutenção

ganho de massa

🎯 Objetivo do projeto

Este projeto foi desenvolvido para praticar:

programação em Python

organização de projetos modulares

lógica aplicada a saúde e fitness

criação de interfaces simples para sistemas