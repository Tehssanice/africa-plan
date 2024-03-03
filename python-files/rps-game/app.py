
import random
from flask import Flask, render_template, request
app = Flask(__name__)


def get_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == "r" and computer_choice == "s") or \
        (user_choice == "s" and computer_choice == "p") or \
            (user_choice == "p" and computer_choice == "r"):
        return 'win'
    else:
        return 'lose'


@app.route('/', methods=['GET', 'POST'])
def play_game():
    if request.method == 'POST':
        user_choice = request.form['user_choice']
        computer_choice = random.choice(["r", "p", "s"])
        result = get_result(user_choice, computer_choice)

        return render_template('rps.html', result=result, user_choice=user_choice, computer_choice=computer_choice)

    return render_template('rps.html')


if __name__ == '__main__':
    app.run(debug=True)
