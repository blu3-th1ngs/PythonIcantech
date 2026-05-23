import os
import cv2

current_dir = os.path.dirname(os.path.abspath(__file__))
xml_path = os.path.join(current_dir, 'haarcascade_frontalface_default.xml')

face_cascade = cv2.CascadeClassifier(xml_path)

if face_cascade.empty():
    print("Error: Cannot load XML file.")
    exit()

cap = None
# Try index 0, 1, and 2 to find any working webcam
for index in [0, 1, 2]:
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        print(f"Successfully connected to camera index: {index}")
        break
    cap.release()

if cap is None or not cap.isOpened():
    print("\n[!] CRITICAL ERROR: OpenCV cannot find any working webcam.")
    print("1. Make sure your webcam is physically plugged in/turned on.")
    print("2. Check Windows Settings -> Privacy -> Camera, and ensure 'Allow apps to access your camera' is turned ON.")
    print("3. Close Discord, Zoom, or Chrome tabs that might be using your camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Face Detection - Lesson 10', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
