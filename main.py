from pydub import AudioSegment
import speech_recognition as sr

# Function to split audio into chunks
def split_audio(audio, chunk_length_ms):
    return [audio[i:i+chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

# Load the WAV file
wav_file_path = "path_to_save_converted_audio.wav"
audio = AudioSegment.from_wav(wav_file_path)

# Split the audio into chunks (e.g., 30 seconds each)
chunk_length_ms = 30 * 1000  # 30 seconds
audio_chunks = split_audio(audio, chunk_length_ms)

# Initialize recognizer
recognizer = sr.Recognizer()

# Transcribe each chunk
full_transcription = ""
for i, chunk in enumerate(audio_chunks):
    chunk_filename = f"chunk_{i}.wav"
    chunk.export(chunk_filename, format="wav")
    
    with sr.AudioFile(chunk_filename) as source:
        audio_data = recognizer.record(source)
        try:
            transcription = recognizer.recognize_google(audio_data)
            full_transcription += transcription + " "
        except sr.UnknownValueError:
            print(f"Could not understand audio in chunk {i}")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

# Print or save the full transcription
print(full_transcription)
