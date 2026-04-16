import yt_dlp
import os
import time
import sys

# 🎨 Colors
class C:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


# 🔥 Professional Intro (Perfect Size)
def intro():
    os.system('cls' if os.name == 'nt' else 'clear')

    title = r"""
   ██╗   ██╗████████╗    ███████╗██████╗ 
   ╚██╗ ██╔╝╚══██╔══╝    ██╔════╝██╔══██╗
    ╚████╔╝    ██║       █████╗  ██████╔╝
     ╚██╔╝     ██║       ██╔══╝  ██╔══██╗
      ██║      ██║       ██║     ██████╔╝
      ╚═╝      ╚═╝       ╚═╝     ╚═════╝  

        TK • FB • YT DOWNLOADER
"""

    print(C.CYAN + C.BOLD)
    print(title.center(80))
    print(C.END)

    print(C.YELLOW + "Starting Atif Downloader..." + C.END)

    spinner = ['|', '/', '-', '\\']
    for i in range(20):
        sys.stdout.write("\r" + C.CYAN + "Loading " + spinner[i % 4] + C.END)
        sys.stdout.flush()
        time.sleep(0.1)

    print("\n" + C.GREEN + "✔ Ready to Use!\n" + C.END)
    time.sleep(1)


# 📥 Download Function
def download_video(url):
    home = os.path.expanduser("~")
    folder = os.path.join(home, "Atif Downloader")

    if not os.path.exists(folder):
        os.makedirs(folder)

    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best',
        'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
    }

    try:
        print(C.YELLOW + "\n⏳ Downloading..." + C.END)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print(C.GREEN + "\n✅ Download Complete!" + C.END)
        print(C.CYAN + f"📁 Saved in: {folder}" + C.END)

    except Exception as e:
        print(C.RED + "\n❌ Error: " + str(e) + C.END)


# 📋 Menu
def menu():
    print(C.BOLD + "\n========= MENU =========" + C.END)
    print("1. Facebook Downloader")
    print("2. YouTube Downloader")
    print("3. TikTok Downloader")
    print("========================")


# 🚀 Main Program
def main():
    intro()

    while True:
        menu()
        choice = input(C.CYAN + "\nSelect option (1/2/3): " + C.END).strip()

        if choice in ["1", "2", "3"]:
            url = input("Enter video URL: ").strip()

            if url == "":
                print(C.RED + "❌ URL cannot be empty" + C.END)
                continue

            download_video(url)

        else:
            print(C.RED + "❌ Invalid option selected" + C.END)

        again = input(C.YELLOW + "\nDownload another video? (y/n): " + C.END).lower().strip()

        if again != 'y':
            print(C.GREEN + "\n👋 Thanks for using ATIF DOWNLOADER!" + C.END)
            break


if __name__ == "__main__":
    main()
