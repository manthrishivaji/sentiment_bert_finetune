
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir torch==2.1.0+cpu  -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install --no-cache-dir huggingface_hub

# Copy the pre-downloaded model
COPY ./model /app/model

# Copy the application code
COPY . .

EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]