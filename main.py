from flask import Flask, render_template
import os

app = Flask(__name__)

PHOTO_FOLDER = "static/photos"
VIDEO_FOLDER = "static/videos"

TEXT_POSTS = [
    "What better way to capture a city old and new than to write an old-fashioned travel diary through the new(?)-fashioned blog post?",
    "And of course, its not me if I dont spend 10 days making the most basic website when I could've spent 10 minutes uploading the photos to Google Photos!",
    "So, that said, enjoy Paris through my eyes (and lens)!",
]

@app.route("/")
def index():
    photos11 = os.listdir(PHOTO_FOLDER + "/photos11")
    photos12 = os.listdir(PHOTO_FOLDER + "/photos12")
    photos2 = os.listdir(PHOTO_FOLDER + "/photos2")
    photos3 = os.listdir(PHOTO_FOLDER + "/photos3")
    videos1 = os.listdir(VIDEO_FOLDER + "/videos1")
    videos2 = os.listdir(VIDEO_FOLDER + "/videos2")

    return render_template(
        "index.html",
        photos11=photos11,
        photos12=photos12,
        photos2 = photos2,
        photos3 = photos3,
        videos1=videos1,
        videos2=videos2,
        texts=TEXT_POSTS
    )

if __name__ == "__main__":
    app.run(debug=True)
