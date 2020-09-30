

from download_track import download_track

class Listener_Profile:

    def __init__(self, likes, dislikes):
        '''Input dictionaries in the form {track_name : preview_url} for the liked and disliked tracks of the user'''
        self.likes = likes
        self.dislikes = dislikes
        self.likes_url = list(likes.values())
        self.dislikes_url = list(dislikes.values())
        self.likes_names = list(likes.keys())
        self.dislikes_names = list(dislikes.keys())

    def download_tracks(self):
        errors = []
        for i in self.likes_names:
            try:
                download_track(i, self.likes[i])
            except:
                errors.append(i)
        for i in self.dislikes_names:
            try:
                download_track(i, self.dislikes[i])
            except:
                errors.append(i)
        return True, errors


    def create_listener_profile(self):
        self.likes_fouriers = []
        self.dislikes_fouriers = []
        for i in self.likes_names:
            self.likes_fouriers.append([float(i) for i in open('./fouriers/' + i + '.txt').read().split('\n')[:-1]])
        for i in self.dislikes_names:
            self.dislikes_fouriers.append([float(i) for i in open('./fouriers/' + i + '.txt').read().split('\n')[:-1]])

        positives = [0]*len(self.likes_fouriers[0])
        for i in self.likes_fouriers:
            positives = [x + y for x, y in zip(i, positives)]

        negatives = [0]*len(self.dislikes_fouriers[0])
        for i in self.dislikes_fouriers:
            negatives = [x + y for x, y in zip(i, negatives)]

        positives = [x / len(self.likes_names) for x in positives]
        negatives = [x / -1*len(self.dislikes_names) for x in negatives]

        self.listener_profile = [x + y for x, y in zip(positives, negatives)]

        return self.listener_profile


#python listener_profile.py
