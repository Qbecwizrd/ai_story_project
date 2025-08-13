from django.shortcuts import render
import os
import speech_recognition as sr
from pydub import AudioSegment
from story_app.langchain_pipeline import generate_story_parts, generate_image_from_hf


def index(request):
    if request.method == 'POST':
        user_prompt = request.POST.get('prompt')
        audio_file = request.FILES.get('audio')

        audio_path = None
        if audio_file:
            # Save uploaded file
            upload_dir = 'story_app/uploads'
            os.makedirs(upload_dir, exist_ok=True)
            audio_path = os.path.join(upload_dir, audio_file.name)
            with open(audio_path, 'wb+') as destination:
                for chunk in audio_file.chunks():
                    destination.write(chunk)

            # Convert to WAV if needed
            if not audio_path.lower().endswith('.wav'):
                wav_path = os.path.splitext(audio_path)[0] + '.wav'
                AudioSegment.from_file(audio_path).export(wav_path, format="wav")
                audio_path = wav_path

            # If no text prompt, transcribe audio
            if not user_prompt:
                recognizer = sr.Recognizer()
                with sr.AudioFile(audio_path) as source:
                    audio_data = recognizer.record(source)
                    try:
                        user_prompt = recognizer.recognize_google(audio_data)
                    except sr.UnknownValueError:
                        user_prompt = "(Audio could not be transcribed)"
                    except sr.RequestError:
                        user_prompt = "(Error with transcription service)"

        # Generate story
        story = character = background = None
        character_img = background_img = None

        if user_prompt and "could not" not in user_prompt.lower():
            story, character, background = generate_story_parts(user_prompt)

            # Generate images for character and background
            if character:
                character_img = generate_image_from_hf(character, "character_image")
            if background:
                background_img = generate_image_from_hf(background, "background_image")

        return render(request, 'result.html', {
            'prompt': user_prompt,
            'audio_file': audio_file.name if audio_file else None,
            'story': story,
            'character': character,
            'background': background,
            'character_img': character_img,
            'background_img': background_img
        })

    return render(request, 'index.html')
