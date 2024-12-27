import customtkinter as tk
from tkinter import filedialog


# Class to create the GUI
class GUI(tk.CTk):
    def __init__(self):
        tk.CTk.__init__(self)
        self.title("Youtube Downloader")
        self.geometry("300x150")

        self.url_label = tk.CTkLabel(self, text="Youtube URL:")
        self.url_text_box = tk.CTkEntry(self)
        self.download_button = tk.CTkButton(self, text="Download")

        self.url_label.pack()
        self.url_text_box.pack()
        self.download_button.pack()

        self.progress_bar = tk.CTkProgressBar(self, width=300)
        self.progress_bar.set(0)  # 0 = 0%
        self.progress_bar.pack(pady=10)

        self.progress_label = tk.CTkLabel(self, text="")
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
