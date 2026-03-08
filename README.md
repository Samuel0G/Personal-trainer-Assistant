# 🏋️ Personal Trainer 

Agente híbrido de Personal Trainer desenvolvido em **Python**, combinando:

* 📊 Cálculos determinísticos (TMB, IMC, gasto calórico)
* 🥗 Geração de plano nutricional automatizado
* 🏋️ Sugestão de treino baseada em objetivo
---

## 🚀 Objetivo do Projeto

Criar um programa inteligente capaz de:

1. Coletar dados físicos do usuário
2. Calcular métricas metabólicas
3. Gerar plano alimentar estruturado

## 🧠 Arquitetura do Projeto

```
personal-trainer
│
├── app.py          # Orquestração principal
├── calculos.py     # TMB, IMC e gasto calórico
├── dieta.py        # Regras nutricionais
├── treino.py       # Sugestão de treino
├── memoria.py      # Persistência de dados
```

Separação clara de responsabilidades:

* `app.py` → fluxo do programa
* Módulos auxiliares → lógica determinística

---

## ⚙️ Tecnologias Utilizadas

* Python
* JSON

---

## 💻 Como Rodar o Projeto

### 4️⃣ Executar

```bash
python app.py
```

---

## 📌 Status

✔ Arquitetura modular
✔ Sistema pronto para expansão
