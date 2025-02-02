from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch




tokenizer = AutoTokenizer.from_pretrained("./model")
model = AutoModelForSequenceClassification.from_pretrained("./model")


# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu") 
model.to(device)

def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)
    # Move inputs to the same device as model
    inputs = {k: v.to(device) for k, v in inputs.items()}
    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_class = torch.argmax(logits, dim=-1).item()
    labels = ['negative', 'neutral', 'positive']
    return labels[predicted_class]