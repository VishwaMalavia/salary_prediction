import streamlit as st
import pickle
model=pickle.load(open('model.pkl','rb'))
st.title("Salary Prediction App")
exp=st.number_input("Years of Experience",min_value=0.0,step=0.1)
if st.button("Predict Salary"):
    result=model.predict([[exp]])
    st.write(f"Predicted Salary: {result[0]:.2f}")
    
