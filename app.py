import streamlit as st
import joblib

# 1. Load the saved model
model = joblib.load('kanye_model.pkl')


st.title("Ye-mometer: Is it Kanye?")
col1, col2 = st.columns([1,2])

with col1:
    st.image("ye_photo.jpeg", caption="The Ye-mometer V1.0", width=200)

with col2:
    st.write("From 'College Dropout' to 'Vultures,' Kanye West has one of the most distinct vocabularies in music history. This project uses Natural Language Processing (NLP) to analyze linguistic patterns—like his specific use of pronouns, religious imagery, and capitalization—to determine if a phrase was born from the mind of Ye or somewhere else entirely.")
    st.write("This classifier was built using a Multinomial Naive Bayes model. It works by calculating the 'weighted importance' of words using TF-IDF (Term Frequency-Inverse Document Frequency). Essentially, the model ignores common 'filler' words and focuses on the high-impact terms that make a sentence uniquely 'Kanye-esque.")
st.divider()
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