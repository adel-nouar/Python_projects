from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')

for url in p.video_urls[:3]:
    print(url)