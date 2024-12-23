import yt_dlp


# Download the video from the given URL from youtube
def download_best_quality(video_url):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",  # Best video and audio
        "merge_output_format": "mp4",  # Output format
        "outtmpl": "%(title)s.%(ext)s",  # Output destination
        "audioquality": "0",  # Highest quality
        "windowsfilenames": True,  # Protect file names on Windows
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
