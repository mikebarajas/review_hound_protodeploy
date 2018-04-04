from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index.html')
def indexNavigation():
    return render_template("index.html")


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/sniffer.html")
def sniffer():
    return render_template("sniffer.html")


# Heroku Mode
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT')))
