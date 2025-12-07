import subprocess
import os
import shlex
import speech_recognition as sr
import pyttsx3
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from geopy.geocoders import Nominatim
import cv2
import paramiko
import warnings

# Suppressing warnings from paramiko
warnings.filterwarnings(action='ignore', module='.*paramiko.*')

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()
geolocator = Nominatim(user_agent="PythonSpeechRecognition")

def speak(text):
    """Function to provide voice feedback"""
    tts_engine.say(text)
    tts_engine.runAndWait()

def open_notepad():
    """Function to open Notepad"""
    try:
        subprocess.Popen(['notepad.exe'])
        speak("Opening Notepad")
    except FileNotFoundError:
        print("Notepad application not found.")
        speak("Notepad application not found.")

def open_chrome():
    """Function to open Chrome"""
    try:
        subprocess.Popen(['chrome.exe'])
        speak("Opening Chrome")
    except FileNotFoundError:
        print("Chrome application not found.")
        speak("Chrome application not found.")

def open_vm():
    """Function to open Oracle Virtual Machine"""
    try:
        subprocess.Popen([r'C:\\Program Files\\Oracle\\VirtualBox.exe'])  # Replace with the actual path to VirtualBox executable
        speak("Opening Oracle VM VirtualBox Manager")
    except FileNotFoundError:
        print("Oracle VM VirtualBox Manager application not found.")
        speak("Oracle VM VirtualBox Manager application not found.")

def show_location():
    """Function to show current location"""
    try:
        location = geolocator.geocode("address")
        print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
        speak(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
    except Exception as e:
        print("Error retrieving location:", e)
        speak("Error retrieving location")

def sum_numbers(*args):
    """Function to sum numbers"""
    try:
        numbers = map(float, args)
        result = sum(numbers)
        print(f"The sum is: {result}")
        speak(f"The sum is {result}")
    except ValueError:
        print("Please provide valid numbers.")
        speak("Please provide valid numbers.")

def change_volume(direction):
    """Function to change the volume"""
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    current_volume = volume.GetMasterVolumeLevelScalar()
    if direction == "up":
        new_volume = min(current_volume + 0.1, 1.0)
    elif direction == "down":
        new_volume = max(current_volume - 0.1, 0.0)
    else:
        print("Invalid volume direction.")
        speak("Invalid volume direction.")
        return

    volume.SetMasterVolumeLevelScalar(new_volume, None)
    print(f"Volume {'increased' if direction == 'up' else 'decreased'}")
    speak(f"Volume {'increased' if direction == 'up' else 'decreased'}")

def start_video():
    """Function to start video capture"""
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def capture_photo():
    """Function to capture a photo"""
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    cv2.imwrite('captured_photo.jpg', frame)
    print("Photo captured successfully.")
    # Show the captured photo
    img = cv2.imread('captured_photo.jpg')
    cv2.imshow('Captured Photo', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def execute_ssh_command(host, username, password, command):
    """Function to execute SSH command"""
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missin
