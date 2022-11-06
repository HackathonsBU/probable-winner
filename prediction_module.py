import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import difflib
import os
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import warnings

warnings.simplefilter("ignore")

df_symp_list = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'dischromic _patches', 'continuous_sneezing',
                'shivering', 'chills', 'watering_from_eyes', 'stomach_pain',
                'acidity', 'ulcers_on_tongue', 'vomiting', 'cough', 'chest_pain', 'yellowish_skin', 'nausea',
                'loss_of_appetite', 'abdominal_pain', 'yellowing_of_eyes',
                'burning_micturition', 'spotting_ urination', 'passage_of_gases', 'internal_itching', 'indigestion',
                'muscle_wasting', 'patches_in_throat', 'high_fever',
                'extra_marital_contacts', 'fatigue', 'weight_loss', 'restlessness', 'lethargy', 'irregular_sugar_level',
                'blurred_and_distorted_vision', 'obesity',
                'excessive_hunger', 'increased_appetite', 'polyuria', 'sunken_eyes', 'dehydration', 'diarrhoea',
                'breathlessness', 'family_history', 'mucoid_sputum',
                'headache', 'dizziness', 'loss_of_balance', 'lack_of_concentration', 'stiff_neck', 'depression',
                'irritability', 'visual_disturbances', 'back_pain',
                'weakness_in_limbs', 'neck_pain', 'weakness_of_one_body_side', 'altered_sensorium', 'dark_urine',
                'sweating', 'muscle_pain', 'mild_fever', 'swelled_lymph_nodes',
                'malaise', 'red_spots_over_body', 'joint_pain', 'pain_behind_the_eyes', 'constipation',
                'toxic_look_(typhos)', 'belly_pain', 'yellow_urine', 'receiving_blood_transfusion',
                'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'acute_liver_failure',
                'swelling_of_stomach', 'distention_of_abdomen', 'history_of_alcohol_consumption',
                'fluid_overload', 'phlegm', 'blood_in_sputum', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure',
                'runny_nose', 'congestion', 'loss_of_smell', 'fast_heart_rate',
                'rusty_sputum', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool',
                'irritation_in_anus', 'cramps', 'bruising', 'swollen_legs', 'swollen_blood_vessels',
                'prominent_veins_on_calf', 'weight_gain', 'cold_hands_and_feets', 'mood_swings', 'puffy_face_and_eyes',
                'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties',
                'abnormal_menstruation', 'muscle_weakness', 'anxiety', 'slurred_speech', 'palpitations',
                'drying_and_tingling_lips', 'knee_pain', 'hip_joint_pain', 'swelling_joints',
                'painful_walking', 'movement_stiffness', 'spinning_movements', 'unsteadiness', 'pus_filled_pimples',
                'blackheads', 'scurring', 'bladder_discomfort', 'foul_smell_of urine',
                'continuous_feel_of_urine', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails',
                'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']




#Start of prediction function

def data_ripper():
    df = pd.read_csv("Warehouse_Data/dataset.csv")

    df.head()

    df["Symptoms"] = 0

    records = df.shape[0]
    for i in range(records):
        values = df.iloc[i].values
        values = values.tolist()
        if 0 in values:
            df["Symptoms"][i] = values[1:values.index(0)]
        else:
            df["Symptoms"][i] = values[1:]

    df.head()
    column_values = df[['Symptom_1', 'Symptom_2', 'Symptom_3', 'Symptom_4',
           'Symptom_5', 'Symptom_6', 'Symptom_7', 'Symptom_8', 'Symptom_9',
           'Symptom_10', 'Symptom_11', 'Symptom_12', 'Symptom_13', 'Symptom_14',
           'Symptom_15', 'Symptom_16', 'Symptom_17']].values.ravel()

    symps = pd.unique(column_values)
    symps = symps.tolist()
    symps = [i for i in symps if str(i) != "nan"]

    symptoms = pd.DataFrame(columns = symps,index = df.index)
    symptoms["Symptoms"] = df["Symptoms"]
    for i in symps:
        symptoms[i] = symptoms.apply(lambda x:1 if i in x.Symptoms else 0, axis=1)

    symptoms["Disease"] = df["Disease"]
    symptoms = symptoms.drop("Symptoms",axis=1)

    train, test = train_test_split(symptoms,test_size=0.2)
    X_train = train.drop("Disease",axis=1)
    y_train = train["Disease"].copy()
    # X_test = test.drop("Disease",axis=1)
    # y_test = test["Disease"].copy()

    rnd_forest = RandomForestClassifier()
    rnd_forest.fit(X_train,y_train)
    return rnd_forest

#To create the df_symp_list
    # df_symnp_list = symptoms.columns.drop("Disease")
    # df_symnp_list = list(df_symnp_list)
    # for i in range(131):
    #     df_symnp_list[i] = df_symnp_list[i].strip()

def predict_med(dis):
    import pandas as pd
    import warnings

    warnings.simplefilter("ignore")
    df = pd.read_csv("Warehouse_Data/dataset.csv")
    disease = df["Disease"].unique()
    disease_meds = {"Disease": disease}
    disease_meds = pd.DataFrame(disease_meds)
    disease_meds
    medicines = ["clotrimazole", "Cetirizine", "esomeprazole", "ursodiol", "Benadryl", "omeprazole",
                 "You Have To Consult Doctor", "Fortamet", "ondansetron", "A MED 10", "A MED 11", "A MED 12", "A MED 13",
                 "A MED 14", "A MED 15", "A MED 16", "A MED 17", "A MED 18", "A MED 19", "A MED 20", "A MED 21",
                 "A MED 22", "A MED 23", "A MED 24", "A MED 25", "A MED 26", "A MED 27", "A MED 28", "A MED 29",
                 "Aspirin", "A MED 31", "A MED 32", "A MED 34", "A MED 35", "A MED 36", "A MED 37", "A MED 38",
                 "Benzoyl peroxide", "A MED 40", "A MED 41", "A MED 42"]
    disease_meds["Medicine"] = medicines
    return disease_meds[disease_meds["Disease"] == dis]["Medicine"].item()
def df_sym_list():
    return df_symp_list