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


def transcribe_audio(wav_file, transcriptions_list):
    """Convert WAV to text using SpeechRecognition and append to list"""
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(wav_file) as source:
            print("🎙 Processing audio...")
            audio_data = recognizer.record(source)
            print("📝 Transcribing...")
            text = recognizer.recognize_google(audio_data)
            print("✅ Transcription:\n", text)

            # Append the transcription (number or word) to the list
            transcriptions_list.append(text)
            print("✅ Transcription added to list")

            # Append the new transcription to the text file
            with open("transcription.txt", "a") as file:
                file.write(text + "\n")
            print("✅ Transcription added to transcription.txt")

    except sr.UnknownValueError:
        print("❌ Speech Recognition could not understand the audio")
    except sr.RequestError:
        print("❌ Could not connect to Speech Recognition service")
    except Exception as e:
        print(f"❌ Error processing WAV: {str(e)}")


def transcribe_mp3(mp3_file):
    """Convert MP3 to WAV and then transcribe it"""
    transcriptions_list = []  # Initialize an empty list for transcriptions

    # Read the existing transcription file (if any) and load previous transcriptions
    if os.path.exists("transcription.txt"):
        with open("transcription.txt", "r") as file:
            previous_transcriptions = file.readlines()
            transcriptions_list.extend(
                [line.strip() for line in previous_transcriptions]
            )
        print("✅ Loaded previous transcriptions.")

    wav_file = convert_mp3_to_wav(mp3_file)
    if wav_file:
        transcribe_audio(wav_file, transcriptions_list)
    else:
        print("❌ MP3 conversion failed!")

    return transcriptions_list


# Run the function with your MP3 file
transcriptions = transcribe_mp3("audioResponse\homeLoanRes3P.wav")
print("✅ All transcriptions:", transcriptions)
