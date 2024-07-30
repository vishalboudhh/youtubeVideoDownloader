import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=progress_function)
        stream = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        # Start the download
        stream.download()
        
        # Download complete
        print("Download Complete!")
        finishLabel.configure(text="Downloaded!")
        finishLabel.configure(text="Downloaded!", text_color="green")
    except Exception as e:
        print("Error:", e)
        

def progress_function(stream, chunk, bytes_remaining, progress_bar):
    # Calculate the percentage of the download
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    # Update the progress bar
    progress_bar.set(percentage)

# system setting
customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme("blue")

# our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a Youtube link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, textvariable=url_var)
link.pack()

# Finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Create progress bar
progressBarWidget = tkinter.ttk.Progressbar(app, orient='horizontal', length=200, mode='determinate')
progressBarWidget.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

# Run app
app.mainloop()
