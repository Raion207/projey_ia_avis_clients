import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

st.title("Application d'analyse de sentiments des avis clients avec FastAPI et Streamlit")

st.header("Entraînement du modèle d'analyse de sentiments")
uploaded_file = st.file_uploader("Choisir un fichier CSV", type="csv")

if uploaded_file is not None:
    st.write("## Fichier CSV téléchargé :")
    df = pd.read_csv(uploaded_file)
    st.write(df)

    if st.button("Envoyer pour entraînement"):
        try:
            file_content = uploaded_file.getvalue()
            
            files = {'file': (uploaded_file.name, file_content, 'text/csv')}
            response = requests.post(f"{API_URL}/train", files=files)
            
            if response.status_code == 200:
                st.success("Le fichier CSV a été traité et validé avec succès !")
                st.json(response.json())
            else:
                st.error(f"Erreur : {response.status_code}")
                st.json(response.json())
        except Exception as e:
            st.error(f"Une erreur s'est produite : {e}")

st.header("Prédiction des sentiments des avis clients")
prediction_message = st.text_area("Classifier un avis client", "Le produit est génial !")

if st.button("Prédire"):
    predict_data = {
        "message": prediction_message
    }
    response = requests.post(f"{API_URL}/predict", json=predict_data)
    if response.status_code == 200:
        st.success(f"Prédictions : {response.json()['prediction']}")
    else:
        st.error(response.json()["detail"])
