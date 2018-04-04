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


# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)