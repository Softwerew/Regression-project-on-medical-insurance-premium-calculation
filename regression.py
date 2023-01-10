#import libraries
import pandas as pd
import streamlit as st 
from pickle import load 

#load the model from disk
import joblib
model = joblib.load(r"finalized_model-sav")

def main():

#title
	st.title('Medical Insurance Premium Calculation app')

#input variables
	sex = st.selectbox('Select your Gender', ['Female', 'Male'])
	age=st.number_input(label='Enter your age',max_value=100, min_value=18, step=1, format='%i')
	children=st.number_input(label='No. of Children', max_value=10, min_value=0, step=1)
	diabetes=st.selectbox('Are you diabetic?',['Yes','No'])
	BP=st.selectbox('Are you suffering from Blood Pressure?',['Yes','No'])
	ATP=st.selectbox('Have you had any transplants?',['Yes','No'])
	ACD=st.selectbox('Are you suffering from any chronic desease?',['Yes','No'])
	Allergies=st.selectbox('Do you have any known allergies?',['Yes','No'])
	HCF=st.selectbox('Any history of Cancer in family?',['Yes','No'])
	NMS=st.selectbox('Any Major surgery?',['Yes','No'])
	
	sex= 1 if sex=="Female" else 0;
	diabetes =  1 if diabetes == "Yes" else 0;
	BP =  1 if BP == "Yes" else 0;
	ATP =  1 if ATP == "Yes" else 0;
	ACD =  1 if ACD == "Yes" else 0;
	Allergies =  1 if Allergies == "Yes" else 0;
	HCF =  1 if HCF == "Yes" else 0;
	NMS =  1 if NMS == "Yes" else 0;

	input_data=pd.DataFrame([{'Sex_0':sex,
		'Age': age,
		'Children': children,
		'Diabetes': diabetes,
		'BloodPressure_Problems': BP,
		'Any_Transplants': ATP,
		'Any_ChronicDiseases': ACD,
		'Known_Allergies': Allergies,
		'HistoryOfCancerInFamily': HCF,
		'NumberOfMajorSurgeries': NMS}])
	
	from sklearn.preprocessing import StandardScaler
    
	#predicting the model

	if 	st.button('Predict'):
		predicted_output=model.predict(input_data)
		st.write(predicted_output)
		
		
if __name__ == '__main__':
        main()
		


				
		