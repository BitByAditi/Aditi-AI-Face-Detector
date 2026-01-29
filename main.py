import cv2
import time
import threading
import subprocess

def speak(text):
    subprocess.Popen(["say", text])

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

last_speech_time = 0
speech_delay = 3

print("------------------------------------------")
print("ADITI'S AI IS NOW RUNNING...")
print("Look at the camera!")
print("------------------------------------------")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            "A HUMAN IS DETECTED",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        current_time = time.time()
        if current_time - last_speech_time > speech_delay:
            print("a human is detected")
            
            # 🔑 Run speech in a separate thread
            threading.Thread(target=speak, args=("hii cutie",), daemon=True).start()

            last_speech_time = current_time

    cv2.imshow("AI Assistant Window", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

