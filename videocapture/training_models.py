import os
import numpy as np
from PIL import Image
from .stream_dataset import FACE_DETECTOR

def getImageAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faceSamples = []
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')
        image_numpy = np.array(PIL_img, 'uint8')
        print("IMAGE PATHS: ", os.path.split(imagePath)[-1].split(".")[0])
        faces = FACE_DETECTOR.detectMultiScale(image_numpy)

        for (x, y, w, h) in faces:
            faceSamples.append(image_numpy[y:y + h, x:x + w])
            ids.append(os.path.split(imagePath)[-1].split(".")[0])
    return faceSamples, ids
