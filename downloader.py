import yt_dlp


# Download the video from the given URL from youtube
def download_video(video_url, filepath):
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",  # Best video and audio
        "merge_output_format": "mp4",  # Output format
        "outtmpl": f"{filepath}/%(title)s.%(ext)s",  # Output destination
        "audioquality": "0",  # Highest quality
        "windowsfilenames": True,  # Protect file names on Windows
        "addmetadata": True,  # Add metadata to the video
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
