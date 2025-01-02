import requests

# data = {
#     "input_type": "chat",
#     "input_text": "Hey?",
# }

# response = requests.post("http://localhost:8000/interact", json=data)
# print(response.json())

data = {
    "input_type": "qa",
    "input_text": "Should I go to a party?",
    "context": "I was invited to a party but have too much work left. I went anyway, and now I regret wasting my time. My question is whether I made the right decision."
}

response = requests.post("http://localhost:8000/interact", json=data)
print(response.json())  # This will print the answer to the question.