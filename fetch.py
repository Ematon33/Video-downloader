from ast import While
import yt_dlp
import time
import utilites

# Global variable to check if the download is cancelled
cancel_requested = False


# Cancel the download
def cancel_fetch():
    """Cancel the download"""
    global cancel_requested
    cancel_requested = True


# Download the video from the given URL from youtube
def fetch_video(video_url, filepath, ydl_opts, progress_callback=None):

    def progress_hook(d):
        """
        Progress hook for the download
        """
        # Check if the download is cancelled
        if cancel_requested:
            raise KeyboardInterrupt("Download aborted by user.")

        if d["status"] == "downloading":
            downloaded = d.get("downloaded_bytes", 0)
            total = d.get("total_bytes") or d.get("total_bytes_estimate") or 1
            fraction = downloaded / total

            if progress_callback:
                progress_callback(fraction, "downloading")

        # Handle postprocessor (conversion) progress

        elif d["status"] == "processing" or d["status"] == "started":
            if progress_callback:
                progress_callback(1.0, "converting (please wait)")
                time.sleep(0.5)
                progress_callback(1.0, "converting. (please wait)")
                time.sleep(0.5)
                progress_callback(1.0, "converting.. (please wait)")
                time.sleep(0.5)
                progress_callback(1.0, "converting... (please wait)")
                time.sleep(0.5)

        elif d["status"] == "finished":
            if progress_callback:
                progress_callback(1.0, "finished")

    ydl_opts.update(
        {
            "outtmpl": f"{filepath}/%(title)s.%(ext)s",  # Output destination
            "audioquality": "0",  # Highest quality
            "windowsfilenames": True,  # Protect file names on Windows
            "addmetadata": True,  # Add metadata to the video
            "progress_hooks": [progress_hook],  # Progress hook
            "postprocessor_hooks": [progress_hook],  # Postprocessor hook
            "ffmpeg_location": "essentials\\ffmpeg.exe",  # Path to ffmpeg
        }
    )

    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
        except KeyboardInterrupt:
            print("Download aborted by user.")
        finally:
            global cancel_requested
            cancel_requested = False
