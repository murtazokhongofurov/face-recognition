from flask import Flask, Response, render_template, request
import os
import numpy as np
import psycopg2
from videocapture.stream_dataset import gen_frames, RECOGNIZER
from videocapture.training_models import getImageAndLabels
from videocapture.stream_recognizer import recognizeFace

app = Flask(__name__, static_url_path='/static')


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='face_recognizer_db',
                            user='developer',
                            password='2002')
    return conn


@app.get("/")
def home():
    return render_template("home.html")


@app.route('/stream')
def index():
    return render_template("train-camera.html")


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.post("/input_name")
def input_name():
    username = request.form['username']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""INSERT INTO users(username) VALUES (%s) RETURNING id""", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return render_template("train-camera.html")


@app.get("/input_name")
def get_input_name():
    return render('input_name.html')


def render(key: str):
    return render_template("header.html") + render_template(key) + render_template("footer.html")


@app.route("/train")
def training_face():
    faces, ids = getImageAndLabels("dataset")
    RECOGNIZER.train(faces, np.array(ids))
    if not os.path.exists("trainer"):
        os.makedirs("trainer")
    RECOGNIZER.write("trainer/trainer.yml")
    return "<h1>Faces trained successfully!!!</h1>"


@app.route("/recognize")
def recognize_face():
    return render_template("recognizer.html")


@app.route('/video_recognize')
def video_recognize():
    return Response(recognizeFace(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8080)
