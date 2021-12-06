import datetime

from pytube import YouTube
import ast

# Input for link
#user_link = input("Please paste your Youtube link here")
LINK = "https://www.youtube.com/watch?v=X40Tr3Q-BvE"

yt = YouTube(LINK)

# Description function
def description(yt_link):
    print(f"Title: {yt_link.title}"
          f"\nViews: {yt_link.views}"
          f"\nLength: {datetime.timedelta(seconds=yt_link.length)}")
    return

# Function to creates dictionary list from fetched streams list
def extract_streams(streams):
    extracted_data = streams.strip("[]").replace('<Stream: ','{"').replace(">","}").split(", ")
    list_of_streams = []
    for stream in extracted_data:
        dict = ast.literal_eval(stream.replace(' ', ', "').replace('=', '":'))
        list_of_streams.append(dict)
    for stream in list_of_streams:
        if stream['type'] == 'video':
            print(f"{list_of_streams.index(stream) + 1}: Quality:{stream['res']}, Type:{stream['type']}, Tag:{stream['itag']}")
        else:
            print(f"{list_of_streams.index(stream) + 1}: Quality:{stream['abr']}, Type:{stream['type']}, Tag:{stream['itag']}")
    return

# Fetch audio streams
def fetch_audio_streams(yt_link):
    fetched_streams = str(yt_link.streams.filter(only_audio=True))
    extract_streams(fetched_streams)
    return

# Fetch video streams
def fetch_video_streams(yt_link):
    fetched_streams = str(yt_link.streams.filter(progressive=True))
    extract_streams(fetched_streams)
    return

#description(yt)
fetch_audio_streams(yt)
fetch_video_streams(yt)