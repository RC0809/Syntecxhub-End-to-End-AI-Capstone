import cv2
import os
import numpy as np

dataset_path = "dataset"
trainer_path = "trainer/trainer.yml"

recognizer = cv2.face.LBPHFaceRecognizer_create()
face_samples = []
ids = []

label_map = {"Rakshit": 1}

for name in os.listdir(dataset_path):
    user_folder = os.path.join(dataset_path, name)

    if not os.path.isdir(user_folder):
        continue

    user_id = label_map.get(name)

    for image_name in os.listdir(user_folder):
        image_path = os.path.join(user_folder, image_name)
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            continue

        face_samples.append(img)
        ids.append(user_id)

print(ids)
print(np.array(ids))
print(np.array(ids).dtype)

recognizer.train(face_samples, np.array(ids))
recognizer.write(trainer_path)

print("Model trained successfully.")
print(f"Saved at: {trainer_path}")