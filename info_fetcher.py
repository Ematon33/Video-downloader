import yt_dlp


def get_formats(url) -> list:
    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)

    all_formats = info.get('formats', [])

    formats_list = []
    for f in all_formats:
        format_info = {
            "format_id": f["format_id"],
            "resolution": f["resolution"],
            "ext": f["ext"],
        }
        formats_list.append(format_info)

    return formats_list
