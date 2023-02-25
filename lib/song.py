class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre,):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)



    @classmethod
    def add_song_to_count(cls, increment=1):
      cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        result = cls.genres.count(genre)
        if result > 0:
            print("the genre is already added to the list")
        else:
           cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        result = cls.artists.count(artist)
        if result > 0:
            print("the artist is already added to the list")
        else:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        #iterate through genres list, create a dictionary with key/value pairs
        if cls.genre_count.get(genre):
                cls.genre_count[genre] += 1
        else:
                cls.genre_count[genre] = 1  


    @classmethod
    def add_to_artist_count(cls, artist):
        #iterate through artist list, create a dictionary with key/value pairs
        if cls.artist_count.get(artist):
                cls.artist_count[artist] += 1
        else:
                cls.artist_count[artist] = 1  

