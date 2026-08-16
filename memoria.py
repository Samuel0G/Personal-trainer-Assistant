import json
import os
from datetime import datetime

ARQUIVO_HISTORICO = "historico_usuarios.json"


def salvar_usuario(dados_usuario):
    """
    Salva os dados do usuário (avaliação + dieta + treino) em um
    arquivo JSON, mantendo um histórico de todas as execuções.
    """
    registro = dict(dados_usuario)
    registro["data_hora"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    historico = []

    if os.path.exists(ARQUIVO_HISTORICO):
        try:
            with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
                historico = json.load(f)
        except (json.JSONDecodeError, OSError):
            historico = []

    historico.append(registro)

    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Dados salvos em '{ARQUIVO_HISTORICO}'.")
