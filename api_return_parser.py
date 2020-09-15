import pandas as pd

class API_return_parser_track:

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
        print(str(self.body['tracks']['items'][result_index]['preview_url']))
        return str(self.body['tracks']['items'][result_index]['preview_url'])

    def return_cover_art_url(self, result_index=0):
        return self.body['tracks']['items'][result_index]['album']['images'][0]['url']

    def to_table(self):
        df = pd.DataFrame(columns = ['Track Name', 'Artist', 'Album', 'Preview URL', 'Cover Art URL'])
        for i in range(len(self.body['tracks']['items'])):
            df.loc[i] = [self.return_track_name(result_index=i), self.return_first_artist_name(result_index=i), self.return_album_name(result_index=i), self.return_preview_url(result_index=i), self.return_cover_art_url(result_index=i)]
        return df






class API_return_parser_album:

    def __init__(self, raw_body):
        self.body = raw_body

    def r(self):
        return self.body
