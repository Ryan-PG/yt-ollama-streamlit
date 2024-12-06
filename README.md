# Ollama Chat Examples (using streamlit)

This repository demonstrates two implementations of using the [Ollama API](https://ollama.ai/) for interacting with AI models like `qwen2.5`. The first example is a Python script, and the second example integrates with a Streamlit app for a simple web-based user interface.

## Features

- **File 1 (`ollama_client.py`)**: Demonstrates a simple script using the Ollama Python client for making API calls to interact with the `qwen2.5` model.
- **File 2 (`streamlit_app.py`)**: Implements a web-based interface using Streamlit, allowing users to input prompts and get responses from the `qwen2.5` model.

## Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed and running locally (default URL: `http://localhost:11434`)
- `pip` for installing dependencies

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Ryan-PG/yt-ollama-streamlit.git
   cd yt-ollama-streamlit
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure that the Ollama server is running locally on `http://localhost:11434`.

## Usage

### File 1: Python Script

1. Run the `ollama_client.py` script to get a response from the `qwen2.5` model:
   ```bash
   python ollama_client.py
   ```

2. The script will print the model's response to the console.

### File 2: Streamlit App

1. Start the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

2. Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Enter your prompt in the text input field and click **GO**. The response from the `qwen2.5` model will be displayed on the page.

## File Descriptions

- `ollama_client.py`: A standalone script for interacting with the Ollama API using a Python client.
- `streamlit_app.py`: A Streamlit app for creating a user-friendly interface to interact with the Ollama API.

## Requirements

Dependencies are listed in the `requirements.txt` file:
```txt
ollama
streamlit
langchain_community
```

To install them, run:
```bash
pip install -r requirements.txt
```

## Contributing

Feel free to fork this repository and submit pull requests if you'd like to improve these examples or add more features.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

