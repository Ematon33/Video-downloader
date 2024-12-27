import gui
import downloader
import threading


# Function to download the video and save it to the disk
def download_video_process():
    video_url = app.url_text_box.get()

    folder_path = app.open_save_dialog()

    t = threading.Thread(
        target=downloader.download_video,
        args=(video_url, folder_path, app.update_progress)
    )
    t.start()

app = gui.GUI()

app.download_button.configure(command=download_video_process)

app.mainloop()
