# Sentiment Analysis App 🚀

## Overview

This project is a Sentiment Analysis Web App that consists of:

- A FastAPI Backend that processes text input and predicts sentiment.

- A Gradio Frontend for a user-friendly interface.

- Dockerized Deployment using docker-compose.



## Features

- ✅ Sentiment analysis (Positive/Negative/Neutral).
- ✅ REST API with FastAPI.
- ✅ Interactive UI with Gradio.
- ✅ Fully containerized using Docker.
<!-- ✅ Cloud deployment-ready. -->

### Note : I did fine tune on notebook and pushed to HF-hub.For project I downloaded the model from hub.

- Clone the repo
- Install required libraries in respective backend and frontend folders
- Go to backend folder file named "model.py" and run it it will create a folder "model" and save the model init.
- To verify if everything is working fine , in frontend/gradio.py for api_url modify it accordingly.Dont use backend:predict/ it wont work, use 127.0.0.1/predict or acoordingly.
