from bs4 import BeautifulSoup
import requests


class BillBoardTop100:
    def __init__(self):
        self.soup = ""
        self.songs = ""
        self.date = ""
        self.URL = ""

    def get_top_100_songs(self):
        self.date = input("Which year you want to go back to?\n"
                     "Enter in YYYY-MM-DD format?\n")
        self.URL = f"https://www.billboard.com/charts/hot-100/{self.date}"
        response = requests.get(self.URL)
        billboard_top_100 = response.text

        self.soup = BeautifulSoup(billboard_top_100, "html.parser")

        song_list = self.soup.select("ul li h3")
        # artist_list = soup.select("ul li span")

        self.songs = [f"{song.getText().strip("\n\t\r")}" for song in song_list]
        # artists = [f"{artist.getText().strip("\n\t\r")}" for artist in artist_list]
        self.songs = self.songs[:100]
        return self.songs
