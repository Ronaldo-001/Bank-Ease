import os

os.environ["PATH"] += (
    os.pathsep + r"C:\Beacon\Personal\DEV\ffmpeg-master-latest-win64-gpl-shared\bin"
)

import speech_recognition as sr
from pydub import AudioSegment


def convert_mp3_to_wav(mp3_file, wav_file="converted_audio.wav"):
    """Convert MP3 to WAV using FFmpeg via pydub"""
    try:
        audio = AudioSegment.from_mp3(mp3_file)
        audio.export(wav_file, format="wav")
        print(f"✅ MP3 converted to WAV: {wav_file}")
        return wav_file
    except Exception as e:
        print(f"❌ Error converting MP3: {str(e)}")
        return None


def transcribe_audio(wav_file):
    """Convert WAV to text using SpeechRecognition"""
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(wav_file) as source:
            print("🎙 Processing audio...")
            audio_data = recognizer.record(source)
            print("📝 Transcribing...")
            text = recognizer.recognize_google(audio_data)
            print("✅ Transcription:\n", text)
            with open("transcription.txt", "w") as file:
                file.write(text)
            print("✅ Transcription saved to transcription.txt")
    except sr.UnknownValueError:
        print("❌ Speech Recognition could not understand the audio")
    except sr.RequestError:
        print("❌ Could not connect to Speech Recognition service")
    except Exception as e:
        print(f"❌ Error processing WAV: {str(e)}")


def transcribe_mp3(mp3_file):
    """Convert MP3 to WAV and then transcribe it"""
    wav_file = convert_mp3_to_wav(mp3_file)
    if wav_file:
        transcribe_audio(wav_file)
    else:
        print("❌ MP3 conversion failed!")


# Run the function with your MP3 file
transcribe_mp3("audioResponse\homeLoanRes1.wav")
