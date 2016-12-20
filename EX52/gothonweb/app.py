from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map

app = Flask(__name__)

@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        return render_template('you_died.html')


@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:
            #no userinput
            return render_template('you_died.html')
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                return render_template('show_scene.html', scene=nextscene)
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:
        return render_template('you_died.html')



# This URL initializes the session with starting values
@app.route('/')
def index():
    session['scene'] = map.START.urlname
    return redirect(url_for('game_get')) #redirect the browser to the url for game_get
# This is for the button to jump to the target URL
@app.route('/help', methods=['POST'])
def help_post():
    if request.form["action"] == "Reference":
        return render_template('help.html')
    if request.form["action"] == "Jump to Final Scene":
        x = map.SCENES['the_end_winner']
        return render_template('show_scene.html', scene=x)

        return render_template('help.html')

@app.route('/help', methods=['GET'])
def help_get():
    if request.form.get('add', None) == "Reference":
        pass
    elif request.form.get('remove', None) == "Jump to Final Scene":
        pass


app.secret_key = '555'

if __name__ == "__main__":
    app.run()
