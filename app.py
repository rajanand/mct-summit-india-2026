from flask import Flask, session, redirect, url_for, render_template, request
from game_logic import Board

app = Flask(__name__)
app.secret_key = 'secret_key_for_session'

board = Board()  # Global board instance

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            session['logged_in'] = True
            return redirect(url_for('game'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/game')
def game():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    probabilities = board.get_win_probabilities()
    return render_template('game.html', 
                           board=board.get_board(), 
                           current_player=board.get_current_player(),
                           winner=board.check_win(),
                           draw=board.check_draw(),
                           probabilities=probabilities)

@app.route('/move', methods=['POST'])
def move():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    row = int(request.form['row'])
    col = int(request.form['col'])
    board.make_move(row, col)
    probabilities = board.get_win_probabilities()
    return render_template('game.html', 
                           board=board.get_board(), 
                           current_player=board.get_current_player(),
                           winner=board.check_win(),
                           draw=board.check_draw(),
                           probabilities=probabilities)

@app.route('/reset', methods=['POST'])
def reset():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    board.reset()
    probabilities = board.get_win_probabilities()
    return render_template('game.html', 
                           board=board.get_board(), 
                           current_player=board.get_current_player(),
                           winner=board.check_win(),
                           draw=board.check_draw(),
                           probabilities=probabilities)

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)