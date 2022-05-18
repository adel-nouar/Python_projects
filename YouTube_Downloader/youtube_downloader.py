from pytube import YouTube
import ffmpeg
import os





def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = 100 * (bytes_downloaded / float(stream.filesize))
    bar = '█' * int(percent) + '' * (100 - int(percent))
    # print(f'Progression de téléchargement : {int(percent)}%')
    print(f"\r|{bar}| {percent:.2f}%", end="\r")


def download_video(url):
    youtube_video = YouTube(url)

    youtube_video.register_on_progress_callback(on_download_progress)

    # print('Titre: '+ youtube_video.title)
    # print('Nb vues: ', youtube_video.views)


    # print("")
    # print("STREAMS")

    streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type='video').order_by('resolution').desc()
    video_stream = streams[0]


    streams = youtube_video.streams.filter(progressive=False, file_extension='mp4', type='audio').order_by('abr').desc()
    audio_stream = streams[0]

    # for stream in streams:
    #     print(stream)

    # print("Vidéo stream", video_stream)
    # print("Audio stream", audio_stream)
    # itag = get_video_stream_itag_from_user(streams)


    # stream = youtube_video.streams.get_by_itag(itag=299)

    print(f'Téléchargement {youtube_video.title}...')
    print('Téléchargement vidéo...')
    video_stream.download("video")

    print(f'Téléchargement audio...')
    audio_stream.download("audio")

    audio_filename = os.path.join("audio", video_stream.default_filename) 
    video_filename = os.path.join("video", video_stream.default_filename) 

    output_filename = video_stream.default_filename

    # print("Combinaison des fichiers...")
    # ffmpeg.output(ffmpeg.input(audio_filename), ffmpeg.input(video_filename), output_filename).run() # Pour réencoder les deux fichiers avec les codes par défaut de ffmpeg
    ffmpeg.output(ffmpeg.input(audio_filename), ffmpeg.input(video_filename), output_filename, vcodec="copy", acodec="copy", loglevel="quiet").run(overwrite_output=True) # Pour uniquement combiner (copier) les deux fichiers et donc gagner beaucoup de temps
    print('OK')
    os.remove(audio_filename)
    os.remove(video_filename)
    os.rmdir("audio")
    os.rmdir("video")
