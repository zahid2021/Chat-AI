from flask import Flask, request, jsonify
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

# Initialize the model and tokenizer
MODEL_NAME = "EleutherAI/gpt-neo-1.3B"  
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

# Create a conversational pipeline
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Flask app setup
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")
    
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Generate a response
    response = chatbot(user_input, max_length=200, num_return_sequences=1, do_sample=True)
    return jsonify({"response": response[0]["generated_text"]})

if __name__ == "__main__":
    app.run(debug=True)
