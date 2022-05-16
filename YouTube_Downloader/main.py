from pytube import YouTube
import ffmpeg
import os


BASE_YOUTUBE_URL = "https://www.youtube.com"

def get_video_url_from_user():
    url = input("Donnez l'url de la vidéo YouTube à télécharger: ")
    if not url.lower().startswith(BASE_YOUTUBE_URL):
        print("ERREUR: Vous devez entrer une url YouTube")
        return get_video_url_from_user()
    return url


def get_video_stream_itag_from_user(streams):
    print('CHOIX DES RÉSOLUTIONS')

    
    indx = 1 
    for stream in streams:
        print(f"{indx} - {stream.resolution}")
        indx += 1

    while True:
        res_num = input("Choisissez la résolution: ")
        if res_num == "":
            print("ERREUR: Vous devez rentrer un nombre")
        else:
            try:
                res_num_int = int(res_num)
            except:
                print("ERREUR: Vous devez rentrer un nombre")
            else:
                if not 1 <= res_num_int <= len(streams):
                    print("ERREUR: Vous devez rentrer un nombre entre 1 et", len(streams))
                else:
                    break
    itag = streams[res_num_int-1].itag
    return itag

url = 'https://www.youtube.com/watch?v=WR8Jb2YFCJk'
# url = get_video_url_from_user()



def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize
    print(f'Progression de téléchargement : {int(percent)}%')

youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)

print('Titre: '+ youtube_video.title)
print('Nb vues: ', youtube_video.views)


print("")
print("STREAMS")

streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type='video').order_by('resolution').desc()
video_stream = streams[0]


streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type='audio').order_by('abr').desc()
audio_stream = streams[0]

for stream in streams:
    print(stream)

print("Vidéo stream", video_stream)
print("Audio stream", audio_stream)
# itag = get_video_stream_itag_from_user(streams)


# stream = youtube_video.streams.get_by_itag(itag=299)
print('Téléchargement vidéo...')
video_stream.download("video")
print('OK')

print('Téléchargement audio...')
audio_stream.download("audio")
print('OK')

audio_filename = os.path.join("audio", video_stream.default_filename) 
video_filename = os.path.join("video", video_stream.default_filename) 

output_filename = video_stream.default_filename

print("Combinaison des fichiers...")
# ffmpeg.output(ffmpeg.input(audio_filename), ffmpeg.input(video_filename), output_filename).run() # Pour réencoder les deux fichiers avec les codes par défaut de ffmpeg
ffmpeg.output(ffmpeg.input(audio_filename), ffmpeg.input(video_filename), output_filename, vcodec="copy", acodec="copy", loglevel="quiet").run(overwrite_output=True) # Pour uniquement combiner (copier) les deux fichiers et donc gagner beaucoup de temps
print('OK')
