import sqlite3
import json
from datetime import datetime

ARQUIVO_BANCO = "personal_trainer.db"


def _conectar():
    conexao = sqlite3.connect(ARQUIVO_BANCO)
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS avaliacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT NOT NULL,
            idade INTEGER NOT NULL,
            peso REAL NOT NULL,
            altura REAL NOT NULL,
            sexo TEXT NOT NULL,
            nivel TEXT NOT NULL,
            objetivo TEXT NOT NULL,
            imc REAL NOT NULL,
            tmb REAL NOT NULL,
            gasto_total REAL NOT NULL,
            calorias REAL NOT NULL,
            proteina REAL NOT NULL,
            gordura REAL NOT NULL,
            carboidrato REAL NOT NULL,
            treino TEXT NOT NULL
        )
    """)
    return conexao


def salvar_usuario(dados_usuario):
    """
    Salva os dados do usuário (avaliação + dieta + treino) no banco
    SQLite (personal_trainer.db), mantendo um histórico de todas
    as execuções na tabela 'avaliacoes'.
    """
    plano = dados_usuario["plano"]

    conexao = _conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO avaliacoes (
            data_hora, idade, peso, altura, sexo, nivel, objetivo,
            imc, tmb, gasto_total, calorias, proteina, gordura,
            carboidrato, treino
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        dados_usuario["idade"],
        dados_usuario["peso"],
        dados_usuario["altura"],
        dados_usuario["sexo"],
        dados_usuario["nivel"],
        dados_usuario["objetivo"],
        dados_usuario["imc"],
        dados_usuario["tmb"],
        dados_usuario["gasto_total"],
        plano["calorias"],
        plano["proteina"],
        plano["gordura"],
        plano["carboidrato"],
        dados_usuario["treino"],
    ))

    conexao.commit()
    conexao.close()

    print(f"\n✅ Dados salvos em '{ARQUIVO_BANCO}'.")


def listar_historico():
    """
    Retorna todas as avaliações já registradas, da mais recente
    para a mais antiga.
    """
    conexao = _conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM avaliacoes ORDER BY id DESC")
    colunas = [descricao[0] for descricao in cursor.description]
    linhas = cursor.fetchall()

    conexao.close()

    return [dict(zip(colunas, linha)) for linha in linhas]


def exportar_para_json(caminho="historico_usuarios.json"):
    """
    Exporta o histórico completo do banco SQLite para um arquivo
    JSON (útil para backup ou compatibilidade com versões antigas).
    """
    historico = listar_historico()

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Histórico exportado para '{caminho}'.")


if __name__ == "__main__":
    # Execução direta: mostra o histórico salvo no banco
    registros = listar_historico()

    if not registros:
        print("Nenhum registro encontrado ainda.")
    else:
        print(f"\n{len(registros)} avaliação(ões) encontrada(s):\n")
        for r in registros:
            print(
                f"[{r['id']}] {r['data_hora']} - "
                f"{r['idade']} anos, {r['peso']}kg, objetivo: {r['objetivo']}, "
                f"IMC: {r['imc']:.2f}"
            )
