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

    def open_save_dialog(self):
        """Opens dialog to save the file"""
        folder_path = filedialog.askdirectory(title="Select folder to save file")
        return folder_path
