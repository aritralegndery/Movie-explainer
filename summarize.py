from transformers import BartForConditionalGeneration, BartTokenizer

# Load the pre-trained BART model and tokenizer
model_name = "facebook/bart-large-cnn"
model = BartForConditionalGeneration.from_pretrained(model_name)
tokenizer = BartTokenizer.from_pretrained(model_name)

# Define the text you want to summarize
with open('John Wick/segment_1.txt', 'r') as f:
    text = f.read()

# Tokenize the input text
inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)

# Generate the summary with increased length
summary_ids = model.generate(inputs, max_length=800, min_length=600, length_penalty=2.0, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Print the summary
print(summary)
