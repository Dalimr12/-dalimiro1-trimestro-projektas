from flask import Flask, render_template

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template("about.html", active = "about")

@app.route('/gameplay')
def gameplay():
    return render_template("gameplay.html", active = "gameplay")

@app.route('/tips')
def tips():
    return render_template("tips.html", active = "tips")

@app.route('/history')
def history():
    return render_template("history.html", active = "history")

@app.route('/')
def index():
    return render_template("index.html", active = "index")

@app.route('/egg')
def egg():
    return render_template("egg.html")

    

if __name__ == "__main__":
    app.run(debug = True)