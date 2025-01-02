import torch
from transformers import pipeline
from fastapi import FastAPI, Body
from pydantic import BaseModel

# Check if GPU is available and set the device accordingly
print(torch.cuda.is_available()) 
device = 0 if torch.cuda.is_available() else -1