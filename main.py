from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/prompt')
def prompt():
    return render_template('prompt.html')


@app.route('/no_prompt')
def no_prompt():
    return render_template('noprompt.html')


if __name__ == '__main__':
    app.run()
