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
    videosSearch = VideosSearch(query, limit = 20)
    videosResult =  await videosSearch.next()
    #print(videosResult["result"])
    complete_data = []
    print(len(videosResult["result"]))
    for i in range(0,len(videosResult["result"])):
        title = videosResult["result"][i]["accessibility"]["title"]
        video_id = videosResult["result"][i]["id"]
        preview = f"https://www.youtube.com/embed/{video_id}"
        data = {"title":title,"preview":preview}
        complete_data.append(data)

    
    
    #print(video_search_results["result"])
    return {"data":complete_data}

if __name__ == "__main__":
    app.run(port=8000,debug=True)   