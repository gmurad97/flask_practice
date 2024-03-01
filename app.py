from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/shop")
def shop():
    return "shop"

if __name__ == "__main__":
    app.run(debug=True)
