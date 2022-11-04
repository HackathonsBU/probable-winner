from flask import request

from flask import Flask
import os
import difflib

#Import variable df_symnp_list from prediction_module.py
from prediction_module import df_sym_list
from prediction_module import data_ripper

#Use that big list to compare user input with
the_df_symnp_list = df_sym_list()

# Flask API to Get and Post Data
app = Flask(__name__)

# Get input from url

arr = []
port_x = int(os.environ.get('PORT', 5000))
@app.route("/")
def index():
    dct = {"greeting": "Hello from Remidi API"}
    return dct

# Get input from url
@app.route("/symptom_predict/<word>")
def matching_symptoms(word):
    the_symptom_i = difflib.get_close_matches(word,the_df_symnp_list,cutoff=.30)
    return {"symptom": the_symptom_i[0]}



@app.route("/disease_predict/<d1>/<d2>/<d3>")
def matching_disease(d1,d2,d3):
    arr = [d1,d2,d3]
    dses = data_ripper(arr)
    return {"disease": dses[0]}

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port = port_x, host='0.0.0.0')