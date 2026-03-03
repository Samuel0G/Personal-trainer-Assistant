import ollama

def gerar_relatorio_ia(dados_usuario, resultados):

-- DADOS PARA IA --

    prompt = f"""
Você é um coach estilo Growth.

RESPONDA SOMENTE EM PORTUGUÊS DO BRASIL.
Nunca responda em inglês.

Gere um resumo direto e motivador.
Máximo 6 linhas.
Sem texto longo.
Foco em resultado.

Dados:
Idade: {dados_usuario['idade']}
Peso: {dados_usuario['peso']} kg
Altura: {dados_usuario['altura']} cm
Objetivo: {dados_usuario['objetivo']}

Resultados:
IMC: {resultados['imc']}
Calorias: {resultados['calorias']} kcal
Proteína: {resultados['proteina']} g
Gordura: {resultados['gordura']} g
Carboidrato: {resultados['carboidrato']} g
"""
-- ESPECIFICAÇÕES PARA IA --
    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': prompt}],
        options={
            "temperature": 0.6,
            "num_predict": 180
        }
    )

    return response['message']['content']