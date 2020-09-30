

from create_fourier import create_fourier

def download_track(track_name, preview_url):
    try:
        create_fourier(track_name, preview_url)
        return True
    except:
        return False
