from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Name: Manvith Rai</h1>
    <h2>AppID: APP123</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
