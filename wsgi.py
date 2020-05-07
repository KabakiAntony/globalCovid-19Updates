from app import create_app

app = create_app()

@app.route("/")
def home():
    return "Hello, this will be the root of our api"
    
if __name__ == "__main__":
    app.run()