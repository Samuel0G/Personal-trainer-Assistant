#Geração de treino
def Treino(objetivo):
    objetivo = objetivo.lower()

    if objetivo == "emagrecer":
        return """
Treino ABC + Cardio:
A - Peito + Triceps + 20-30min cardio moderado
B - Costas + Biceps + 20-30min cardio
C - Pernas + HIIT 15min
Foco: Déficit calórico + alta frequência.
"""

    elif objetivo == "hipertrofia":
        return """
Treino ABC focado em sobrecarga progressiva:
A - Peito + Triceps (6-12 reps)
B - Costas + Biceps (6-12 reps)
C - Pernas (agachamento, levantamento terra)
Foco: Progressão de carga + superávit calórico.
"""

    elif objetivo == "manter":
        return """
Treino Full Body 3x por semana:
Exercícios compostos + intensidade moderada.
Foco: manutenção de massa e saúde geral.
"""