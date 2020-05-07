from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this will be the root of our api"
    
if __name__ == "__main__":
    app.run(debug=True)