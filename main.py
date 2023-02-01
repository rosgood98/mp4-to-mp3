from moviepy.editor import VideoFileClip
from pytube import YouTube

def main():
    link = input("Enter YouTube link: ")
    mp3 = "audio.mp3"

    fileName = Download(link)

    video = VideoFileClip(fileName)
    audio = video.audio

    audio.write_audiofile(mp3)

    audio.close()
    video.close()
    print("Conversion Finished.")

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_lowest_resolution()

    try:
        youtubeObject.download()
    except:
        print("An error has occurred")

    print("Download is completed successfully")
    return youtubeObject.default_filename

main()