import spotipy
from spotipy.oauth2 import SpotifyOAuth


class SpotifyPlaylist:
    def __init__(self):
        self.spotify_client_id = "93a95faa83b344b884cf00a71ba19b8e"
        self.spotify_client_secret = "ab69e418afb240efa8b7f548fac1f037"
        self.redirect_url = "http://example.com"
        self.spotify_playlist_url = "https://api.spotify.com/v1/users/sthbr82/playlists"
        self.sp_handle = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.spotify_client_id,
                                         client_secret=self.spotify_client_secret,
                                         redirect_uri=self.redirect_url,
                                         scope="playlist-modify-private"))
        self.track_ids = ""
        self.playlist_id = ""

    def create_spotify_playlist(self, song_date):
        user_info = self.sp_handle.current_user()
        playlist = self.sp_handle.user_playlist_create(user=user_info["id"], name=f"{song_date} Billboard Top 100", public=False)
        self.playlist_id = playlist["id"]

    def add_songs_to_playlist(self):
        self.sp_handle.playlist_add_items(playlist_id=self.playlist_id, items=self.track_ids)

    def get_track_id(self, tracks, track_date):
        year = track_date.split("-")[0]
        self.track_ids = []
        for song in tracks:
            track_id = self.sp_handle.search(q=f"track: {song} year: {year}")
            try:
                self.track_ids.append(track_id['tracks']['items'][0]['uri'])
            except IndexError:
                print(f"{song} does not exist in Spotify")
