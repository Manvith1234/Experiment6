from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Name: Manvith Rai</h1>
    <h2>AppID: APP123</h2>
    <h3>Hobbies: Coding, Gym, Music</h3>
    <br>
    <a href="/resume">Download My Resume</a>
    """

@app.route("/resume")
def resume():
    return send_file("Manvith Rai.pdf")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
