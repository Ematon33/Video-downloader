import select
import gui
import fetch
import threading
import info_fetcher


def cancel_download_process():
    """Cancel the download"""
    fetch.cancel_fetch()


# Function to download the video and save it to the disk
def download_video_process():
    video_url = app.url_text_box.get()
    folder_path = app.open_save_dialog()

    selected_format = app.format_map[app.file_formats.get()]

    yt_options = {
        "format": selected_format,
    }

    # If the user has provided a URL and a folder path, start the download
    if folder_path and video_url:
        # Start the download in a separate thread
        t = threading.Thread(target=fetch.fetch_video, args=(video_url, folder_path, yt_options, app.update_progress))
        t.start()

def list_formats(event=None):
    formats = info_fetcher.get_formats(app.url_text_box.get())

    app.format_map = {
        f"{format['resolution']} - {format['ext']}": format['format_id']
        for format in formats
    }

    app.file_formats.configure(values=list(app.format_map.keys()))

app = gui.GUI()

app.url_text_box.bind("<KeyRelease>", list_formats)

# Download button
app.download_button.configure(command=download_video_process)

app.cancel_button.configure(command=cancel_download_process)

app.mainloop()
