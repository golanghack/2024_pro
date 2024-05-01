from flask_script import Manager 
from flask import Flask 
app = Flask(__name__)
manager = Manager(app)

@app.route('/user/<username>')
def index(username: str) -> str:
    return f'<h1>Hello {username}</h2>'

if __name__ == '__main__':
    manager.run()