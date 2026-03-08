import json
import os

def salvar(dados):
    arquivo = "memoria.json"

    # Se o arquivo não existir, cria uma lista vazia
    if not os.path.exists(arquivo):
        with open(arquivo, "w") as f:
            json.dump([], f)

    # Ler histórico
    with open(arquivo, "r") as f:
        try:
            historico = json.load(f)
        except json.JSONDecodeError:
            historico = []

    # Garantir que seja lista
    if not isinstance(historico, list):
        historico = []

    # Adicionar novo registro
    historico.append(dados)

    # Salvar novamente
    with open(arquivo, "w") as f:
        json.dump(historico, f, indent=4)

    print("✅ Dados salvos com sucesso.")