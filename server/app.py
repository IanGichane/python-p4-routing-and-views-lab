#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'<h1>{parameter}</h1>'
print_string('hello')

@app.route('/count/<int:parameter>')
def count(parameter):
    for i in range(parameter):
        return '{i}<br>'
    
@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2

    if result is not None:
        return f'Result: {result}'
    else:
        return 'Invalid operation or division by zero!'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
