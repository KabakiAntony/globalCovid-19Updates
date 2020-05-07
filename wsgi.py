from app import create_app

the_configuration = "production"
app = create_app(the_configuration)

@app.route("/")
def home():
    return "Hello, this will be the root of our api"
    
if __name__ == "__main__":
    app.run()