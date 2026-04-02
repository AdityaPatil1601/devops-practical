from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello! DevOps Practical Running Successfully"
    return "My name is Aditya"
    return "I live in Malad(w)"
    return "Study in Dept CMPN"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
