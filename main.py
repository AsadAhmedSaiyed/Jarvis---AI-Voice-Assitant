# to create venv ->  python -m venv venv
# to activate ->  source venv/Scripts/activate
# pip install speechrecognition pyaudio setuptools groq

# execute this part only when file is run directly
from dotenv import load_dotenv
import os
from groq import Groq
import speech_recognition as sr
import webbrowser
import pyttsx3
load_dotenv()
import requests

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not NEWS_API_KEY and not GROQ_API_KEY: 
    raise ValueError("Missing API KEY in environment variables.")

os.environ["NEWS_API_KEY"] = NEWS_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY
print("✅ API key setup complete.")


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
 
def aiProcess(cmd):
    client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content":"You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud and answer in a concise way"
            },
            {
                "role": "user",
                "content": cmd,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content    
        
def processCommand(c):
        if "open google" in c.lower():
            webbrowser.open("https://google.com")
            print("Opened Google succssfully!")
        elif "open facebook" in c.lower():
            webbrowser.open("https://facebook.com")
            print("Opened facebook succssfully!")
        elif "open linkedin" in c.lower():
            webbrowser.open("https://linkedin.com")
            print("Opened Linkedin succssfully!")
        elif "news" in c.lower():
            print("Getting news")
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}")
            if r.status_code == 200:
                # Parse the JSON response
                data = r.json()
                
                # Extract the articles
                articles = data.get('articles', [])
                
                # Print the headlines
                for article in articles[:3]:
                    print(article['title'])
                    speak(article['title']) 
        else:
            # let groq handle the request
            output = aiProcess(c)   
            speak(output)            
        
             

if __name__ == "__main__":
    speak("Initializing Jarvis ....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        
        r = sr.Recognizer()
        try:
            
            with sr.Microphone() as source:
               print("Listening ...!")
               audio = r.listen(source,timeout=5,phrase_time_limit=3)
        # recognize speech
            print("Recognizing...")
            word = r.recognize_google(audio)
            print(word)
    
            if "jarvis" in word.lower():
                speak("Yes?")  
                    
                #Listen for cmd
                with sr.Microphone() as source:
                    print("Jarvis Activated ...!")
                    print("Listening...")
                    audio = r.listen(source,timeout=5,phrase_time_limit=3)
                    command = r.recognize_google(audio)
                    print("Working...")
                    processCommand(command)
                    print("Completed...")
        except sr.WaitTimeoutError:
            print("No speech detected. Listening again...")
        except sr.UnknownValueError:
            print("Could not understand audio. Try again...")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")       