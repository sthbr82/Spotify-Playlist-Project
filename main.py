from billboard_top_100 import BillBoardTop100
from spotify_pl import SpotifyPlaylist


if __name__ == "__main__":
    billboard = BillBoardTop100()
    songs = billboard.get_top_100_songs()

    spotify_obj = SpotifyPlaylist()
    spotify_obj.get_track_id(songs, billboard.date)
    spotify_obj.create_spotify_playlist(billboard.date)
    spotify_obj.add_songs_to_playlist()







