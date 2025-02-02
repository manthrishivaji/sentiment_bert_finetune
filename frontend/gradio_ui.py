import gradio as gr
import requests

# FastAPI backend URL
API_URL = "http://backend:8000/predict"


def predict(text):
    response = requests.post(API_URL, json={"text": text})
    
    if response.status_code == 200:
        result = response.json()
        return result.get("sentiment", "Error processing sentiment")
    else:
        return f"Error: {response.status_code}, {response.text}"

# Gradio UI
app = gr.Interface(fn=predict, inputs="text", outputs="text", title="Sentiment Analyzer")
app.launch(server_name="0.0.0.0", server_port=7860)  # Runs on http://127.0.0.1:7860/
