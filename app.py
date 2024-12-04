import pickle
import streamlit as st

# Modelni yuklash
with open('model.pkl', 'rb') as LrdetectFile:
    Lrdetect_Model = pickle.load(LrdetectFile)

# Streamlit interfeysi
st.title("Tilni aniqlovchi dastur")
input_test = st.text_input("Bu yerg text kiriting", 'Hello')

button_clicked = st.button("Get Language Name")
if button_clicked:
    # Predict natijasini chiqarish
    st.write(Lrdetect_Model.predict([input_test]))

