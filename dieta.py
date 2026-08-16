def plano_nutricional(objetivo, gasto_total, peso):
    objetivo = objetivo.lower()

    # Ajuste calórico
    if objetivo == "emagrecer":
        calorias = gasto_total * 0.85
        proteina = peso * 2.0

    elif objetivo == "hipertrofia":
        calorias = gasto_total * 1.10
        proteina = peso * 2.0

    elif objetivo == "manter":
        calorias = gasto_total
        proteina = peso * 1.6

    else:
        raise ValueError("Objetivo inválido.")

    gordura = peso * 0.8

    calorias_proteina = proteina * 4
    calorias_gordura = gordura * 9

    carboidrato = (calorias - calorias_proteina - calorias_gordura) / 4

    return {
        "calorias": calorias,
        "proteina": proteina,
        "gordura": gordura,
        "carboidrato": carboidrato
    }