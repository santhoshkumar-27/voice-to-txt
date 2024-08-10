# from pydub import AudioSegment

# # Path to the MP3 file
# mp3_file = "test.mp3"
# # Path to save the converted WAV file
# wav_file = "path_to_save_converted_audio.wav"

# # Convert MP3 to WAV
# audio = AudioSegment.from_mp3(mp3_file)
# audio.export(wav_file, format="wav")
from moviepy.editor import AudioFileClip

# Path to the MP3 file
mp3_file = "test.mp3"
# Path to save the converted WAV file
wav_file = "path_to_save_converted_audio.wav"

# Load and convert
audio_clip = AudioFileClip(mp3_file)
audio_clip.write_audiofile(wav_file)