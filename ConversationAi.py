from transformers import AutoModelForCausalLM, AutoTokenizer

# Load pre-trained DialoGPT
model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Function to generate responses
def chat_with_model(user_input, chat_history=""):
    # Tokenize input and append eos_token
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # If there's chat history, concatenate with new input for context
    bot_input_ids = tokenizer.encode(chat_history, return_tensors='pt') if chat_history else new_input_ids

    # Generate response
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Decode response
    bot_output = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    
    return bot_output
