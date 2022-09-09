import streamlit as st
import numpy as np
import pandas as pd
import pickle
with open('co2_model.pkl', 'rb') as file:
    model=pickle.load(file)




st.title("CO2 emission prediction")
st.write(""" ##### Please input the parameters for the car """)


ENGINESIZE=st.number_input('Engine Size', format='%f')
CYLINDERS=st.number_input("Number of Cylinders", format='%f')

fcc=st.number_input("Fuel Consumption in City, (L/100 km)", format='%f')
fch=st.number_input("Fuel Consumption in Highway, (L/100 km)", format='%f')

df=pd.DataFrame({'ENGINESIZE':[ENGINESIZE],'CYLINDERS':[CYLINDERS],'FUELCONSUMPTION_CITY':[fcc], 'FUELCONSUMPTION_HWY':[fch]})
if st.button('Calculate'):
    pre=model.predict(df)
    st.subheader('The predicted amount of CO2 emission is %.2f g/km' % (pre[0][0]))




