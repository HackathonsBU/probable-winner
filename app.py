from flask import Flask

# Flask API to Get and Post Data
app = Flask(__name__)

# Get input from url

arr = []

@app.route("/")
def index():
    return "Hello World!"
@app.route('/<name>')
def hello(name):
    arr.append(name)
    print(arr)
    return 'Hello ' + name

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')