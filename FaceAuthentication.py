import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def recognize_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        if w < 150 or h < 150:
            return False, frame, "Show full face clearly"

        face = gray[y:y+h, x:x+w]
        user_id, confidence = recognizer.predict(face)

        if user_id == 1 and confidence < 60:
            status = "Face Matched"
            color = (0, 255, 0)
            matched = True
        else:
            status = "Access Denied"
            color = (0, 0, 255)
            matched = False

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, status, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

        return matched, frame, status

    return False, frame, "Scanning Face..."