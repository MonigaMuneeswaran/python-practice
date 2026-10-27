# GEN AI
from openai import OpenAI
client = OpenAI()
response = client.responses.create(
    model='gpt-4.1-mini',
    input="Explain Gen AI and its applications"
)

