from flask import Flask, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

@app.route("/cotacoes")
def cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()
    cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]
    dados = {
        "atualizado_em": datetime.now().isoformat(),
        "dolar": cotacao_dolar,
        "euro": cotacao_euro,
        "btc": cotacao_btc
    }
    return jsonify(dados)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
