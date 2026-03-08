import streamlit as st
from calculos import tmb_calculos, tmb_total, calcular_imc
from dieta import plano_nutricional
from treino import Treino
from ia import gerar_relatorio_ia

st.title("Personal Trainer IA")

idade = st.number_input("Idade", 10, 100, 25)
peso = st.number_input("Peso (kg)", 30.0, 200.0, 70.0)
altura = st.number_input("Altura (cm)", 100.0, 220.0, 170.0)

sexo = st.selectbox("Sexo", ["Masculino", "Feminino"])
nivel = st.selectbox("Nível de Atividade", ["sedentario", "leve", "moderado", "intenso"])
objetivo = st.selectbox("Objetivo", ["emagrecer", "hipertrofia", "manter"])

if st.button("Gerar Plano 🔥"):

    tmb = tmb_calculos(peso, altura, idade, sexo)
    gasto_total = tmb_total(tmb, nivel)
    plano = plano_nutricional(objetivo, gasto_total, peso)
    imc = calcular_imc(peso, altura)

    dados_usuario = {
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "objetivo": objetivo
    }

    resultados = {
        "imc": round(imc, 2),
        "calorias": round(plano['calorias']),
        "proteina": round(plano['proteina']),
        "gordura": round(plano['gordura']),
        "carboidrato": round(plano['carboidrato'])
    }

    relatorio = gerar_relatorio_ia(dados_usuario, resultados)

    st.subheader("Resultado")
    st.write(relatorio)

    st.write("### Métricas")
    st.write(resultados)

    st.write("### Treino Sugerido")
    st.write(Treino(objetivo))