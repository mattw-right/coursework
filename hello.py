

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time



auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

q='hello'

def create_query(title=False, artist=False, album=False, year=False):
    q = ''
    if title:
        q += 'track:' + title
    elif artist:
        q += 'artist:' + artist
    elif album:
        q += 'album:' + album
    elif year:
        q += 'year:' + year
    return q


def search(title=None, year=None, artist=None, album=None, genre=None, type='track', limit=10, market=None, offset=0, error_catch=10):
    i = 0
    while True:
        try:
            results = sp.search(create_query(title=title, artist=artist, album=album, year=year), limit=limit, offset=offset, type=type, market=market)
            break
        except:
            i += 1
            time.sleep(1)
            print('Trouble connecting. Trying again')
            if i>10:
                break
    return results

limit = 3




class API_return_parser:

    def __init__(self, raw_body):
        self.body = raw_body

    def return_track_name(self, result_index=0):
        '''Returns the name of the track at index result_index'''
        return self.body['tracks']['items'][result_index]['name']

    def return_track_uri(self, result_index=0):
        return self.body['tracks']['items'][result_index]['uri']

    def return_first_artist_name(self, result_index=0):
        return self.body['tracks']['items'][result_index]['artists'][0]['name']

    def return_all_artists(self, result_index=0):
        return self.body['tracks']['items'][result_index]['artists']

    def return_first_artist_uri(self, result_index=0):
        return self.body['tracks']['items'][result_index]['artists'][0]['uri']

    def return_album_name(self, result_index=0):
        return self.body['tracks']['items'][result_index]['album']['name']

    def return_album_uri(self, result_index=0):
        return self.body['tracks']['items'][result_index]['album']['uri']

    def return_release_date(self, result_index=0):
        return self.body['tracks']['items'][result_index]['album']['release_date']

    def return_preview_url(self, result_index=0):
        return str(self.body['tracks']['items'][result_index]['preview_url'])

    def return_cover_art_url(self, result_index=0):
        return self.body['tracks']['items'][result_index]['album']['images'][0]['url']


r = search(title=input(), limit=limit)

r = API_return_parser(r)

print(r.return_cover_art_url())


'''
redirect uri = http://127.0.0.1:9090


export SPOTIPY_CLIENT_ID='3cfe7e53e98a4e8b99785159a125ef91'
export SPOTIPY_CLIENT_SECRET='8eea3e2665d9460fa3cd46f516e0890b'
export SPOTIPY_REDIRECT_URI='http://127.0.0.1:9090'
export FLASK_APP=main.py

'''
