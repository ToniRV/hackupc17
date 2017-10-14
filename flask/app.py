import numpy as np
from flask import Flask, abort, jsonify, request
import json
import pandas as pd
import db_handler as dbh

db = pd.read_csv('transactions.csv')

# Flask App

app = Flask(__name__)

# done
@app.route('/balance', methods=['GET'])
def balance():
  res = {
    "result": dbh.get_balance(db)
  }
  return jsonify(res)

# done
@app.route('/definition', methods=['POST'])
def definition():
  data = request.get_json(force=True)
  deff = data['definition']
  res = {
      "result": dbh.get_definition(deff)
  }
  return jsonify(res)

# done
@app.route('/subscriptions', methods=['GET'])
def subscriptions():
  res = {
      "result": dbh.get_subscriptions()
  }
  return jsonify(res)

# done
@app.route('/spending', methods=['POST'])
def spending():
  data = request.get_json(force=True)
  category = data['category']
  res = {
    "result": dbh.get_spending(db,category=category)
  }
  return jsonify(res)

@app.route('/spending_since', methods=['POST'])
def spending_since():
  # return the amount spent on that object since date specified
  res = {
      "result": "Result"
  }
  return jsonify(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
