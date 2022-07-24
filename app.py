from flask import Flask, jsonify
from pytube import YouTube


app = Flask(__name__)

@app.route("/user", methods = ['GET'])
def yt():
    url = 'https://www.youtube.com/watch?v=7BXJIjfJCsA'

    my_video = YouTube(url)
    print(my_video.title)
    print(my_video.thumbnail_url)

    my_video = my_video.streams.get_highest_resolution()
    video = my_video.download()
    print("downloaded!")

    return jsonify({"getUrl":video})


if __name__ == "__main__":
    app.run()




