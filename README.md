# mega_project-jarvis

Lightweight voice assistant (Jarvis) that can open websites, play songs (from a local mapping), and read top headlines via NewsAPI.

## Features
- Wake-word listening ("jarvis") and voice commands
- Open Google / YouTube / Instagram
- Play songs from your `musiclibrary`
- Read top headlines from NewsAPI (configurable via env var)

## Requirements
- Python 3.8+
- Microphone (for speech input)

Python packages:
- speech_recognition
- requests
- gTTS
- pygame
- pyaudio (or use pipwin on Windows)

## Setup (Windows)
1. Create & activate virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\Activate
   ```

2. Install dependencies:
   ```
   pip install speechrecognition requests gTTS pygame
   # Install PyAudio (recommended via pipwin on Windows)
   pip install pipwin
   pipwin install pyaudio
   ```

3. Configure NewsAPI key (do NOT commit keys):
   - For current PowerShell session:
     ```
     $env:NEWSAPI_KEY = "YOUR_NEWSAPI_KEY"
     ```
   - To persist:
     ```
     setx NEWSAPI_KEY "YOUR_NEWSAPI_KEY"
     ```

4. Run:
   ```
   python main.py
   ```

## Notes & Security
- Remove any hard-coded API keys from source. Use environment variables as shown.
- If a key was accidentally committed, rotate/regenerate it and remove it from git history before pushing.
- If microphone access fails, ensure PyAudio is installed and Windows privacy settings allow microphone access.

## Contributing
- Create a branch, make changes, push, and open a PR.
- Keep secrets out of commits.

## License
Add a license file or specify your preferred license here.
```<!-- filepath: c:\Users\hp\Desktop\python\mega_project-jarvis\README.md -->
# mega_project-jarvis

Lightweight voice assistant (Jarvis) that can open websites, play songs (from a local mapping), and read top headlines via NewsAPI.

## Features
- Wake-word listening ("jarvis") and voice commands
- Open Google / YouTube / Instagram
- Play songs from your `musiclibrary`
- Read top headlines from NewsAPI (configurable via env var)

## Requirements
- Python 3.8+
- Microphone (for speech input)

Python packages:
- speech_recognition
- requests
- gTTS
- pygame
- pyaudio (or use pipwin on Windows)

## Setup (Windows)
1. Create & activate virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\Activate
   ```

2. Install dependencies:
   ```
   pip install speechrecognition requests gTTS pygame
   # Install PyAudio (recommended via pipwin on Windows)
   pip install pipwin
   pipwin install pyaudio
   ```

3. Configure NewsAPI key (do NOT commit keys):
   - For current PowerShell session:
     ```
     $env:NEWSAPI_KEY = "YOUR_NEWSAPI_KEY"
     ```
   - To persist:
     ```
     setx NEWSAPI_KEY "YOUR_NEWSAPI_KEY"
     ```

4. Run:
   ```
   python main.py
   ```

## Notes & Security
- Remove any hard-coded API keys from source. Use environment variables as shown.
- If a key was accidentally committed, rotate/regenerate it and remove it from git history before pushing.
- If microphone access fails, ensure PyAudio is installed and Windows privacy settings allow microphone access.

## Contributing
- Create a branch, make changes, push, and open a PR.
- Keep secrets out of commits.

## License
Add a license file or specify your preferred license here.