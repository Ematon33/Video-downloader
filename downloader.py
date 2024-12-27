import yt_dlp

# Download the video from the given URL from youtube
def download_video(video_url, filepath, progress_callback=None):

    def progress_hook(d):
        ''' 
        Progress hook for the download 
        '''
        if d['status'] == 'downloading':
            downloaded = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes') or d.get('total_bytes_estimate') or 1
            fraction = downloaded / total 

            if progress_callback:
                progress_callback(fraction)

        elif d['status'] == 'finished':
            if progress_callback:
                progress_callback(1.0, "finished")

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",  # Best video and audio
        "merge_output_format": "mp4",  # Output format
        "outtmpl": f"{filepath}/%(title)s.%(ext)s",  # Output destination
        "audioquality": "0",  # Highest quality
        "windowsfilenames": True,  # Protect file names on Windows
        "addmetadata": True,  # Add metadata to the video

        "progress_hooks": [progress_hook], # Progress hook
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
