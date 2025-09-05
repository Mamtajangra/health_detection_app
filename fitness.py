import streamlit as st
st.title("Health and Fitness")

st.header("Enter the daily data")


### here minimum,maximum are just used to ignore unnecessary values and value is just only used to determine a single number appeared firstly
Height = st.number_input("Height (cm)",min_value = 100 ,max_value = 250,value = 175)
Weight = st.number_input("Weight(kg)",min_value = 30,max_value = 200,value = 75)
Sleep = st.number_input("sleep hours(last night)",min_value = 0.0,max_value = 24.0,value = 7.0)
steps = st.number_input("steps(today)",min_value = 0,max_value = 50000,value = 8000)
calorie = st.number_input("calorie(today)",min_value = 0,max_value = 10000,value = 2000)

Height_m = Height/100
bmi = Weight/(Height_m**2)

if bmi < 18.5:
  bmi_status = "Underweight"
elif 18.5 <= bmi < 24.9: 
  bmi_status = "Normal"
elif  25 <= bmi < 29.9:  
  bmi_status = "Overweight"
else:
  bmi_status = "obese"


st.header("result")
st.write("bmi:",round(bmi,2))        ## rounding off upto 2 places
st.write("bmi_status:",bmi_status)
st.write("sleep:",Sleep)    
st.write("steps:",steps)
st.write("calorie:",calorie)
