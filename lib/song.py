

class Song:

    all = []

    song_count = 4
    genres = set()
    artists= set()
    genre_count={}
    artist_count={}


    def __init__(self, name,artist,genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genres.add(genre)
        Song.artists.add(artist)

        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        if artist in Song.artist_count:
            Song.artist_count[artist] +=1
        else:
            Song.artist_count[artist] = 1