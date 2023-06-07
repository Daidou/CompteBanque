from flask import Flask


app = Flask(__name__)


@app.route('/')
def home(): 
    return 'Page d\'accueil'


if __name__ == '__main__':
    app.run()