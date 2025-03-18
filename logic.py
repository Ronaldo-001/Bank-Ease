import os

def process_transcription():
    """ Reads the transcription.txt file and writes a new file each time. """
    try:
        with open("transcription.txt", "r") as file:
            value = file.read().strip()
            
        print(f"✅ Transcription value read: {value}")
        
        # Generate a unique filename for each run
        filename = f"transaction_{len(os.listdir('.'))}.txt"
        
        with open(filename, "w") as output_file:
            output_file.write(value + "\n")
        
        print(f"✅ Value written to {filename}")
        
    except FileNotFoundError:
        print("❌ transcription.txt not found!")
    except Exception as e:
        print(f"❌ Error reading file: {str(e)}")

if __name__ == "__main__":
    process_transcription()
