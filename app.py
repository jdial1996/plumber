from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('basetest.html')

@app.route('/services')
def services():
    return render_template('test.html')


@app.route('/contact')
def contact():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()

