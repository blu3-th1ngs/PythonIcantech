import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import time

def text_to_speech(text_vietnamese):
    tts = gTTS(text=text_vietnamese, lang='vi', slow=False)
    filename = "temp_voice.mp3"
    tts.save(filename)
  
    playsound(filename)

    if os.path.exists(filename):
        os.remove(filename)

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            text_result = recognizer.recognize_google(audio_data, language="vi-VN")
            return text_result
        except:
            return ""

if __name__ == "__main__":
    van_ban_mau = "Xin chào, đây là ứng dụng thử nghiệm nhận diện âm thanh bằng tiếng Việt."
    text_to_speech(van_ban_mau)

    while True:
        ket_qua = speech_to_text()
        if ket_qua:
            print(ket_qua)
            ket_qua_lower = ket_qua.lower().strip()
            if "stop" in ket_qua_lower or "dừng" in ket_qua_lower:
                text_to_speech("Chương trình kết thúc.")
                break
        time.sleep(1)