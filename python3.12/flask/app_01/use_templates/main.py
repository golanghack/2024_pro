from flask import render_template
from flask import Flask
app = Flask(__name__)
from flask import request

@app.route('/hi/')
@app.route('/hi/<name>')
def hi(name: str=None) -> render_template:
    return render_template('hello.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error: str=None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return login_for_user(request.form['username'])
        else:
            error = 'Invalid login for user'
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run()