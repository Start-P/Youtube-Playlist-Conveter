import requests


class SpotifyWrapper:
    def __init__(self, token: str):
        self.host = "https://api.spotify.com/v1"
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': token,
        }

    def get_user_id(self):
        response = requests.get(self.host + '/me', headers=self.headers)
        return response.json()["id"]
        
    def create_playlist(self, name):
        user_id = self.get_user_id()
        data = {
            "name": name,
            "public": False,
            "description": "Created by Start_P's Spotify Playlist Converter."
        }
        
        response = requests.post(self.host + f'/users/{user_id}/playlists', json=data, headers=self.headers)
        return response.json()["id"]

    def add_track_to_playlist(self, id, uri):
        data = {
            "position": "0",
            "uris": uri,
        }
        
        response = requests.post(self.host + f'/playlists/{id}/tracks', json=data, params=data, headers=self.headers)
        return response.json()

    def search(self, query: str, type: str = "track", market: str = "JP", limit: str = "10", offset: str = "5"):
        params = {
            'q': query,
            'type': type,
            'market': market.upper(),
            'limit': limit,
            'offset': offset,
        }

        response = requests.get(self.host + '/search', params=params, headers=self.headers)
        result = response.json()
        return result