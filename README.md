# College FAQ Chatbot

A rule-based chatbot built with spaCy and Flask to answer frequently asked questions about a college.

## Features

- **Rule-based intent matching:** Uses spaCy for natural language understanding.
- **Web interface:** Built with Flask for easy user interaction.
- **Customizable FAQ data:** Easily add or update questions and answers in `data/faq_responses.json`.
- **Responsive design:** Clean, modern chat interface with typing indicators.


## How to Run

1. **Install dependencies:**
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm

2. **Run the application:**

3. **Open your browser to `http://localhost:5000` and start chatting!**

## How to Contribute

- **Add more FAQ patterns** in `data/faq_responses.json` to improve response accuracy.
- **Report issues or suggest improvements** via GitHub Issues.
