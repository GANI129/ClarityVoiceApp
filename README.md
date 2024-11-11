ClearSpeakRecorder
A professional-grade voice recording application designed to transcribe audio and remove filler words (like "uh", "um", "like") for cleaner, more concise speech. Perfect for enhancing clarity in online presentations, lectures, and personal recordings.

Features
Voice Recording: Record high-quality audio with ease.
Automatic Transcription: Convert audio to text using speech recognition.
Filler Removal: Eliminate filler words to enhance the clarity of transcripts.
User-Friendly Interface: Intuitive interface with a premium design for ease of use.
Requirements
Python 3.6+
Required libraries:
bash
Copy code
pip install PyQt5 pyaudio SpeechRecognition
FFmpeg (for audio handling): Install FFmpeg if not already available on your system.
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/your-username/ClearSpeakRecorder.git
cd ClearSpeakRecorder
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Run the Application

bash
Copy code
python main.py
Usage
Recording: Click the "Record" button to start a 30-second recording.
Transcription: Click "Transcribe" to convert the recorded audio into text.
Filler Removal: Click "Remove Fillers" to remove common filler words from the transcription.
Example
Sample Input Speech:

"Um, so I'm just trying to, like, explain this process, you know? Actually, it's a bit tricky, but uh, we can manage it!"

Expected Output After Removing Fillers:

"I'm trying to explain this process. It's a bit tricky, but we can manage it."

Contributing
Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
