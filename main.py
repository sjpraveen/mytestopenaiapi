import os
from openai import OpenAI

# Initialize the OpenAI client using OPENAIKEY environment variable
api_key = os.getenv('OPENAIKEY')
if not api_key:
    raise ValueError("OPENAIKEY environment variable is not set")

client = OpenAI(api_key=api_key)

# Create a simple prompt for the model
prompt = "What is the capital of France?"

print("=" * 50)
print("OpenAI API Call Example")
print("=" * 50)
print(f"Prompt: {prompt}\n")

try:
    # Call the OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=100
    )
    
    # Extract and display the result
    result = response.choices[0].message.content
    print("Response:")
    print(result)
    print("\n" + "=" * 50)
    
except Exception as e:
    print(f"Error calling OpenAI API: {e}")
