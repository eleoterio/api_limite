#PARTE1
from flask import Flask, request
import redis 
import os
import json

r = redis.Redis(host='redis', port=6379)
app = Flask(__name__)

@app.route('/v1/products', methods=['POST'])
def products():
  _json = request.json

  validade = r.sadd(json.dumps(_json), 'ok')
  if validade == 0:
    return str('403 Forbidden'), 403
  else:
    response = r.sadd('request', json.dumps(_json))
    r.expire(json.dumps(_json),600)

  result = r.smembers('request')
  return str(result)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  