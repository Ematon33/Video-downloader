import gui
import downloader
import threading


# Function to download the video and save it to the disk
def download_video_process():
    video_url = app.url_text_box.get()

    folder_path = app.open_save_dialog()

    file_format = app.file_formats.get()

    yt_options = {
        "merge_output_format": file_format,  # Output format
    }

    t = threading.Thread(
        target=downloader.download_video, args=(video_url, folder_path, yt_options, app.update_progress)
    )
    t.start()


def switch_event():
    audio_video_switch = app.av_switch.get()

    if audio_video_switch:
        app.file_formats.configure(values=["mp3"])
        app.file_formats.set("mp3")
    else:
        app.file_formats.configure(values=["mp4", "webm", "mkv"])
        app.file_formats.set("mp4")


app = gui.GUI()

app.av_switch.configure(command=switch_event)
switch_event()

app.download_button.configure(command=download_video_process)

app.mainloop()
