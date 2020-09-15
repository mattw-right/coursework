
from api_call import create_api_call
from api_return_parser import API_return_parser_track, API_return_parser_album
from flask import Flask
from flask import render_template, request
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('search_page.html')

@app.route('/', methods=['POST'])
def search():
    query = request.form['search']
    type = 'track'
    track, year, artist, album, genre = None, None, None, None, None
    if type == 'track': track=query
    elif type == 'year': year=query
    elif type == 'artist': artist=query
    elif type == 'album': album=query
    elif type == 'genre': genre=query
    r = create_api_call(track=track, year=year, artist=artist, album=album, genre=genre, type=type)
    r = API_return_parser_track(r)
    return render_template("results.html", results=r.to_table().values.tolist())
    #return render_template("results.html", data=r.to_table().to_html())
    '''try:
        #return render_template('search_page.html', artist_name = r.return_first_artist_name(), song_url=r.return_preview_url(), album_name=r.return_album_name(), image_url=r.return_cover_art_url(), release_date=r.return_release_date(), song_title=r.return_track_name())
    except Exception as e:
        print(e)
        return render_template('search_page.html', artist_name = "Oops, we couldn't find that title. Check your spelling and try again")
    pass'''

#do drop down box to select type
