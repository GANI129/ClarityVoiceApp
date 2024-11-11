import sys 
import pyaudio # type: ignore
import wave
import speech_recognition as sr # type: ignore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt

# Function to record audio
def record_audio(filename="input.wav", duration=20):
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

    print("Recording...")
    frames = []

    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

# Function to transcribe audio
def transcribe_audio(filename="input.wav"):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "API unavailable or unresponsive"

# Function to remove filler words
def remove_fillers(text):
    fillers = ["uh", "um", "like", "you know", "so", "actually"]
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in fillers]
    return ' '.join(filtered_words)

class VoiceRecorderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Premium Voice Recorder")
        self.setGeometry(300, 300, 400, 400)
        self.setStyleSheet("background-color: #2c2c2c; color: #eee;")
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout()

        # Header Label with new styling
        header_label = QLabel("🎙 Professional Voice Recorder")
        header_label.setFont(QFont("Arial", 20, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("color: #00e676; margin-bottom: 20px;")
        layout.addWidget(header_label)

        # Record Button with new style
        self.record_button = QPushButton("Record")
        self.record_button.setFont(QFont("Arial", 14))
        self.record_button.setIcon(QIcon(r"C:\Users\ganig\Downloads\voice.png")) 
        self.record_button.setStyleSheet("""
            QPushButton {
                background-color: #424242; 
                padding: 10px; 
                color: #ffffff;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #616161;
            }
        """)
        self.record_button.clicked.connect(self.record_audio)
        layout.addWidget(self.record_button)

        # Transcribe Button with new style
        self.transcribe_button = QPushButton("Transcribe")
        self.transcribe_button.setFont(QFont("Arial", 14))
        self.transcribe_button.setIcon(QIcon(r"C:\Users\ganig\Downloads\document-xxl.png"))  
        self.transcribe_button.setStyleSheet("""
            QPushButton {
                background-color: #424242; 
                padding: 10px; 
                color: #ffffff;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #616161;
            }
        """)
        self.transcribe_button.clicked.connect(self.transcribe_audio)
        layout.addWidget(self.transcribe_button)

        # Remove Fillers Button with new style
        self.remove_fillers_button = QPushButton("Remove Fillers")
        self.remove_fillers_button.setFont(QFont("Arial", 14))
        self.remove_fillers_button.setIcon(QIcon(r"C:\Users\ganig\Downloads\icone-de-filtre-rouge.png"))  
        self.remove_fillers_button.setStyleSheet("""
            QPushButton {
                background-color: #424242; 
                padding: 10px; 
                color: #ffffff;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #616161;
            }
        """)
        self.remove_fillers_button.clicked.connect(self.remove_fillers_text)
        layout.addWidget(self.remove_fillers_button)

        # Display Area for Text with new style
        self.result_display = QTextEdit()
        self.result_display.setFont(QFont("Arial", 12))
        self.result_display.setStyleSheet("""
            background-color: #222;
            color: #eee;
            padding: 10px;
            border: 1px solid #555;
            border-radius: 5px;
        """)
        layout.addWidget(self.result_display)

        self.setLayout(layout)

    def record_audio(self):
        self.result_display.append("Recording audio...")
        record_audio()
        self.result_display.append("Recording finished.")

    def transcribe_audio(self):
        self.result_display.append("Transcribing audio...")
        text = transcribe_audio()
        self.result_display.append(f"Transcription: {text}")

    def remove_fillers_text(self):
        text = self.result_display.toPlainText()
        filtered_text = remove_fillers(text)
        self.result_display.setText(f"Filtered Text: {filtered_text}")

# Run the application
app = QApplication(sys.argv)
app.setStyle('Fusion')
window = VoiceRecorderApp()
window.show()
sys.exit(app.exec_())
