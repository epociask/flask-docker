import os
import json 

from flask import request
from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def bye(): 
  try:
    name = request.args.get('name')
    return f"Goodbye {name}!"
  except Exception as e:
    print(e)
    return "could not unmarshall request"

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
