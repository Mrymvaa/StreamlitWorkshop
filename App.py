import pandas as pd 
import numpy as np 
import streamlit as st

# Set the app title 
st.title('My First Streamlit App') 
# Add a welcome message 
st.write('Welcome to my Streamlit app!') 
# Create a text input 
user_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!') 
# Display the customized message 
st.write('Customized Message:', user_input)
# Reading from a dataframe
df = pd.read_csv('/Users/ma/Desktop/App/CSV.csv')
df

#visualization:
st.bar_chart(data=df, x='College', y='Salary', color="#ffaa0099", width=0, height=0)


#calculating your BMI:
st.write("Please enter your info:")
cm = st.slider('Height:', 120,200)
meter = cm / 100
height = round(meter,2)

weight = st.slider('Weight:', 30, 150)
data = {'Height': height,
        'Weight': weight}

features = pd.DataFrame(data, index=[0])
features

BMI = weight/height**2
st.write("Your BMI is:",round(BMI,2))
