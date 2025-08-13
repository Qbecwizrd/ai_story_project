# Development Phases - LangChain + Django Story App

## Phase 1 - Environment & Project Setup
- Install Python, create virtual environment, install Django & required packages
- Create Django project (`story_project`)
- Create main app (`story_app`)
- Configure `settings.py`:
  - Add `story_app` to INSTALLED_APPS
  - Setup static/templates directories
- Test by running server and seeing default Django welcome page

## Phase 2 - Basic Web Interface
- Create `index.html` template with:
  - Text input for user prompt
  - Optional file upload for audio
- Create `urls.py` in `story_app`
- Create `views.py` function to render the form
- Connect `story_app/urls.py` to `project_root/urls.py`

## Phase 3 - LangChain Orchestration
- Install & setup LangChain in `langchain_pipeline.py`
- Create Chain 1:
  - Generates short story
  - Generates detailed character description
  - Generates detailed background description
- Create Chain 2:
  - Builds prompt from character description
  - Generates character image
- Create Chain 3:
  - Builds prompt from background description
  - Generates background image

## Phase 4 - Image Processing
- Use PIL/OpenCV to merge character & background images into one
- Ensure style and perspective match
- Save merged image to `static/` folder

## Phase 5 - Output Display
- Create `result.html` template:
  - Show short story text
  - Show character description
  - Show merged image
- Modify `views.py` to send generated data to template

## Phase 6 - Error Handling & Testing
- Add try/except blocks for model calls
- Log errors to a file
- Test with multiple prompt variations

## Phase 7 - Documentation & Submission
- Write `README.md` with setup instructions & architecture
- Create `prompts.md` explaining prompt design
- Export `requirements.txt`
- Prepare sample outputs (optional)
- Zip and submit project via Google Form
