# 🏋️ Personal Trainer IA 

Agente híbrido de Personal Trainer desenvolvido em **Python**, combinando:

* 📊 Cálculos determinísticos (TMB, IMC, gasto calórico)
* 🥗 Geração de plano nutricional automatizado
* 🏋️ Sugestão de treino baseada em objetivo
* 🤖 LLM local com Ollama (100% offline)

---

## 🚀 Objetivo do Projeto

Criar um agente inteligente capaz de:

1. Coletar dados físicos do usuário
2. Calcular métricas metabólicas
3. Gerar plano alimentar estruturado
4. Produzir análise personalizada com IA
5. Rodar totalmente offline

Arquitetura híbrida:

```
Regras matemáticas + LLM interpretativa = Agente inteligente
```

---

## 🧠 Arquitetura do Projeto

```
personal-trainer-ia/
│
├── app.py          # Orquestração principal
├── calculos.py     # TMB, IMC e gasto calórico
├── dieta.py        # Regras nutricionais
├── treino.py       # Sugestão de treino
├── memoria.py      # Persistência de dados
└── ia.py           # Integração com LLM (Ollama)
```

Separação clara de responsabilidades:

* `app.py` → fluxo do programa
* `ia.py` → inteligência artificial
* Módulos auxiliares → lógica determinística

---

## ⚙️ Tecnologias Utilizadas

* Python 
* Ollama
* JSON

---

## 💻 Como Rodar o Projeto

### 1️⃣ Instalar dependências

```bash
pip install ollama
```

### 2️⃣ Instalar Ollama

Baixe em:
[https://ollama.com](https://ollama.com)

### 3️⃣ Baixar modelo

```bash
ollama pull llama3
```

Ou modelo mais leve:

```bash
ollama pull mistral
```

### 4️⃣ Executar

```bash
python app.py
```

---

## 📌 Status

✔ Arquitetura modular
✔ LLM offline funcional
✔ Sistema pronto para expansão
