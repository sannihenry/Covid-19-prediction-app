# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 03:32:31 2021

@author: Sanni Henry
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 03:32:31 2021

@author: Sanni Henry
"""



import streamlit as st
from PIL import Image
image = Image.open('440px-3D_Medical_Animation_Spleen_Anatomy.jpg')
st.image(image, caption='Spleen analysis')

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Volume,Volume_indexed,T1_ms,T2_ms,T0_relaxation_rate,Tg_relaxation_rate,Transverse_magnetization,Gender):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Volume
        in: query
        type: number
        required: true
      - name: Volume_indexed
        in: query
        type: number
        required: true
      - name: T1_ms
        in: query
        type: number
        required: true
      - name: T2_ms
        in: query
        type: number
        required: true
      - name: T0_ralaxation_rate
        in: query
        type: number
        required: true
      - name: Tg_ralaxation_rate
        in: query
        type: number
        required: true
      - name: Transverse_magnetization
        in: query
        type: number
        required: true
      - name: Gender
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[Volume,Volume_indexed,T1_ms,T2_ms,T0_relaxation_rate,Tg_relaxation_rate,Transverse_magnetization,Gender]])
    print(prediction)
    return prediction



def main():
    st.title("COVID 19 Prediction Software")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Check your COVID 19 status today </h2>
    </div>

    <div style="background-color:tomato;padding:10px">
    <h3 style="color:yellow;text-align:left;">Result: </h3>
    </div>    

    <div style="background-color:tomato;padding:5px">
    <h4 style="color:yellow;text-align:left;">1-You have COVID 19 </h4>
    </div>    

    <div style="background-color:tomato;padding:5px">
    <h5 style="color:yellow;text-align:left;">0-You are free from the VIRUS </h5>
    </div>    
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Volume = st.text_input("Volume","Type Here")
    Volume_indexed = st.text_input("Volume_indexed","Type Here")
    T1_ms = st.text_input("T1_ms","Type Here")
    T2_ms = st.text_input("T2_ms","Type Here")
    T0_relaxation_rate = st.text_input("T0_relaxation_rate","Type Here")
    Tg_relaxation_rate = st.text_input("Tg_relaxation_rate","Type Here")
    Transverse_magnetization = st.text_input("Transverse_magnetization","Type Here")
    Gender = st.text_input("Gender","input (1) for male and (0) for female")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Volume,Volume_indexed,T1_ms,T2_ms,T0_relaxation_rate,Tg_relaxation_rate,Transverse_magnetization,Gender)
    st.success('Your COVID 19 Chances {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built by Henry")

if __name__=='__main__':
    main()
    
    
    