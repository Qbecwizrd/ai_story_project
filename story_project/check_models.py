import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from your .env file
load_dotenv()

print("--- Running Google AI Diagnostic Script ---")

# 1. Check for the API Key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("\nERROR: GOOGLE_API_KEY was not found in your .env file. Please check it.")
    exit()
else:
    print("\nSuccessfully loaded GOOGLE_API_KEY.")
    try:
        genai.configure(api_key=api_key)
    except Exception as e:
        print(f"ERROR: Failed to configure the SDK. Error: {e}")
        exit()

# 2. Check the installed library version
try:
    import pkg_resources
    version = pkg_resources.get_distribution("google-generativeai").version
    print(f"Version of 'google-generativeai' library: {version}")
except Exception:
    print("Could not determine the version of 'google-generativeai'. Please ensure it's installed.")

# 3. List all available models for your key
print("\n--- Listing all models available to your API key ---")
try:
    image_model_found = False
    for m in genai.list_models():
        # Let's check for any model that seems capable of image generation
        if 'generateContent' in m.supported_generation_methods and 'vision' not in m.name:
             # The 'vision' models are for input, not output. We are looking for text-to-image.
             # Image models often have 'image' or 'imagen' in their name.
            print(f"  - Model: {m.name}")
            if 'image' in m.name:
                image_model_found = True

    if not image_model_found:
        print("\nWARNING: No obvious image generation models (like 'imagen' or 'imagegeneration') were found.")
        print("This could be due to your account's region or permissions.")

except Exception as e:
    print(f"\nERROR: An exception occurred while trying to list the models: {e}")

print("\n--- Diagnostic Complete ---")