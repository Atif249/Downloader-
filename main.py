import yt_dlp

def download_video(url):
    ydl_opts = {
        # Best video + best audio merge (audio missing issue fix)
        'format': 'bestvideo[height<=1080]+bestaudio/best',
        
        'outtmpl': '%(title)s.%(ext)s',
        
        # Merge into MP4 (important for audio)
        'merge_output_format': 'mp4',

        # Ensure ffmpeg is used (required for merging)
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'
        }]
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ Download Complete with Audio!")
    except Exception as e:
        print("\n❌ Error:", e)


def main():
    while True:
        print("\n====== Video Downloader ======")
        print("1. Facebook Downloader")
        print("2. YouTube Downloader")
        print("3. TikTok Downloader")
        print("==============================")

        choice = input("Select option (1/2/3): ")

        if choice in ["1", "2", "3"]:
            url = input("Enter video URL: ")
            print("\n⏳ Downloading... Please wait")
            download_video(url)
        else:
            print("❌ Invalid option selected")

        # Repeat / Exit option
        print("\n==============================")
        again = input("Do you want to download another video? (y/n): ").lower()

        if again != 'y':
            print("👋 Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()
