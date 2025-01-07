import gui
import downloader
import threading
import file_formats


# Function to download the video and save it to the disk
def download_video_process():
    video_url = app.url_text_box.get()
    folder_path = app.open_save_dialog()

    yt_options = file_formats.get_yt_options(app.av_switch.get(), app.file_formats.get())

    # If the user has provided a URL and a folder path, start the download
    if folder_path and video_url:
        # Start the download in a separate thread
        t = threading.Thread(
            target=downloader.download_video, args=(video_url, folder_path, yt_options, app.update_progress)
        )
        t.start()


def switch_event():
    """
    This function is called whenever the audio/video switch changes.
    It sets the available values in the ComboBox, chooses a default format,
    and fetches the appropriate yt_options from the 'options' module.
    """
    audio_video_switch = app.av_switch.get()

    if audio_video_switch:
        app.file_formats.configure(values=file_formats.AUDIO_FORMATS)
        app.file_formats.set(file_formats.AUDIO_FORMATS[0])

    else:
        app.file_formats.configure(values=file_formats.VIDEO_FORMATS)
        app.file_formats.set(file_formats.VIDEO_FORMATS[0])

    selected_format = app.file_formats.get()
    yt_options = file_formats.get_yt_options(audio_video_switch, selected_format)

    return yt_options


app = gui.GUI()

# Attach switch_event to the switch
app.av_switch.configure(command=switch_event)
# Call it once so that yt_options is initialized right away
yt_options = switch_event()

# Download button
app.download_button.configure(command=download_video_process)

app.mainloop()
