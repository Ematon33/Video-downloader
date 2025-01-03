import customtkinter as CTk
from tkinter import filedialog


# Class to create the GUI
class GUI(CTk.CTk):
    def __init__(self):
        CTk.CTk.__init__(self)
        self.title("Youtube Downloader")
        self.geometry("400x250")

        self.url_label = CTk.CTkLabel(self, text="Youtube URL:")
        self.url_text_box = CTk.CTkEntry(self)
        self.download_button = CTk.CTkButton(self, text="Download")

        # Dropdown to select file format for download, default is 'mp4'
        self.file_formats = CTk.CTkComboBox(
            self,
            state="readonly",
        )

        self.av_switch = CTk.CTkSwitch(self, text="Video/Audio")
        self.av_switch.pack()

        self.url_label.pack()
        self.url_text_box.pack()
        self.file_formats.pack()
        self.download_button.pack()

        self.progress_bar = CTk.CTkProgressBar(self, width=300)
        self.progress_bar.set(0)  # 0 = 0%
        self.progress_bar.pack(pady=10)

        self.progress_label = CTk.CTkLabel(self, text="")
        self.progress_label.pack(pady=(0, 10))

    def open_save_dialog(self):
        """Opens dialog to save the file"""
        folder_path = filedialog.askdirectory(title="Select folder to save file")
        return folder_path

    def update_progress(self, fraction, eta=""):
        def _update():
            self.progress_bar.set(fraction)
            percent = fraction * 100
            percent_text = f"{percent:.0f}%"
            self.progress_label.configure(text=f"{percent_text}")

        self.after(0, _update)

    def download_finished(self):
        self.progress_label.configure(text="Download finished")
