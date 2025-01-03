import copy

AUDIO_FORMATS = ["mp3"]
VIDEO_FORMATS = ["mp4", "webm", "mkv"]

# Base settings for AUDIO
AUDIO_OPTIONS = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

# Base settings for VIDEO
VIDEO_OPTIONS = {
    "format": "bestvideo+bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mp4",
        }
    ],
}


def get_yt_options(audio_video_switch: bool, selected_format: str) -> dict:
    """
    Generates the youtube-dl/yt-dlp options based on whether
    the user chose audio only (audio_video_switch = True) or
    video (audio_video_switch = False), and the selected format.
    """

    if audio_video_switch:
        # Work with AUDIO_OPTIONS
        yt_opts = copy.deepcopy(AUDIO_OPTIONS)
        # Dynamically overwrite the preferred codec according to the selected format (e.g., mp3)
        yt_opts["postprocessors"][0]["preferredcodec"] = selected_format

    else:
        # Work with VIDEO_OPTIONS
        yt_opts = copy.deepcopy(VIDEO_OPTIONS)

        # Dynamically set the format/codec depending on what the user chose:
        if selected_format == "mp4":
            yt_opts["postprocessors"][0]["preferedformat"] = selected_format
        elif selected_format == "webm":
            yt_opts["postprocessors"][0]["preferedformat"] = selected_format
        elif selected_format == "mkv":
            yt_opts["postprocessors"][0]["preferedformat"] = selected_format

    return yt_opts
