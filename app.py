import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

LrdetectFile = open('model.pkl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title("Tilni aniqlovchi dastur")
input_test = st.text_input("Bu yerg text kiriting", 'Hello my name is Jamila ')

button_clicked = st.button("Get Language Name")
if button_clicked:
	st.text(Lrdetect_Model.predict([input_test]))
