#GenAI
# import sys
# print(sys.executable)

# import os

# api_key = os.getenv("OPENAI_API_KEY")

# if api_key:
#     print("API key found!")
# else:
#     print("API key not found!")

from openai import OpenAI

# Create an OpenAI client
client = OpenAI()

# Send a prompt to the AI model
response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain ML in simple words with 3 real-world examples."
)

# Display the AI response
print(response.output_text)



