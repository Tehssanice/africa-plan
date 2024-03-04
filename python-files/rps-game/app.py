
import random
import os
from flask import Flask, render_template, request, session


app = Flask(__name__)
app.secret_key = os.urandom(24)


def get_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Tie'
    elif (user_choice == "r" and computer_choice == "s") or \
        (user_choice == "s" and computer_choice == "p") or \
            (user_choice == "p" and computer_choice == "r"):
        return 'Win'
    else:
        return 'Lose'


@app.route('/', methods=['GET', 'POST'])
def play_game():
    if 'wins' not in session:
        session['wins'] = 0
    if 'losses' not in session:
        session['losses'] = 0

    if 'ties' not in session:
        session['ties'] = 0

    if request.method == 'POST':
        user_choice = request.form['user_choice']
        computer_choice = random.choice(["r", "p", "s"])
        result = get_result(user_choice, computer_choice)

    if result == 'Win':
        session['wins'] += 1
    elif result == 'Lose':
        session['losses'] += 1
    elif result == 'Tie':
        session['ties'] += 1

    return render_template('rps.html', result=result, user_choice=user_choice, computer_choice=computer_choice, wins=session['wins'], losses=session['losses'], ties=session['ties'])


if __name__ == '__main__':
    app.run(debug=True)
