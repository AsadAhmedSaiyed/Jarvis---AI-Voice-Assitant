# 🤖 Jarvis: Voice-Controlled AI Assistant

## Project Overview

**Jarvis** is a powerful, voice-controlled personal assistant built in Python. It performs tasks like opening websites, speaking news updates, and answering questions using AI.  
It integrates:

- 🎤 Speech Recognition  
- 🗣️ Text-to-Speech  
- ⚡ Ultra-fast LLM (Groq)  
- 🌐 Web automation  
- 📰 News API for real-time headlines  

---

## ✨ Key Features

- 🎙️ **Voice Activation:** Wake word **"Jarvis"** triggers the assistant.
- ⚡ **High-Speed AI:** Uses **Groq LLaMA 3.3** with almost real-time responses.
- 🌐 **Web Automation:** Opens Google, Facebook, LinkedIn, etc.
- 📰 **Live News:** Fetches & reads top U.S. headlines using NewsAPI.
- 🗣️ **Text-to-Speech:** Uses `pyttsx3` for smooth audio output.
- 🎧 **Wake Word System:** Listens continuously and activates only when “Jarvis” is spoken.

---

## 🚀 Getting Started

### 🧩 Prerequisites

- Python **3.8+**
- API Keys:
  - **Groq API Key** → https://console.groq.com/keys  
  - **NewsAPI Key** → https://newsapi.org/

---

## 📥 Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd Jarvis
````

---

### 2️⃣ Create & Activate Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install speechrecognition pyaudio setuptools groq python-dotenv requests pyttsx3
```

⚠️ **Note:**
If `pyaudio` fails, install a prebuilt wheel from:
[https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

---

### 4️⃣ Configure Environment Variables

Create a new file named **`.env`** in your project folder:

```
GROQ_API_KEY="YOUR_GROQ_API_KEY_HERE"
NEWS_API_KEY="YOUR_NEWS_API_KEY_HERE"
```

---

## ▶️ Running Jarvis

Run the project:

```bash
python jarvis.py
```

### 🔊 What Happens

1. Jarvis loads API keys
2. Says: **“Initializing Jarvis ….”**
3. Console shows: **Listening ...**
4. Say the wake word **Jarvis**
5. Jarvis responds **“Yes?”** and waits for your command

---

## 🎮 Usage Guide

### Example Commands

| Speak This                            | Jarvis Will…                 |
| ------------------------------------- | ---------------------------- |
| “Jarvis, open google”                 | Open Google.com              |
| “Jarvis, open linkedin”               | Open LinkedIn.com            |
| “Jarvis, news”                        | Read top U.S. news headlines |
| “Jarvis, who discovered electricity?” | Answer using Groq LLM        |

---

## 🧠 Code Structure Overview

### `speak(text)`

Handles all text-to-speech output.

### `aiProcess(cmd)`

Uses **Groq LLaMA 3.3** to answer questions.

### `processCommand(c)`

* Opens websites
* Fetches news
* Sends other commands to AI

---

## 🔧 Customization

### Change the Groq model

```python
model="llama-3.3-70b-versatile"
```

Other faster models:

* `"llama-3.3-8b-instant"`
* `"mixtral-8x7b"`

---

### Add a Custom Command

```python
elif "open spotify" in c.lower():
    webbrowser.open("https://open.spotify.com")
    print("Opened Spotify successfully!")
```

---

## 📁 Recommended Folder Structure

```
Jarvis/
│── main.py
│── README.md
│── .env
│── venv/
```

---

## 🤝 Contributing

1. Fork the repo
2. Create your branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m "Added new feature"`
4. Push: `git push origin feature/YourFeature`
5. Open a Pull Request

---

## 📄 License

Licensed under the **MIT License**.

---

## ⭐ Support

If you like this project, give it a **star** ⭐ on GitHub!


