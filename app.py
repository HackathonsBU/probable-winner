from flask import Flask
import os
# Flask API to Get and Post Data
app = Flask(__name__)

# Get input from url

arr = []
port_x = int(os.environ.get('PORT', 5000))
@app.route("/")
def index():
    dct = {"greeting": "Hello from our API"}
    return dct

# Get input from url
@app.route("/<name>")
def hello(name):
    dct_x = {"GreetUser": "Hello " + name}
    return dct_x

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port = port_x, host='0.0.0.0')