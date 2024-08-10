import speech_recognition as sr

# Path to the audio file
audio_file_path = "path_to_save_converted_audio.wav"

# Initialize recognizer
recognizer = sr.Recognizer()

# Load the audio file
with sr.AudioFile(audio_file_path) as source:
    audio_data = recognizer.record(source)

# Transcribe the audio to text
transcription = recognizer.recognize_google(audio_data)
print(transcription)