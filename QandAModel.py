import torch
from transformers import pipeline
from fastapi import FastAPI, Body
from pydantic import BaseModel

# Check if GPU is available and set the device accordingly
print(torch.cuda.is_available()) 
device = 0 if torch.cuda.is_available() else -1

# Initialize Q&A pipeline with BERT model
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad", device=device)

# Function to answer questions
def get_answer(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']
