from flask import Flask
from flask_cors import CORS, cross_origin
from youtubesearchpython.__future__ import VideosSearch
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/app/test",methods=["GET"])
def test_reply():
    return {"messgage":"Suscess"}

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/search/<query>')
async def Search(query):
    videosSearch = VideosSearch(query, limit = 2)
    videosResult =  await videosSearch.next()
    print(videosResult["result"])
    title = videosResult["result"][0]["accessibility"]["title"]
    video_id = videosResult["result"][0]["id"]
    preview = f"https://www.youtube.com/embed/{video_id}"
    #print(video_search_results["result"])
    return {"title":title,"preview":preview}

if __name__ == "__main__":
    app.run(port=8000,debug=True)   