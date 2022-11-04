from flask import Flask
import os
import difflib

#Import variable df_symnp_list from prediction_module.py
from prediction_module import df_symnp_list

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
@app.route("/<sentence>")
def hello(name):
    the_symptoms = difflib.get_close_matches('',df_symp_list,cutoff=.30)
    return the_symptoms

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port = port_x, host='0.0.0.0')