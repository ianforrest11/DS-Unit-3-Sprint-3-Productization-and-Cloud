from flask import Flask

# create flask web server
app = Flask(__name__)

# route determines location
@app.route("/")

#define function
def home():
    return "Hello Beautiful World!"

if __name__ == "__main__":
    app.run(debug=True)