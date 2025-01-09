import customtkinter as CTk
from tkinter import filedialog
import time


# Class to create the GUI
class GUI(CTk.CTk):
    def __init__(self):
        CTk.set_appearance_mode("System")
        CTk.set_default_color_theme("blue")

        super().__init__()

        self.title("Youtube Downloader")
        self.geometry("450x250")
        self.resizable(False, False)

        self.main_frame = CTk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.main_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.url_label = CTk.CTkLabel(self.main_frame, text="YouTube URL:", font=CTk.CTkFont(size=14, weight="bold"))
        self.url_label.grid(row=0, column=0, columnspan=2, padx=5, sticky="w")

        self.url_text_box = CTk.CTkEntry(self.main_frame, placeholder_text="Insert link to video here...", width=300)
        self.url_text_box.grid(row=1, column=0, columnspan=2, padx=5, pady=(0, 20), sticky="we")

        self.switch_frame = CTk.CTkFrame(self.main_frame, fg_color="transparent")
        self.switch_frame.grid(row=2, column=0, padx=5, pady=(0, 20), sticky="ew")

        self.av_switch = CTk.CTkSwitch(
            self.switch_frame, text="Video / Audio", fg_color="gray20", progress_color="#1f6aa5"
        )
        self.av_switch.pack(anchor="center")

        self.file_formats = CTk.CTkComboBox(self.main_frame, values=["mp4", "mp3", "wav"], state="readonly", width=200)
        self.file_formats.set("mp4")
        self.file_formats.grid(row=2, column=1, padx=5, pady=(0, 20), sticky="w")

        self.download_button = CTk.CTkButton(self.main_frame, text="Download")
        self.download_button.grid(row=4, column=0, columnspan=2, padx=5, pady=(0, 20), sticky="we")

        self.progress_bar = CTk.CTkProgressBar(self.main_frame, width=300)
        self.progress_bar.set(0)  # 0 = 0 %
        self.progress_bar.grid(row=5, column=0, columnspan=2, padx=5, pady=(0, 10), sticky="we")

        self.progress_label = CTk.CTkLabel(self.main_frame, text="", font=CTk.CTkFont(size=12, weight="normal"))
        self.progress_label.grid(row=6, column=0, padx=5, pady=(0, 0), sticky="w")

    def open_save_dialog(self):
        """Opens dialog to save the file"""
        folder_path = filedialog.askdirectory(title="Select folder to save file")
        return folder_path

    def update_progress(self, fraction, eta=""):
        def _update():
            time.sleep(0.02)
            self.progress_bar.set(fraction)
            percent = fraction * 100
            percent_text = f"{percent:.0f}%"
            self.progress_label.configure(text=f"{percent_text}")

        self.after(0, _update)

    def download_finished(self):
        self.progress_label.configure(text="Download finished")
