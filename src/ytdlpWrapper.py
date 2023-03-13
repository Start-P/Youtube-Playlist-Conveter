import requests
from bs4 import BeautifulSoup
from yt_dlp import YoutubeDL

class ytdlpWrapper():
    
    def get_playlist_name(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.find("meta", attrs={"property": "og:title"})["content"]
    
    def parse_playlist(self, url):
        with YoutubeDL() as ydl:
            results = ydl.extract_info(url, download=False)
            title_list = []
            for result in results["entries"]:
                title_list.append(result["title"])

        return title_list