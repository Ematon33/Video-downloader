import customtkinter as CTk
from tkinter import filedialog
import utilites


# Class to create the GUI
class GUI(CTk.CTk):
    def __init__(self):
        # Set the appearance mode and default color theme
        CTk.set_appearance_mode("System")
        CTk.set_default_color_theme("blue")

        # Initialize the CTk class
        super().__init__()

        # Set the window title, size, and make it non-resizable
        self.title("Video Downloader")
        self.geometry("450x250")
        self.resizable(False, False)
        self.iconbitmap(utilites.resource_path("favicon.ico"))

        # Create the main frame
        self.main_frame = CTk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Configure the grid layout
        self.main_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        # Create the widgets
        self.url_label = CTk.CTkLabel(self.main_frame, text="Video URL:", font=CTk.CTkFont(size=14, weight="bold"))
        self.url_label.grid(row=0, column=0, columnspan=2, padx=5, sticky="w")

        # Create the text box for the URL
        self.url_text_box = CTk.CTkEntry(self.main_frame, placeholder_text="Insert link to video here...", width=300)
        self.url_text_box.grid(row=1, column=0, columnspan=2, padx=5, pady=(0, 20), sticky="we")

        # Create the switch for audio/video
        self.switch_frame = CTk.CTkFrame(self.main_frame, fg_color="transparent")
        self.switch_frame.grid(row=2, column=0, padx=5, pady=(0, 20), sticky="ew")

        # Create the switch
        self.av_switch = CTk.CTkSwitch(
            self.switch_frame, text="Video / Audio", fg_color="gray20", progress_color="#1f6aa5"
        )
        self.av_switch.pack(anchor="center")

        # Create the file format ComboBox
        self.file_formats = CTk.CTkComboBox(self.main_frame, values=["mp4", "mp3", "wav"], state="readonly", width=200)
        self.file_formats.set("mp4")
        self.file_formats.grid(row=2, column=1, padx=5, pady=(0, 20), sticky="w")

        # Create the download button
        self.download_button = CTk.CTkButton(self.main_frame, text="Download")
        self.download_button.grid(row=4, column=1, padx=5, pady=(0, 20), sticky="we")

        # Create the cancel button
        self.cancel_button = CTk.CTkButton(self.main_frame, text="Cancel", fg_color="grey20")
        self.cancel_button.grid(row=4, column=0, padx=5, pady=(0, 20), sticky="we")

        # Create the progress bar
        self.progress_bar = CTk.CTkProgressBar(self.main_frame, width=300)
        self.progress_bar.set(0)  # 0 = 0 %
        self.progress_bar.grid(row=5, column=0, columnspan=2, padx=5, pady=(0, 2), sticky="we")

        # Create the progress label
        self.progress_label = CTk.CTkLabel(self.main_frame, text="", font=CTk.CTkFont(size=20, weight="bold"))
        self.progress_label.grid(row=6, column=0, columnspan=2, padx=5, pady=(0, 0), sticky="we")

    def open_save_dialog(self):
        """Opens dialog to save the file"""
        folder_path = filedialog.askdirectory(title="Select folder to save file")
        return folder_path

    def update_progress(self, fraction, status=""):
        def _update():
            """Update the progress bar and label"""
            self.progress_bar.set(fraction)
            percent = fraction * 100
            percent_text = f"{percent:.0f}%"
            self.progress_label.configure(text=f"{percent_text} {status}")

        self.after(20, _update)

    def download_finished(self):
        """Called when the download is finished"""
        self.progress_label.configure(text="Download finished")
