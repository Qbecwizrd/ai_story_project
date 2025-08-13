# 🎨📖 AI Story & Image Generator

Welcome to **AI Story & Image Generator** — a Django-based web app that turns your **ideas or voice recordings** into **beautiful AI-generated stories** ✍️ and **vivid images** 🖼️ using Hugging Face models!  

---

## ✨ Features

- 🗣️ **Speech-to-Text** — Upload an audio file and let Google Speech Recognition transcribe it.  
- 💬 **Prompt-to-Story** — Write a story idea and watch it expand into a full narrative.  
- 🧑‍🎨 **Character & Background Generation** — Get separate detailed descriptions for characters and scenes.  
- 🖌️ **AI Image Generation** — Turn descriptions into images using **Hugging Face's `black-forest-labs/FLUX.1-schnell` model**.  
- 🌐 **Web Interface** — Clean, simple UI for both text and file inputs.  

---

## 🛠️ Tech Stack

- **Backend:** 🐍 Python + Django
- **Frontend:** HTML + CSS (Django templates)
- **AI Models:**
  - 🖼️ Image: Hugging Face Stable Diffusion / FLUX
  - 📝 Story: LLM pipeline (LangChain + Groq/OpenAI API)
  - 🎤 Audio: Google Speech Recognition
- **Libraries:**
  - `django`
  - `huggingface_hub`
  - `langchain`
  - `pillow`
  - `speechrecognition`
  - `pydub`
  - `python-dotenv`

---

## 📂 Project Structure

