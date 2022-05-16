import youtube_downloader
from pytube import Playlist



p = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')

urls = ('https://www.youtube.com/watch?v=WR8Jb2YFCJk',
'https://youtu.be/ZA-tUyM_y7s', 'https://www.youtube.com/watch?v=CHhwJjR0mZA')


for url in urls:
    youtube_downloader.download_video(url)