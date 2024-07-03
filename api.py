import numpy as np
import joblib
import pandas as pd
import os
from fastapi import FastAPI, HTTPException, UploadFile, File
from functions import clean
from pydantic import BaseModel, Field
from io import StringIO
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

app = FastAPI(
    title="API d'analyse de sentiments des avis clients",
    description="API d'analyse de sentiments avec FastAPI pour analyser les avis clients",
    version="0.1.0",
)

model_path = "sentiment_model.joblib"

class TrainData(BaseModel):
    review: str = Field(..., description="L'avis client à analyser")
    sentiment: str = Field(..., description="Le sentiment associé (positive, negative, neutral)")

class PredictData(BaseModel):
    message: str = Field(..., example="Le produit est génial !")

pipeline = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

@app.post("/train", summary="Entraîner le modèle", description="Entraîner le modèle d'analyse de sentiments avec les données d'entraînement.")
async def train(file: UploadFile = File(...)):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Le format du fichier est invalide. Veuillez fournir un fichier CSV.")
    
    try:
        content = await file.read()
        decoded_content = content.decode("utf-8")
        data = pd.read_csv(StringIO(decoded_content))

        if 'review' not in data.columns or 'sentiment' not in data.columns:
            raise HTTPException(status_code=400, detail="Le fichier CSV doit contenir les colonnes 'review' et 'sentiment'.")

        if data.isnull().values.any():
            raise HTTPException(status_code=400, detail="Le fichier CSV contient des valeurs manquantes.")
        
        data["review"] = data["review"].apply(clean)

        X = data["review"]
        y = data["sentiment"]

        pipeline.fit(X, y)

        joblib.dump(pipeline, model_path)
        
        return {
            "status": "success",
            "message": "Modèle entraîné avec succès.",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing and training the file: {e}")

@app.post("/predict", summary="Prédire", description="Prédire le sentiment d'un avis client.")
async def predict(data: PredictData):
    try:
        model = joblib.load(model_path)
        cleaned_message = clean(data.message)
        prediction = model.predict([cleaned_message])[0]

        return {
            "status": "success",
            "prediction": prediction
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la prédiction : {str(e)}")
