import yt_dlp

def Download(link):
    try:
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        print("Download completed successfully")
    except Exception as e:
        print(f"An error has occurred: {e}")

link = input("Link : ")
Download(link)