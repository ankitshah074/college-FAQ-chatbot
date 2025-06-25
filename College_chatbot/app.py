from flask import Flask, render_template, request, jsonify
import json
import spacy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load spaCy model
nlp = spacy.load("en_core_web_md")

# Load FAQ data
with open('data/faq_responses.json', 'r') as f:
    faq_data = json.load(f)

def get_intent(user_input):
    """Match user input to FAQ intent using spaCy"""
    user_doc = nlp(user_input.lower())
    
    # Check for keyword matches
    best_match = None
    highest_score = 0
    
    for intent, data in faq_data.items():
        if intent == "default":
            continue
            
        for pattern in data["patterns"]:
            pattern_doc = nlp(pattern.lower())
            similarity = user_doc.similarity(pattern_doc)
            
            if similarity > 0.7 and similarity > highest_score:
                highest_score = similarity
                best_match = intent
                
    return best_match or "default"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    if not user_message.strip():
        return jsonify({"response": "Please enter a valid question."})
    
    intent = get_intent(user_message)
    responses = faq_data[intent]["responses"]
    
    # Select random response
    import random
    bot_response = random.choice(responses)
    
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
