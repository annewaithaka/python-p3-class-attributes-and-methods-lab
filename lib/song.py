class Song:
    # Class attributes to track the number of instances and counts by genre and artist
    count = 0
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment the count of Song instances
        Song.count += 1
        
        # Update genre_count dictionary
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        
        # Update artist_count dictionary
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
        
        # Track unique genres and artists
        if not hasattr(Song, 'genres'):
            Song.genres = set()
        Song.genres.add(genre)
        
        if not hasattr(Song, 'artists'):
            Song.artists = set()
        Song.artists.add(artist)

# Example usage for clarity
if __name__ == "__main__":
    # Create Song instances
    Song("99 Problems", "Jay Z", "Rap")
    Song("Halo", "Beyonce", "Pop")
    Song("Smells Like Teen Spirit", "Nirvana", "Rock")
    Song("Out of Touch", "Hall and Oates", "Pop")
    Song("Sara Smile", "Hall and Oates", "Pop")
