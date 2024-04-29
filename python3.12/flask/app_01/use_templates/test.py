from flask import request
from main import app

with app.test_request_context('/hi', method='POST'):
    assert request.path == '/hi'
    assert request.method == 'POST'