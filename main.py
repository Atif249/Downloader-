import yt_dlp
import os
import time
import sys
import subprocess

# 🎨 Colors
class C:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


# 🔊 SOUND (safe for all systems)
def play_sound():
    print('\a')  # simple beep (no error)


# 🔄 AUTO UPDATE
def auto_update():
    try:
        print(C.YELLOW + "🔄 Checking for updates..." + C.END)

        result = subprocess.run(
            ["git", "pull"],
            capture_output=True,
            text=True
        )

        if "Already up to date" in result.stdout:
            print(C.GREEN + "✅ Latest version" + C.END)
        else:
            print(C.CYAN + "🚀 Updating..." + C.END)
            print(result.stdout)
            print("♻ Restarting...\n")
            os.execv(sys.executable, ['python'] + sys.argv)

    except:
        print(C.RED + "⚠ Auto update failed" + C.END)


# 🔥 INTRO
def intro():
    os.system('cls' if os.name == 'nt' else 'clear')

    title = """
 ██╗   ██╗████████╗
 ╚██╗ ██╔╝╚══██╔══╝
  ╚████╔╝    ██║
   ╚██╔╝     ██║
    ██║      ██║
    ╚═╝      ╚═╝

 ████████╗██╗  ██╗
 ╚══██╔══╝██║ ██╔╝
    ██║   █████╔╝ 
    ██║   ██╔═██╗ 
    ██║   ██║  ██╗
    ╚═╝   ╚═╝  ╚═╝

     YT • FB • TK DOWNLOADER
          By Atif 🚀
"""

    print(C.CYAN + C.BOLD)
    print(title.center(80))
    print(C.END)

    spinner = ['|', '/', '-', '\\']
    for i in range(15):
        sys.stdout.write("\r" + C.CYAN + "Loading " + spinner[i % 4] + C.END)
        sys.stdout.flush()
        time.sleep(0.1)

    print("\n" + C.GREEN + "✔ Ready!\n" + C.END)


# 📊 PROGRESS BAR
def progress_hook(d):
    if d['status'] == 'downloading':
        percent_str = d.get('_percent_str', '0%').strip()

        try:
            percent = float(percent_str.replace('%', '').strip())
        except:
            percent = 0

        bar_length = 30
        filled = int(bar_length * percent / 100)
        bar = '█' * filled + '░' * (bar_length - filled)

        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')

        print(
            f"\r{C.CYAN}📥 [{bar}] {percent:.1f}% | ⚡ {speed} | ⏳ {eta}{C.END}",
            end=''
        )

    elif d['status'] == 'finished':
        print(C.GREEN + "\n✔ Download Finished!" + C.END)
        play_sound()


# 📥 DOWNLOAD FUNCTION
def download_video(url):
    start_time = time.time()

    home = os.path.expanduser("~")
    folder = os.path.join(home, "Atif Downloader")

    if not os.path.exists(folder):
        os.makedirs(folder)

    ydl_opts = {
        'format': 'bestvideo[height<=1080]+bestaudio/best',
        'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'progress_hooks': [progress_hook],
        'js_runtimes': {'node': {}},  # ✅ FIXED
    }

    try:
        print(C.YELLOW + "\n⏳ Starting Download...\n" + C.END)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        end_time = time.time()
        total_time = round(end_time - start_time, 2)

        print(C.GREEN + f"\n✅ Completed in {total_time} seconds!" + C.END)
        print(C.CYAN + f"📁 Saved in: {folder}" + C.END)

        play_sound()

    except Exception as e:
        print(C.RED + "\n❌ Error: " + str(e) + C.END)


# 📋 MENU
def menu():
    print(C.BOLD + "\n========= MENU =========" + C.END)
    print("1. Facebook")
    print("2. YouTube")
    print("3. TikTok")
    print("========================")


# 🚀 MAIN
def main():
    auto_update()
    intro()

    while True:
        menu()
        choice = input(C.CYAN + "\nSelect option (1/2/3): " + C.END).strip()

        if choice in ["1", "2", "3"]:
            url = input("Enter video URL: ").strip()

            if not url:
                print(C.RED + "❌ URL empty" + C.END)
                continue

            download_video(url)

        else:
            print(C.RED + "❌ Invalid option" + C.END)

        again = input(C.YELLOW + "\nDownload another? (y/n): " + C.END).lower()

        if again != 'y':
            print(C.GREEN + "\n👋 Goodbye Atif Boss!" + C.END)
            break


if __name__ == "__main__":
    main()
