from pytube import YouTube
import datetime


# Input for link
#user_link = input("Please paste your Youtube link here")
LINK = "https://www.youtube.com/watch?v=QAg1a9RlHPs"

yt = YouTube(LINK)

def description(link_yt):
    print(f"Title: {link_yt.title}"
          f"\nViews: {link_yt.views}"
          f"\nLength: {datetime.timedelta(seconds=link_yt.length)}")

    return

description(yt)



# Details of link
# print("Title: ", yt.title, "\n")
# print("Number of views: ", yt.views, "\n")
# print("Length of video: ", yt.length, "seconds \n")
# print("Description: ", yt.description, "\n")
# print("Ratings: ", yt.rating, "\n")
#title(yt)
#print(type(yt.streams))
#print(yt.streams.get_highest_resolution())
#print(yt.streams.get_by_itag(yt.streams.get_audio_only().itag))
#ys = yt.streams.get_by_itag('22')
#ys.download()
