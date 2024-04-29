from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/hi/')
@app.route('/hi/<name>')
def hi(name: str=None) -> render_template:
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()