

---

```markdown
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

```

story\_app\_v2/
│
├── story\_project/            # Django project folder
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── story\_app/                # Main app
│   ├── templates/            # HTML files
│   ├── static/                # Generated images
│   ├── uploads/               # Uploaded audio files
│   ├── langchain\_pipeline.py  # AI logic (story + image generation)
│   └── views.py               # Django views
│
├── venv/                      # Virtual environment
├── phases.md                  # Notes/Planning
└── README.md

````

---

## 🚀 Getting Started

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/story_app_v2.git
cd story_app_v2
````

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Add Environment Variables

Create a `.env` file in the project root:

```
HF_API_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_key   # Or OpenAI key if using OpenAI
```

⚠️ **Do NOT commit `.env` to GitHub!**

---

## 🖥️ Running the App

```bash
python manage.py runserver
```

Visit: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)** 🌐

---

## 📸 Screenshots

### Main Input Page

![Main Input](https://via.placeholder.com/600x300?text=Main+Page+Screenshot)

### Result Page

![Generated Story & Images](https://via.placeholder.com/600x300?text=Result+Screenshot)

---

## 💡 Example Prompt

> "In a futuristic city floating in the clouds, a young inventor discovers a secret blueprint that could save the world from an impending energy crisis."

This will produce:

* **📜 Story:** An engaging AI-generated short story
* **🧑 Character Image:** AI-rendered protagonist
* **🏙️ Background Image:** Beautiful AI-generated scene

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, open an issue first to discuss what you’d like to change.

---

## 📜 License

This project is licensed under the **MIT License**.

---

💖 *Built with passion for AI, creativity, and storytelling!*

```

---

If you want, I can also **make a matching `requirements.txt`** so your README install section works perfectly without manually typing dependencies.
```


Here’s a lively, emoji-rich `README.md` for your project:

```markdown
# 🎨📚 AI Story & Image Generator

A Django web app that turns your ✍️ ideas or 🎤 voice recordings into **stories** and vivid **AI-generated images** using Hugging Face models!  

---

## ✨ Features

- 🗣️ **Speech-to-Text** — Upload audio and transcribe it.
- 💬 **Prompt-to-Story** — Expand short ideas into complete narratives.
- 🧑‍🎨 **Character & Background** — Get detailed scene descriptions.
- 🖌️ **AI Image Generation** — Render characters and backgrounds using `black-forest-labs/FLUX.1-schnell`.
- 🌐 **Simple Web UI** — Text and audio input support.

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML + Django Templates
- **AI Models:**
  - Image: Hugging Face FLUX
  - Story: LangChain + LLM
  - Audio: Google Speech Recognition
- **Key Libraries:**  
  `django` · `huggingface_hub` · `langchain` · `pillow` · `speechrecognition` · `pydub` · `python-dotenv`

---

## 📂 Project Structure

```

story\_app\_v2/
│
├── story\_project/            # Django project config
├── story\_app/                 # Main application
│   ├── templates/             # HTML files
│   ├── static/                 # Generated images
│   ├── uploads/                # Uploaded audio
│   ├── langchain\_pipeline.py   # AI logic
│   └── views.py                # Request handling
├── venv/                       # Virtual environment
├── phases.md                   # Notes
└── README.md

````

---

## 🚀 Getting Started

1️⃣ **Clone Repo**
```bash
git clone https://github.com/YOUR_USERNAME/story_app_v2.git
cd story_app_v2
````

2️⃣ **Create Virtual Environment**

```bash
python -m venv venv
# Mac/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Environment Variables**
Create `.env` in root:

```
HF_API_TOKEN=your_huggingface_token
GROQ_API_KEY=your_groq_api_key
```

⚠️ Do **not** commit `.env` to GitHub.

---

## 🖥 Run App

```bash
python manage.py runserver
```

Visit 👉 `http://127.0.0.1:8000/`

---

## 💡 Example Prompt

> "In a futuristic city floating in the clouds, a young inventor discovers a secret blueprint that could save the world from an impending energy crisis."

Generates:

* 📜 **Story**
* 🧑 **Character Image**
* 🏙 **Background Image**

---


---

💖 *Built with AI, creativity, and storytelling magic!*



