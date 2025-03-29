import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Print all environment variables
print("OPENAI_API_KEY:", os.getenv('OPENAI_API_KEY'))
print("ANTHROPIC_API_KEY:", os.getenv('ANTHROPIC_API_KEY'))
print("AZURE_ENDPOINT:", os.getenv('AZURE_ENDPOINT'))
print("AZURE_OPENAI_API_KEY:", os.getenv('AZURE_OPENAI_API_KEY'))
print("GEMINI_API_KEY:", os.getenv('GEMINI_API_KEY'))
print("DEEPSEEK_API_KEY:", os.getenv('DEEPSEEK_API_KEY'))