import speech_recognition as sr
import pyautogui
import keyboard
import time

def listen_and_send(timeout=12):  # Increase the timeout value
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=timeout)
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected.")
            return None

    start_time = time.time()
    try:
        text = recognizer.recognize_google(audio)
        end_time = time.time()
        print(f"You said: {text}")
        send_text_to_focused_window(text)
        print(f"Translation took {end_time - start_time:.2f} seconds.")
        return text
    except sr.UnknownValueError:
        print("Sorry, couldn't understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def send_text_to_focused_window(text, typing_speed=0.06):  # Increase the typing speed
    # Simulate pressing Right Alt key
    keyboard.press_and_release('right alt')

    # Send the recognized text to the focused window with a typing speed delay
    pyautogui.typewrite(text, interval=typing_speed)

    # Simulate pressing Enter key
    pyautogui.press('enter')

if __name__ == "__main__":
    while True:
        print("Press Right Alt to start listening...")
        keyboard.wait('right alt')

        text = listen_and_send()

        if text:
            print("Last recognized text:", text)

        # Add a brief pause to avoid issues with quickly pressing Alt again
        time.sleep(0.3)
