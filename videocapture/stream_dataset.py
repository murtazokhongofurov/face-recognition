import cv2
import os


FACE_DETECTOR = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
RECOGNIZER = cv2.face.LBPHFaceRecognizer.create()


def gen_frames():
    count = 0
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)
    if not os.path.exists("dataset"):
        os.makedirs("dataset")
    while True:
        success, img = cam.read()  # read the camera frame
        if not success:
            break
        else:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = FACE_DETECTOR.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                count += 1

            k = cv2.waitKey(100) & 0xff
            if k == 27:
                break
            elif count <= 30:
                cv2.imwrite("dataset/User" + str(1) + str(count) + ".jpg", gray[y:y + h, x:x + w])
                # break
            ret, buffer = cv2.imencode('.jpg', img)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cam.release()
    cv2.destroyAllWindows()

