from flask import Flask
from flask import url_for

app = Flask(__name__)
from flask import request

@app.route('/')
def hi():
    return 'Hi'

@app.route('/user/<username>')
def show_username(username: str) -> str:
    return f'User -> {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id: int) -> str:
    return f'Post -> {post_id}'

def success():
    return 'Successfully!'

def draw_form_login():
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        success()
    draw_form_login()
    
if __name__ == '__main__':
    app.debug = True
    app.run()