import speech_recognition as sr
from textblob import TextBlob
from gtts import gTTS
import os

def analyze_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak now...")
        try:
            # Listen to user input
            audio = recognizer.listen(source, timeout=5)
            # Convert speech to text
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            # Perform text analysis
            feedback = analyze_text(text)
            print("Feedback:", feedback)

            # Convert feedback to speech
            tts = gTTS(text=feedback, lang='en')
            tts.save("feedback.mp3")
            os.system("start feedback.mp3")  # Use "xdg-open" for Linux or "open" for macOS
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Error: {e}")

def analyze_text(text):
    blob = TextBlob(text)
    feedback = []

    # Check for grammatical correctness
    if blob.correct() != text:
        feedback.append(f"Consider rephrasing your sentence to: '{blob.correct()}'.")

    # Check sentence polarity
    if blob.sentiment.polarity < 0:
        feedback.append("Your tone seems negative; try to sound more positive.")

    # Overall feedback
    if not feedback:
        feedback.append("Great job! Your speech is clear and grammatically correct.")
    return " ".join(feedback)

if __name__ == "__main__":
    analyze_speech()
