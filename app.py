from flask import Flask

# Flask API to Get and Post Data
app = Flask(__name__)

# Get input from url
@app.route('/<name>')
def hello(name):
    return 'Hello ' + name

# Run the app
if __name__ == '__main__':
    app.run(debug=True)