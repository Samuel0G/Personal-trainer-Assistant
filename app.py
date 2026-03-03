from calculos import tmb_calculos, tmb_total, calcular_imc
from treino import Treino
from dieta import plano_nutricional
from memoria import salvar
from ia import gerar_relatorio_ia

print("--- AGENTE IA PERSONAL TRAINER ---")


#--- FUNÇÕES DE VALIDAÇÃO ---

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



# --- ENTRADAS DO USUÁRIO ---


idade = perguntar_int("Idade: ")
peso = perguntar_float("Peso (kg): ")
altura = perguntar_float("Altura (cm): ")

sexo = perguntar_opcao("Sexo (m/f): ", ["m", "f"])

nivel = perguntar_opcao(
    "Nivel (sedentario/leve/moderado/intenso): ",
    ["sedentario", "leve", "moderado", "intenso"]
)

objetivo = perguntar_opcao(
    "Objetivo (emagrecer/hipertrofia/manter): ",
    ["emagrecer", "hipertrofia", "manter"]
)



# --- PROCESSAMENTO ---

tmb = tmb_calculos(peso, altura, idade, sexo)
gasto_total = tmb_total(tmb, nivel)
plano = plano_nutricional(objetivo, gasto_total, peso)
treino = Treino(objetivo)
imc = calcular_imc(peso, altura)

dados_usuario = {
    "idade": idade,
    "peso": peso,
    "altura": altura,
    "objetivo": objetivo
}

resultados = {
    "imc": imc,
    "calorias": plano['calorias'],
    "proteina": plano['proteina'],
    "gordura": plano['gordura'],
    "carboidrato": plano['carboidrato']
}

relatorio = gerar_relatorio_ia(dados_usuario, resultados)

print("\n--- ANÁLISE PERSONALIZADA ---\n")
print(relatorio)

# --- RESULTADOS ---


print("\n--- RESULTADOS ---")
print(f"IMC: {imc:.2f}")
print(f"TMB: {tmb:.2f}")
print(f"Gasto Calórico Total: {gasto_total:.2f}")
print(f"Calorias: {plano['calorias']:.0f} kcal")
print(f"Proteína: {plano['proteina']:.1f} g")
print(f"Gordura: {plano['gordura']:.1f} g")
print(f"Carboidrato: {plano['carboidrato']:.1f} g")
print("\nTreino sugerido:")
print(treino)


# --- SALVAR MEMÓRIA ---


salvar({
    "idade": idade,
    "peso": peso,
    "altura": altura,
    "tmb": tmb,
    "gasto_total": gasto_total,
    "objetivo": objetivo,
})

input("\nPressione Enter para sair...")