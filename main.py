import yt_dlp
import os

def download_video(url):
    # Home directory path
    home = os.path.expanduser("~")

    # Folder path
    folder = os.path.join(home, "Atif Downloader")

    # Agar folder exist nahi karta to bana do
    if not os.path.exists(folder):
        os.makedirs(folder)

    ydl_opts = {
        # Best video + audio
        'format': 'bestvideo[height<=1080]+bestaudio/best',

        # Save inside folder
        'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),

        # Merge into mp4
        'merge_output_format': 'mp4',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(f"\n✅ Download Complete!")
        print(f"📁 Saved in: {folder}")

    except Exception as e:
        print("\n❌ Error:", e)


def main():
    while True:
        print("\n====== Video Downloader ======")
        print("1. Facebook Downloader")
        print("2. YouTube Downloader")
        print("3. TikTok Downloader")
        print("==============================")

        choice = input("Select option (1/2/3): ").strip()

        if choice in ["1", "2", "3"]:
            url = input("Enter video URL: ").strip()

            if url == "":
                print("❌ URL cannot be empty")
                continue

            print("\n⏳ Downloading... Please wait")
            download_video(url)

        else:
            print("❌ Invalid option selected")

        print("\n==============================")
        again = input("Download another video? (y/n): ").lower().strip()

        if again != 'y':
            print("👋 Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()
