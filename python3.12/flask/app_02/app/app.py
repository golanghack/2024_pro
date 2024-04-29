from flask import Flask 
app = Flask(__name__)

@app.route('/user/<username>')
def index(username: str) -> str:
    return f'<h1>Hello {username}</h2>'

if __name__ == '__main__':
    app.run(debug=True)