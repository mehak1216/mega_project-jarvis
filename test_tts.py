import speech_recognition as sr
import webbrowser
import requests
from gtts import gTTS
import pygame
import tempfile
import os
import time
import uuid
import musiclibrary   # your custom file for songs

# Your News API key
newsapi = "3e0e9b901e3545239c3d803b87ebe9b9"

# ---- SPEAK FUNCTION ---- #
def speak(text):
    try:
        # Unique filename each time
        tmp_file = os.path.join(tempfile.gettempdir(), f"jarvis_{uuid.uuid4().hex}.mp3")

        # Save speech
        tts = gTTS(text=text, lang="en")
        tts.save(tmp_file)

        # Initialize pygame mixer if not already running
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        # Load and play
        pygame.mixer.music.load(tmp_file)
        pygame.mixer.music.play()

        # Wait until finished
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.stop()

        # Delete temp file after use
        if os.path.exists(tmp_file):
            os.remove(tmp_file)

    except Exception as e:
        print("Speech error:", e)

# ---- COMMAND HANDLER ---- #
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        try:
            song = c.lower().split(" ")[1]
            link = musiclibrary.music.get(song)
            if link:
                webbrowser.open(link)
                speak(f"Playing {song}")
            else:
                speak("Song not found in your library.")
        except Exception:
            speak("Please say the song name again.")
    elif "news" in c.lower():
        a = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
    r = requests.get(a)

    if r.status_code == 200:
        data = r.json()
        articles = data.get('articles', [])

        if not articles:
            speak("Sorry, I could not find any news right now.")
        else:
            speak("Here are the top headlines.")
            for article in articles[:5]:   # only top 5
                headline = article.get('title', '')
                print("📰 News:", headline)  # Debug print
                if headline:
                    speak(headline)


    else:
        #let openai handle the request
        pass
    


# ---- MAIN LOOP ---- #
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("🎙️ Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)

            try:
                word = recognizer.recognize_google(audio)
                print("Heard:", word)

                if "jarvis" in word.lower():
                    speak("Yes?")
                    with sr.Microphone() as source:
                        print("🤖 Jarvis Active... waiting for command")
                        audio = recognizer.listen(source, timeout=5)
                        command = recognizer.recognize_google(audio)
                        print("Command:", command)
                        processcommand(command)

            except sr.UnknownValueError:
                print("Did not understand...")
                continue

        except sr.WaitTimeoutError:
            continue
        except Exception as e:
            print("Error:", e)

