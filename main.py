import gui
import downloader
import os


# Function to download the video and save it to the disk
def download_video_process():
    video_url = app.url_text_box.get()
    downloader.download_video(video_url, app.open_save_dialog())


app = gui.GUI()

app.download_button.configure(command=download_video_process)

app.mainloop()
