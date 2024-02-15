import os
from pydub import AudioSegment
from pytube import YouTube
from pytube.exceptions import PytubeError
from pytube.cli import on_progress

DIR_FILE = os.getcwd()
URL = 'https://www.youtube.com/watch?v=D0KMxRMfwxE'

def download_youtube():
    """
    Download audio from a YouTube video and save it as an mp3 file.

    Args:
    - URL: str, the URL of the YouTube video
    - DIR_FILE: str, the directory where the file will be saved
    - on_progress: function, a callback function to track the download progress

    Returns:
    - True if the download is successful
    - None if there is an error
    """
    try:
        yt = YouTube(URL,on_progress_callback=on_progress)
        audio = yt.streams.filter(only_audio=True).first()
        out_file = audio.download(output_path=DIR_FILE)
        audio = AudioSegment.from_file(out_file)
        new_file = "audio.mp3"
        audio.export(new_file, format="mp3")
        os.remove(out_file)
        return True 
    except PytubeError as yterror:
        print("error - {}".format(yterror))
        return None
    except Exception as e:
        print(print("error - {}".format(e)))
        return None

if __name__ == "__main__":
    status = download_youtube()
    if status is True:
        print("download finalizado com sucesso")
    else:
        print("download falhou")