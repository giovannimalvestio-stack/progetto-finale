from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/tipi')
def tipi():
    return render_template('tipi.html')


@app.route('/cucinanellebarche')
def cucinanellebarche():
    return render_template('cucinanellebarche.html')


if __name__ == '__main__':
    app.run(debug=True)