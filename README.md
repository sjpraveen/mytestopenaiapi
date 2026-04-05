# Simple OpenAI API Python Application

A lightweight Python application that demonstrates how to call OpenAI models and display results on the console.

## Description

This application uses the OpenAI Python client library to interact with OpenAI's chat completion API. It reads your API key from an environment variable and processes user queries through the model, displaying responses directly in the terminal.

## Prerequisites

- Python 3.7 or higher
- An OpenAI API key (get one at [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys))

## Installation

### Step 1: Clone or Navigate to Project Directory

```bash
cd c:\vscodeworkspace\AIWorkspace\simpleAIcall
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install the required OpenAI library.

## Setup

### Set Your OpenAI API Key

**Windows (PowerShell):**
```powershell
$env:OPENAIKEY = "your-api-key-here"
```

**Windows (Command Prompt):**
```cmd
set OPENAIKEY=your-api-key-here
```

**Linux/macOS (Terminal):**
```bash
export OPENAIKEY="your-api-key-here"
```

## How to Use

### Basic Steps

1. **Set your API key** (do this once per session):
   ```powershell
   $env:OPENAIKEY = "your-api-key-here"
   ```

2. **Run the application with your prompt**:
   ```bash
   python main.py "your prompt here"
   ```

3. **View the response** in the console

### Step-by-Step Walkthrough

1. Open your terminal/command prompt
2. Navigate to the project directory:
   ```bash
   cd c:\vscodeworkspace\AIWorkspace\mytestaiapi
   ```
3. Ensure dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```
4. Set your OpenAI API key (replace with your actual key):
   ```powershell
   $env:OPENAIKEY = "sk-xxxxxxxxxxxx"
   ```
5. Run the script with your prompt:
   ```bash
   python main.py "What is the capital of France?"
   ```
6. The application will query the model and display the result

## Usage

Run the application from the command line with your prompt:

```bash
python main.py "your prompt here"
```

### Examples

```bash
python main.py "What is the capital of France?"
python main.py "Tell me a joke about programming"
python main.py "Explain quantum computing in simple terms"
```

The application will:
1. Initialize the OpenAI client using your API key
2. Send your prompt to the model
3. Display the response on the console

### Example Output

```
==================================================
OpenAI API Call Example
==================================================
Prompt: What is the capital of France?

Response:
The capital of France is Paris. It is located in the north-central part of the country and is the most populous city in France.

==================================================
```

### Common Use Cases

**Example 1: Answer a Quick Question**
```python
prompt = "What is machine learning?"
```

**Example 2: Generate Creative Content**
```python
prompt = "Write a short poem about spring"
```

**Example 3: Code Help**
```python
prompt = "How do I read a JSON file in Python?"
```

**Example 4: Translation**
```python
prompt = "Translate 'Hello, world!' to Spanish"
```

## Customization

### Change the Prompt

Edit `main.py` and modify the `prompt` variable:

```python
prompt = "Your custom question here"
```

### Change the Model

Modify the `model` parameter in the API call:

```python
response = client.chat.completions.create(
    model="gpt-4",  # or "gpt-4o", "gpt-3.5-turbo", etc.
    messages=[...],
    ...
)
```

### Adjust Response Parameters

- `temperature` (0-2): Controls randomness. Lower = more deterministic, Higher = more creative
- `max_tokens`: Maximum length of the response

Example:
```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.5,      # More consistent responses
    max_tokens=200        # Longer responses
)
```

## Troubleshooting

### Error: "OPENAIKEY environment variable is not set"
Make sure you've set the environment variable correctly before running the script.

### Error: "Invalid API key provided"
Verify that your API key is correct and active at [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

### Error: "Rate limit exceeded"
You've hit OpenAI's rate limits. Wait a moment before running again.

## Files

- `main.py` - Main application script
- `requirements.txt` - Python dependencies
- `README.md` - This file

## License

This is a simple example project for educational purposes.
