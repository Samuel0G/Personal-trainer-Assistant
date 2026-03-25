# Calculando TMB
def tmb_calculos(peso, altura, idade, sexo):

    sexo = sexo.upper()

    if sexo == "M":
        return (10 * peso) + (6.25 * altura) - (5 * idade) + 5

    elif sexo == "F":
        return (10 * peso) + (6.25 * altura) - (5 * idade) - 161

    else:
        raise ValueError("Sexo inválido. Use 'M' ou 'F'.")


# Calculando gasto com base no nível de atividade
def tmb_total(tmb, nivel_atividade):
    fatores = {
        "sedentario": 1.2,
        "leve": 1.375,
        "moderado": 1.55,
        "intenso": 1.725
    }

    if nivel_atividade.lower() not in fatores:
        raise ValueError("Nível de atividade inválido.")

    return tmb * fatores[nivel_atividade.lower()]


# Cálculo de IMC
def calcular_imc(peso, altura):
    altura_m = altura / 100
    return round(peso / (altura_m ** 2), 2)