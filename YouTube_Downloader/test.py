# Prérequis: installer la librairie pytube, 2 méthodes possibles:
# 1) # Peut-être pas la dernière version
#       pip install pytube 
# 2) Dernière version à partir du github
#       python -m pip install git+https://github.com/pytube/pytube
from pytube import YouTube

# Contiendra l'url de la vidéo YouTube
url_video_youtube = ''

# On crée l'objet à partir de l'url
video_youtube = YouTube(url_video_youtube)

# Récupération du stream ayant la meilleure résolution
# par défaut, et généralement cette résolution est à 720p max
stream = video_youtube.streams.get_highest_resolution()


# Lancement du téléchargement de la vidéo
stream.download()

