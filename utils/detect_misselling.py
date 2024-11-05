from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("Atharva26/tiny-bert-finetuned-misselling")
model = AutoModelForSequenceClassification.from_pretrained("Atharva26/tiny-bert-finetuned-misselling")

# Define a function for inference
def classify_text(text):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt")
    
    # Run inference
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get the predicted class label
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_class = predictions.argmax(dim=-1).item()
    confidence_score = predictions.max().item()
    
    return predicted_class, confidence_score

# Example text
text = "Your example text here."

# Get the classification result
predicted_class, confidence = classify_text(text)
print(f"Predicted Class: {predicted_class}, Confidence Score: {confidence:.2f}")
