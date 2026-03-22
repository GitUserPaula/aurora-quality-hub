from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("--- Listing available models for your key ---")
try:
    # Simplemente listamos los nombres de los modelos
    models = client.models.list()
    for m in models:
        print(f"Model Name: {m.name}")
except Exception as e:
    print(f"Error connecting: {e}")