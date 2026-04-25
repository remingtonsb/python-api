from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Dados em memória para demonstração
conta = {
    "saldo": 1000.0,
    "historico": []
}

@app.route('/extrato', methods=['GET'])
def extrato():
    return jsonify({
        "saldo_atual": conta["saldo"],
        "transacoes": conta["historico"],
        "data_consulta": datetime.datetime.now().isoformat()
    }), 200

@app.route('/saque', methods=['POST'])
def saque():
    dados = request.get_json()
    valor = dados.get('valor')

    if not valor or valor <= 0:
        return jsonify({"erro": "Valor de saque inválido"}), 400
    
    if valor > conta["saldo"]:
        return jsonify({"erro": "Saldo insuficiente"}), 403

    # Processa o saque
    conta["saldo"] -= valor
    transacao = {
        "tipo": "saque",
        "valor": valor,
        "data": datetime.datetime.now().isoformat()
    }
    conta["historico"].append(transacao)

    return jsonify({
        "mensagem": "Saque realizado com sucesso",
        "novo_saldo": conta["saldo"]
    }), 200

if __name__ == '__main__':
    # O OpenShift geralmente espera que a app ouça na porta 8080
    app.run(host='0.0.0.0', port=8080)
