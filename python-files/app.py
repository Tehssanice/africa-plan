# from flask import Flask, render_template

# app = Flask(__name__, template_folder='templates', static_folder='static')

# @app.route('/')
# def calculator():
#     return render_template('calculator.html')

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None

    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operator']

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"

    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
