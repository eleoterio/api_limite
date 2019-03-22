#PARTE1
from flask import Flask, request
import redis
import os
import json

r = redis.Redis(host='localhost', port=6379, db=0)
app = Flask(__name__)

@app.route('/v1/products', methods=['POST'])
def products():
  _json = request.json

  validade = r.sadd(json.dumps(_json), 'ok')
  if validade == 0:
    return str('403 Forbidden'), 403
  else:
    response = r.sadd('request', json.dumps(_json))
    r.expire(json.dumps(_json),10)

  result = r.smembers('request')
  return str(result)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='127.0.0.1', port=port)
  