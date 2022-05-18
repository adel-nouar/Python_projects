import youtube_downloader
from pytube import Playlist



if __name__ == "__main__":
    urls = []
    with open("test.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("https://www.youtube.com/playlist?"):
                urls.extend(Playlist(line).video_urls[:3])
            elif line.startswith("https://www.youtube.com/"):
                urls.append(line)
            else:
                continue


# p = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')

# urls = ('https://www.youtube.com/watch?v=WR8Jb2YFCJk',
# 'https://youtu.be/ZA-tUyM_y7s', 'https://www.youtube.com/watch?v=CHhwJjR0mZA')

print(urls)
for url in urls:
    youtube_downloader.download_video(url)