from SpotifyWrapper import SpotifyWrapper
from ytdlpWrapper import ytdlpWrapper

with open("token.txt") as f:
    token = f.read().splitlines()[0]

spotifyWrapper = SpotifyWrapper(token)
ytdlpWrapper = ytdlpWrapper()


playlist_url = input("変換したいYoutubeプレイリストのURLを入力してください。\n")

playlist_title = ytdlpWrapper.get_playlist_name(playlist_url)
playlist_id = spotifyWrapper.create_playlist(playlist_title)

title_list = ytdlpWrapper.parse_playlist(playlist_url)

for title in title_list:
    try:
        song = spotifyWrapper.search(title, limit=1, offset=1)
        uri = song["tracks"]["items"][0]["uri"]
    
        print(spotifyWrapper.add_track_to_playlist(playlist_id, uri))
    except:
        print("err", title)
  
