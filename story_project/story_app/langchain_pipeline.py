import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Use LLaMA 3 model from Groq
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.7,
    max_tokens=512,
    groq_api_key=GROQ_API_KEY
)

story_template = PromptTemplate(
    input_variables=["user_prompt"],
    template="""
    You are a creative writer. Based on the user prompt, respond in this exact format:

    STORY:
    <short story of 3-5 sentences>

    CHARACTER:
    <detailed description of the main character>

    BACKGROUND:
    <detailed description of the background or scene>

    User prompt: {user_prompt}
    """
)

def generate_story_parts(user_prompt):
    final_prompt = story_template.format(user_prompt=user_prompt)
    response = llm.invoke(final_prompt)  # ChatGroq uses invoke() instead of __call__()
    
    story = character = background = ""
    if "STORY:" in response.content:
        parts = response.content.split("CHARACTER:")
        story = parts[0].replace("STORY:", "").strip()

        if len(parts) > 1:
            char_and_bg = parts[1].split("BACKGROUND:")
            character = char_and_bg[0].strip()
            if len(char_and_bg) > 1:
                background = char_and_bg[1].strip()

    return story, character, background


import os
import requests

import os
import requests

# langchain_pipeline.py (or a helper module)
import os
from huggingface_hub import InferenceClient
from PIL import Image
import io

import os
import io
import google.generativeai as genai
from PIL import Image

# C:\Users\DELL\Desktop\ai_story_project\story_project\story_app\langchain_pipeline.py

# In file: C:\Users\DELL\Desktop\ai_story_project\story_project\story_app\langchain_pipeline.py

import os
import io
import google.generativeai as genai
# We MUST import this to specify the image output
# In your `langchain_pipeline.py` or a `utils.py` file

import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

# Make sure this is called to load your .env file
load_dotenv()

def generate_image_from_hf(prompt: str, filename: str) -> str:
    """
    Generates an image using the Hugging Face Inference API and saves it.

    Requirements:
      - pip install huggingface_hub pillow python-dotenv
      - An HF_TOKEN in your .env file with 'write' permissions.
    """
    hf_token = os.getenv("HF_API_TOKEN")
    if not hf_token:
        raise ValueError("HF_TOKEN not found in environment variables. Please set it in your .env file.")

    # Initialize the client.
    # It automatically uses the token from the environment variable if available.
    # If you are specifically using the Nebius provider, you would change this to:
    # client = InferenceClient(provider="nebius", token=hf_token)
    client = InferenceClient(token=hf_token)

    # The model you specified
    model_id = "black-forest-labs/FLUX.1-schnell"

    try:
        # The API call to generate the image. This returns a PIL.Image object.
        image = client.text_to_image(prompt, model=model_id)

    except Exception as e:
        # Provide a helpful error message if the API call fails
        # This can happen if the model is loading or under heavy use.
        raise Exception(f"Hugging Face image generation failed for model '{model_id}': {e}")

    # --- This file saving logic is the same as our previous functions ---

    # Ensure the object returned is a valid image
    if not hasattr(image, "save"):
        raise Exception("Hugging Face client did not return a valid PIL Image object.")

    static_dir = os.path.join("story_app", "static")
    os.makedirs(static_dir, exist_ok=True)

    # Save the image as a PNG
    image_path = os.path.join(static_dir, f"{filename}.png")
    image.save(image_path, format="PNG")

    # Return the static URL path for your Django template
    return f"/static/{filename}.png"