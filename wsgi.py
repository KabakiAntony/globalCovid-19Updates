from flask import render_template
from app import create_app

the_configuration = "production"
app = create_app(the_configuration)

@app.route("/")
def home():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run()