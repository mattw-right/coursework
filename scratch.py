

from api_call import create_api_call
from api_return_parser import API_return_parser_track, API_return_parser_album
from create_fourier import create_fourier

tracks = ['psycho killer']

for track in tracks:
    try:
        r = create_api_call(track=track)
        r = API_return_parser_track(r)
        create_fourier(r.return_track_name(), r.return_preview_url())
    except:
        print(track)
