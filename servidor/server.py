from flask import Flask, jsonify, request
from flask_cors import CORS  # Importa o Flask-Cors para lidar com o erro de CORS do navegador
import csv

app = Flask(__name__)  # Cria uma instância da classe Flask
CORS(app)  # Habilita o CORS para permitir requisições de diferentes origens

# Rota para realizar a busca textual
@app.route('/buscar', methods=['POST'])
def buscar_operadoras():
    termo_busca = request.form.get('termo_busca')  # Obtém o termo de busca a partir dos dados enviados na requisição POST

    operadoras = carregar_dados_csv('Relatorio_cadop(1) (2) (2).csv')  # Carrega os dados do arquivo CSV

    resultados = buscar_string(termo_busca, operadoras)  # Realiza a busca textual e retorna as linhas que mais se assemelham

    return jsonify(resultados)  # Retorna os resultados em formato JSON


# Função para para carregar os dados do arquivo CSV.
def carregar_dados_csv(nome_arquivo):
    operadoras = []

    with open(nome_arquivo, 'r', encoding='LATIN1') as arquivo:
        leitor_csv = csv.reader(arquivo, delimiter=';')

        next(leitor_csv)  # Ignora o cabeçalho do arquivo CSV, se houver

        for linha in leitor_csv:
            if linha != []:  # Verifica se a linha não está vazia
                operadoras.append(linha)

    return operadoras

# Função para realizar busca textual (procura o se o termo passado está contido nos nomes das empresas).
def buscar_string(termo_busca, operadoras):
    resultados = []

    for operadora in operadoras:
        razao_social = operadora[2] #operador[2] é a coluna referente ao nome (razão social) das empresa.
        if termo_busca.upper() in razao_social:  # Verifica se o termo de busca está contido na razão social da operadora
            resultados.append({'Registro ANS': operadora[0], 'cnpj': operadora[1], 'Razão Social': operadora[2]})

    return resultados


if __name__ == '__main__':
    app.run()  # Inicia o servidor Flask
