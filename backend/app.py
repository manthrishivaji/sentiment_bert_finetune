from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from main import predict_sentiment

app = FastAPI()

# Enable CORS for all origins or specify the allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, or you can specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text:str

@app.post("/predict")
def predict_api(input: TextInput):
    sentiment = predict_sentiment(input.text)
    return {"sentiment": sentiment}

@app.get("/")
async def root():
    return {"message": "Welcome to Sentiment Analysis."}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)