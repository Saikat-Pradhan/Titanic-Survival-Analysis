import streamlit as st
import pickle as pkl

# Load the model
with open('titanic_model.pkl', 'rb') as f:
    model = pkl.load(f)

with open('age_scaler.pkl', 'rb') as f:
    scaler = pkl.load(f)

# Set up the Streamlit app    
st.title('Titanic Survival Prediction')
# Create input fields for user to enter data
# Passenger Class
pclass = st.selectbox('Passenger Class', ['1st', '2nd', '3rd'])
if pclass == '1st':
    pclass = 1
elif pclass == '2nd':
    pclass = 2
else:
    pclass = 3
    
# Sex    
sex = st.selectbox('Sex', ['male', 'female'])
if sex == 'male':
    sex = 0
else:
    sex = 1
    
# Age
age = st.number_input('Age', min_value=0, max_value=100, value=25)
age = scaler.transform([[age]])[0][0]  # Scale the age input
    
# SibSp (Number of siblings/spouses aboard)
sibsp = st.number_input('Number of Siblings/Spouses Aboard', min_value=0, max_value=10, value=0)

# Parch (Number of parents/children aboard)
parch = st.number_input('Number of Parents/Children Aboard', min_value=0, max_value=10, value=0)

# Embarked (Port of embarkation)
embarked = st.selectbox('Port of Embarkation', ['Cherbourg', 'Queenstown', 'Southampton'])
if embarked == 'Cherbourg':
    embarked = 1
elif embarked == 'Queenstown':
    embarked = 2
else:
    embarked = 3
    
# Preform the prediction when the user clicks the button    
if st.button('Predict'):
    # Create a feature array for the model
    features = [pclass, sex, age, sibsp, parch, embarked]
    # Make the prediction
    prediction = model.predict([features])
    # Display the prediction
    if prediction[0] == 1:
        st.success('The passenger is predicted to survive.')
    else:
        st.warning('The passenger is predicted to not survive.')