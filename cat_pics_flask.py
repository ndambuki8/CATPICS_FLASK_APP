from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

def get_meme():
    url = "https://api.thecatapi.com/v1/images/search?format=json"
    response = json.loads(requests.request("GET", url).text)
    # print(type(response))
    # print(response)
    img = response[0]
    img = img.get("url")
    return img

@app.route("/")
def index():
    meme_pic = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic)

app.run(host="0.0.0.0", port=5000)