print("RODANDO...")
from calculos import tmb_calculos, tmb_total, calcular_imc
from treino import Treino
from dieta import plano_nutricional
from memoria import salvar_usuario


# FUNÇÕES DE VALIDAÇÃO


def perguntar_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("⚠️ Digite apenas números inteiros.")


def perguntar_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("⚠️ Digite apenas números.")


def perguntar_opcao(mensagem, opcoes):
    while True:
        valor = input(mensagem).lower().strip()
        if valor in opcoes:
            return valor
        print(f"⚠️ Escolha apenas entre: {', '.join(opcoes)}")


# COLETA DE DADOS


def coletar_dados_usuario():
    print("\n--- PERSONAL TRAINER ---\n")

    idade = perguntar_int("Idade: ")
    peso = perguntar_float("Peso (kg): ")
    altura = perguntar_float("Altura (cm): ")

    sexo = perguntar_opcao("Sexo (m/f): ", ["m", "f"])

    nivel = perguntar_opcao(
        "Nível (sedentario/leve/moderado/intenso): ",
        ["sedentario", "leve", "moderado", "intenso"]
    )

    objetivo = perguntar_opcao(
        "Objetivo (emagrecer/hipertrofia/manter): ",
        ["emagrecer", "hipertrofia", "manter"]
    )

    return idade, peso, altura, sexo, nivel, objetivo


# PROCESSAMENTO


def processar_dados(idade, peso, altura, sexo, nivel, objetivo):

    tmb = tmb_calculos(peso, altura, idade, sexo)
    gasto_total = tmb_total(tmb, nivel)
    imc = calcular_imc(peso, altura)

    plano = plano_nutricional(objetivo, gasto_total, peso)
    treino = Treino(objetivo)

    return tmb, gasto_total, imc, plano, treino


# RESULTADOS


def mostrar_resultados(imc, tmb, gasto_total, plano, treino):

    print("\n--- RESULTADOS ---")

    print(f"IMC: {imc:.2f}")
    print(f"TMB: {tmb:.2f}")
    print(f"Gasto Calórico Total: {gasto_total:.2f}")

    print("\n--- DIETA ---")

    print(f"Calorias: {plano['calorias']:.0f} kcal")
    print(f"Proteína: {plano['proteina']:.1f} g")
    print(f"Gordura: {plano['gordura']:.1f} g")
    print(f"Carboidrato: {plano['carboidrato']:.1f} g")

    print("\n--- TREINO ---")
    print(treino)


# MAIN


def main():

    idade, peso, altura, sexo, nivel, objetivo = coletar_dados_usuario()

    tmb, gasto_total, imc, plano, treino = processar_dados(
        idade, peso, altura, sexo, nivel, objetivo
    )

    mostrar_resultados(imc, tmb, gasto_total, plano, treino)

    dados_usuario = {
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "sexo": sexo,
        "nivel": nivel,
        "objetivo": objetivo,
        "imc": imc,
        "tmb": tmb,
        "gasto_total": gasto_total,
        "plano": plano,
        "treino": treino}

    salvar_usuario(dados_usuario)

    input("\nPressione Enter para sair...")


# ------------------------------

if __name__ == "__main__":
    main()