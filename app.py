from flask import request

from flask import Flask
import os
import difflib
import pandas as pd
#Import variable df_symnp_list from prediction_module.py
from prediction_module import df_sym_list
from prediction_module import data_ripper

#Use that big list to compare user input with


the_symp_to_predict_from = ["itching","skin_rash", "skin_rashes", "nodal_skin_eruptions","vomiting", "dehydration", "diarrhoea", "vomiting", "breathlessness", "sweating", "blackheads", "scurring", "fainting", "fainting"]

# Flask API to Get and Post Data
app = Flask(__name__)

# Get input from url
trained_mdl = data_ripper()

arr = []
port_x = int(os.environ.get('PORT', 5000))
@app.route("/")
def index():
    dct = {"greeting": "Hello from Remidi API"}
    return dct

# Get input from url
@app.route("/symptom_predict/<word>")
def matching_symptoms(word):
    the_symptom_i = difflib.get_close_matches(word,the_symp_to_predict_from,cutoff=.30)
    return {"symptom": the_symptom_i[0]}



@app.route("/disease_predict/<d1>/<d2>/<d3>")
def matching_disease(d1,d2,d3):
    inp_arr = [d1,d2,d3]

    the_df_symnp_list = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'dischromic _patches', 'continuous_sneezing',
                         'shivering', 'chills', 'watering_from_eyes', 'stomach_pain',
                         'acidity', 'ulcers_on_tongue', 'vomiting', 'cough', 'chest_pain', 'yellowish_skin', 'nausea',
                         'loss_of_appetite', 'abdominal_pain', 'yellowing_of_eyes',
                         'burning_micturition', 'spotting_ urination', 'passage_of_gases', 'internal_itching',
                         'indigestion',
                         'muscle_wasting', 'patches_in_throat', 'high_fever',
                         'extra_marital_contacts', 'fatigue', 'weight_loss', 'restlessness', 'lethargy',
                         'irregular_sugar_level',
                         'blurred_and_distorted_vision', 'obesity',
                         'excessive_hunger', 'increased_appetite', 'polyuria', 'sunken_eyes', 'dehydration',
                         'diarrhoea',
                         'breathlessness', 'family_history', 'mucoid_sputum',
                         'headache', 'dizziness', 'loss_of_balance', 'lack_of_concentration', 'stiff_neck',
                         'depression',
                         'irritability', 'visual_disturbances', 'back_pain',
                         'weakness_in_limbs', 'neck_pain', 'weakness_of_one_body_side', 'altered_sensorium',
                         'dark_urine',
                         'sweating', 'muscle_pain', 'mild_fever', 'swelled_lymph_nodes',
                         'malaise', 'red_spots_over_body', 'joint_pain', 'pain_behind_the_eyes', 'constipation',
                         'toxic_look_(typhos)', 'belly_pain', 'yellow_urine', 'receiving_blood_transfusion',
                         'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'acute_liver_failure',
                         'swelling_of_stomach', 'distention_of_abdomen', 'history_of_alcohol_consumption',
                         'fluid_overload', 'phlegm', 'blood_in_sputum', 'throat_irritation', 'redness_of_eyes',
                         'sinus_pressure',
                         'runny_nose', 'congestion', 'loss_of_smell', 'fast_heart_rate',
                         'rusty_sputum', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
                         'irritation_in_anus', 'cramps', 'bruising', 'swollen_legs', 'swollen_blood_vessels',
                         'prominent_veins_on_calf', 'weight_gain', 'cold_hands_and_feets', 'mood_swings',
                         'puffy_face_and_eyes',
                         'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
                         'abnormal_menstruation', 'muscle_weakness', 'anxiety', 'slurred_speech', 'palpitations',
                         'drying_and_tingling_lips', 'knee_pain', 'hip_joint_pain', 'swelling_joints',
                         'painful_walking', 'movement_stiffness', 'spinning_movements', 'unsteadiness',
                         'pus_filled_pimples',
                         'blackheads', 'scurring', 'bladder_discomfort', 'foul_smell_of urine',
                         'continuous_feel_of_urine', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
                         'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']

    for i in range(131):
        if the_df_symnp_list[i] in inp_arr:
            the_df_symnp_list[i] = 1;
        else:
            the_df_symnp_list[i] = 0;

    df_t = pd.DataFrame([the_df_symnp_list])

    df_pd = trained_mdl.predict(df_t)


    return {"disease": df_pd[0]}



# Run the app
if __name__ == '__main__':
    app.run(debug=True, port = port_x, host='0.0.0.0')