from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "You just set a server as well."

@app.route("/tony")
def tony():
	return "Developer Tony"
    
if __name__ == "__main__":
    app.run(debug=True)