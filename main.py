from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Olá, Mundo Python! O pipeline GitOps funcionou!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

#trigger-pipe5
