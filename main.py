from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello Pol Pujols, welcome to your first TFG Python Flask application!'

if __name__ == '__main__':
  app.run()
