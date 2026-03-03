import streamlit as st
import joblib

# 1. Load the saved model
model = joblib.load('kanye_model.pkl')

# 2. Build the UI
st.title("Ye-mometer: Is it Kanye?")
st.write("Type a phrase below to see if it sounds like Kanye West.")

user_input = st.text_input("Enter phrase:")

if st.button("Predict"):
    if user_input:
        # The model predicts [1] for Kanye or [0] for Not Kanye
        prediction = model.predict([user_input])[0]
        
        if prediction == 1:
            st.success("🔥 That sounds like Kanye!")
        else:
            st.info("🤷 Probably not Kanye.")
    else:
        st.warning("Please enter some text first!")