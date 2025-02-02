from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from dotenv import load_dotenv
import os


load_dotenv()

# # Check if the Hugging Face Hub API token is set
# HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
# if not HUGGINGFACEHUB_API_TOKEN:
#     raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in .env file.")
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGI_FACEHUB_API_TOKEN")

# Load model and tokenizer from huggingface
model_name = "Wolverine001/bert_finetuned_senti"

tokenizer = AutoTokenizer.from_pretrained(model_name,token=HUGGINGFACEHUB_API_TOKEN)
model = AutoModelForSequenceClassification.from_pretrained(model_name,token=HUGGINGFACEHUB_API_TOKEN)


# Save model and tokenizer
model.save_pretrained("./model")
tokenizer.save_pretrained("./model")