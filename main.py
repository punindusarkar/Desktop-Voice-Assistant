


import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os
import smtplib
import pyautogui
import platform
import random
import webbrowser















def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("I am your Desktop Assistant. How can I assist you today?")

def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't get that. Could you please repeat?")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def open_website(url):
    webbrowser.open(url)
    speak(f"Opening {url}")

def play_music(song):
    pywhatkit.playonyt(song)
    speak(f"Playing {song}")

def open_file_manager():
    system_platform = platform.system().lower()

    if system_platform == 'windows':
        os.startfile('explorer.exe')
    elif system_platform == 'darwin':
        os.system('open .')
    elif system_platform == 'linux':
        os.system('xdg-open .')

    speak("File manager opened.")






def send_email(receiver, subject, body):
    # Replace these with your email credentials and SMTP server details
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, receiver, message)
        server.quit()

        speak("Email sent successfully.")
    except Exception as e:
        speak(f"Error sending email: {str(e)}")

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    speak("Screenshot taken and saved.")

def open_music_player():
    system_platform = platform.system().lower()

    if system_platform == 'windows':
        os.startfile('wmplayer.exe')
    elif system_platform == 'darwin':
        os.system('open -a "Music"')
    elif system_platform == 'linux':
        os.system('rhythmbox &')

    speak("Music player opened.")

def adjust_volume(action):
    if action == 'up':
        pyautogui.press('volumeup')
    elif action == 'down':
        pyautogui.press('volumedown')
    speak(f"Volume {action}.")



def open_camera():
        os.system("start microsoft.windows.camera:")
        speak("camera opened.")




def open_paint():
        os.system("start mspaint")
        speak("Paint opened.")


def open_word():
        os.system("start winword")
        speak("Word opened.")



def open_notepad():
    os.system("start notepad")


def open_calculator():
    os.system("start calc")


def open_google_maps():
    url = "https://www.google.com/maps"
    webbrowser.open(url)



def open_whatsapp():
    url = "https://web.whatsapp.com/"
    webbrowser.open(url)


def open_google():
    url ="https://www.google.com/"
    webbrowser.open


def open_youtube():
    url= "https://www.youtube.com"






































def main():
    wish_me()

    while True:
        query = take_command()

        if query:
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak(f"According to Wikipedia: {result}")
            


            

            elif 'what is your name' in query:
                speak('i dont know my i am Desktop assistant what can i help you..')
            
            elif 'time' in query:
                current_time = datetime.datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}")

            

            elif 'date' in query:
                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                speak(f"Today's date is {current_date}")
            elif 'file manager' in query:
                open_file_manager()


            elif 'what are you doing' in query:
                speak('i am listening say me some thing.')
            
            elif 'send email' in query:
                speak("Whom do you want to send the email to?")
                receiver = take_command()
                speak("What is the subject of the email?")
                subject = take_command()
                speak("What should be the content of the email?")
                body = take_command()
                send_email(receiver, subject, body)

            

            
            elif 'take screenshot' in query:
                take_screenshot()
            elif 'music player' in query:
                open_music_player()

            elif 'play music' in query:
                music_folder = "G:/songe"
                songs = os.listdir(music_folder)
                random_song = random.choice(songs)
                os.startfile(os.path.join(music_folder, random_song))

            elif 'What are you doing' in query:
                speak("i am assiste you for use the computer desktop")

            




            elif 'volume up' in query:
                adjust_volume('up')
            elif 'volume down' in query:
                adjust_volume('down')
            
            elif "good" in query:
                speak("Glad to hear that sir!!")
                print("Glad to hear that sir!!")

            
            elif "open camera" in query:
                open_camera()


            elif "open paint" in query:
                open_paint()

            elif "open word" in query:
                open_word()


            elif "open notepad" in query:
                speak("Opening Notepad.")
                open_notepad()


            elif "open calculator" in query:
                speak("Opening Calculator.")
                open_calculator()


            elif "open google maps" in query:
                speak("Opening Google Maps.")
                open_google_maps()



            elif "open whatsapp" in query:
                speak("Opening WhatsApp.")
                open_whatsapp()


            elif "open google" in query:
                speak("Opening google")
                open_google()

            elif "open google maps" in query:
                speak("Opening google maaps")
                open_google_maps()





































            elif 'quit' in query or 'exit' in query:
                speak("Thank you and Goodbye!")


                break
            else:
                speak("I am not sure about that. Can you please clarify?")



if __name__ == "__main__":

    
    main()
