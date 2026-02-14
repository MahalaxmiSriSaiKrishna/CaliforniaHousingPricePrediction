import streamlit as st
import pandas as pd
import joblib as jb

##Loding Model
model = jb.load('model.pkl')
st.title('House Price Prediction')
st.write('Enter the details of the house to predict the price')

##User Input
st.sidebar.header("Enter House Details")

MedInc = st.sidebar.number_input("Median Income",min_value=0.5, max_value=15.0,value=3.5, step=0.1)
HouseAge = st.sidebar.number_input("House Age",min_value=1, max_value=52,value=29, step=1)
AveRooms = st.sidebar.number_input("Average Rooms",min_value=1.0, max_value=15.0,value=5.2, step=0.1)
AveBedrms = st.sidebar.number_input("Average Bedrooms",min_value=0.5, max_value=5.0,value=1.0, step=0.1)
Population = st.sidebar.number_input("Population",min_value=0, max_value=35000,value=100, step=100)
AveOccup = st.sidebar.number_input("Average Occupancy",min_value=1.0, max_value=10.0,value=2.8, step=0.1)
Latitude = st.sidebar.number_input("Latitude",min_value=32.5,max_value=42.0,value=34.2,step=0.01)
Longitude = st.sidebar.number_input("Longitude",min_value=-124.5,max_value=-114.0,value=-118.5,step=0.01)

if(st.button('Predict')):
    input_data = pd.DataFrame([[MedInc,HouseAge,AveRooms,AveBedrms,Population,AveOccup,Latitude,Longitude]],
                  columns=['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude'])
    prediction = model.predict(input_data)
    st.success(f'The predicted price of the house is {prediction[0]:,.2f}')



