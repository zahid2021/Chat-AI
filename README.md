# Chat-AI


This repository contains a simple Flask-based API for a chatbot using the GPT-Neo 1.3B model. The chatbot is implemented with Hugging Face's `transformers` library for natural language generation.

## Features
- Provides a REST API endpoint (`/chat`) to interact with the chatbot.
- Uses the GPT-Neo 1.3B model for text generation.
- Easy to deploy and extend.

## Requirements

- Python 3.8+
- pip (Python package manager)
- The following Python libraries:
  - Flask
  - transformers

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/flask-chatbot-api.git
   cd flask-chatbot-api
   ```

2. **Install dependencies:**
   ```bash
   pip install flask transformers
   ```

3. **Download the model:**
   The code automatically downloads the `EleutherAI/gpt-neo-1.3B` model when you first run the application. Ensure you have sufficient disk space (~5GB) and a stable internet connection.

## Usage

1. **Run the Flask application:**
   ```bash
   python app.py
   ```
   By default, the server runs on `http://127.0.0.1:5000`.

2. **Send a POST request to the `/chat` endpoint:**
   - Endpoint: `http://127.0.0.1:5000/chat`
   - Method: `POST`
   - Payload (JSON):
     ```json
     {
       "message": "Your input text here"
     }
     ```

   Example using `curl`:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello, chatbot!"}' http://127.0.0.1:5000/chat
   ```

3. **Receive the response:**
   The API will return a JSON response with the chatbot's reply. Example:
   ```json
   {
     "response": "Hello! How can I assist you today?"
   }
   ```

## Configuration

The following parameters can be adjusted in the code to fine-tune the chatbot's behavior:
- **`max_length`**: Maximum length of the generated response.
- **`num_return_sequences`**: Number of response sequences to generate.
- **`do_sample`**: Whether to sample the output (True for sampling, False for deterministic output).

## Notes

- Ensure your machine has adequate resources (e.g., GPU) for running large language models efficiently.
- The application is set to run in debug mode for development purposes. Do not use `debug=True` in a production environment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Hugging Face](https://huggingface.co/) for the `transformers` library.
- [EleutherAI](https://www.eleuther.ai/) for the GPT-Neo model.
