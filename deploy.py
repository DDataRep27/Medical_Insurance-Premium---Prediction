#ML-App for Premium Charges Prediction - Medical Insurance!!

#A health insurance premium calculator is an online tool that helps a potential health insurance buyer to get an estimate of the 
#premium amount that he/she will be required to pay for a particular health insurance plan. With the rising medical expenses, 
#calculating the premium becomes important.

#Import Libraries
import pandas as pd
import streamlit as st 
from pickle import load 
from PIL import Image
import time
from streamlit_lottie import st_lottie_spinner
import json

#Web Page Configuration
st.set_page_config(page_title=("DR Health Insurance"))

#Background config
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
    
lottie_start = load_lottiefile("1631-healthtap-spinner.json")
lottie_type  = load_lottiefile("55867-congratulation.json")
lottie_process = load_lottiefile("106399-be-healthy.json")


#Web-page image
img = Image.open("health-insurance-premium-calculator.jpeg")
st.image(img)


#Button Values
db = {0: 'No ❌', 1: 'Yes 💉'}
bp = {0: 'No ❌', 1: 'Yes 🌡'} 
at = {0: 'No ❌', 1: 'Yes 🏥'}
ac = {0: 'No ❌', 1: 'Yes 🤒'}
ak = {0: 'No ❌', 1: 'Yes 🦠'}
hc = {0: 'No ❌', 1: 'Yes 🎗'}

 
#Input variables 
def user_input_features():
    tab1, tab2, tab3, tab4, tab5 = st.tabs(['Personal Details', '         ', 'Health Status', '         ', 'Premium Calculator'])

    with tab1:
        st.subheader("Enter your details")
        col1, col2 = st.columns(2, gap=("medium"))
    with col1:
        sex = st.selectbox("Select your Gender", ['Female  👩🏻', 'Male  👨🏻'])
    with col2:
        age = st.number_input(label="Please Enter your Age", max_value=100, min_value=18, step=1, format='%i')   
       
    with tab3:
        st.subheader("Be Honest with your Health Status")
        col1, col2 = st.columns(2, gap=("large"))
        
    with col1:    
        smoke = st.selectbox("Do you Smoke?", ['No  🚭', 'Yes 🚬'])
    
    with col2:
        diab  = st.selectbox("Do you have Diabetes?", options=db.keys(), format_func=(lambda x: '{}'.format(db.get(x)) ))
    
    with col1:
        BP    = st.selectbox("Do you have Blood Pressure Problem?", options=bp.keys(), format_func=(lambda x: '{}'.format(bp.get(x)) ))
    
    with col2:
        ATP   = st.selectbox("Did you had Any Transplant?", options=at.keys(), format_func=(lambda x: '{}'.format(at.get(x)) ))
    
    with col1:
        ACD   = st.selectbox("Any Chronic Disease?", options=ac.keys(), format_func=(lambda x: '{}'.format(ac.get(x)) ))
    
    with col2:
        KAL   = st.selectbox("Any Allergy?", options=ak.keys(), format_func=(lambda x: '{}'.format(ak.get(x)) ))
    
    with col1:
        HCF   = st.selectbox("Do you have a past history of Cancer in family?", options=hc.keys(), format_func=(lambda x: '{}'.format(hc.get(x)) ))
    
    with col2:
        NOM   = st.slider("How many major Surgeries you had in past?", min_value=0, max_value=5, step=1)

       
    new = {'Sex': sex,
           'Age': age, 
           'Smoker': smoke, 
           'Diabetes': diab,
           'BloodPressure_Problems': BP, 
           'Any_Transplants': ATP, 
           'Any_ChronicDiseases': ACD, 
           'Known_Allergies': KAL,
           'HistoryOfCancerInFamily': HCF,
           'NumberOfMajorSurgeries': NOM}
           
    features = pd.DataFrame(new, index=[0])
    
    features = features.rename(index={0:'Details'})
    
    with tab5:
        st.subheader("Calculating the Premium based on your details")
        st.write('Below mentioned are your details: ')
        st.table(features)
        
        #Loading the model
        model = load(open('Medprem_intelligence.pkl', 'rb'))
        
        #Predicting the model
        ml = model.predict(features).round()
        
        if st.button('Predict'):
            with st_lottie_spinner(lottie_process, height=(200), width=(300), quality="high", speed=1):
                time.sleep(4)
            st.write("**Result:**")           
            st.warning(f"Your Monthly Premium Charges is ₹{(ml[0]*0.85)/12:,.1f} (inclusive of tax & charges)")
            
            
            with st.expander(label="Would like to go for Annual Premium?"):
                with st_lottie_spinner(lottie_type, height=(200), width=(400), quality="high", speed=1):
                    time.sleep(4.2)
                st.success(f"You save ₹{(ml[0]*0.85)*0.035:,.1f}  😃", icon=("🎉"))
                st.metric(label="Annual Premium Charges  (inclusive of tax & charges)", value = f" ₹{(ml[0]*0.85)*0.965:,.1f}")
           
              
    return 


#Running the function
df = user_input_features()


if __name__=='__user_input_features__':
    user_input_features()

