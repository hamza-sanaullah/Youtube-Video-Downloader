import tkinter as tk
import yt_dlp
import os
from tkinter import filedialog
from tkinter import ttk
import threading
from PIL import Image, ImageTk

def download_video():
    def start_download():
        video_url = url_entry.get()
        save_path = save_path_entry.get()
        selected_format = format_dropdown.get()
        selected_resolution = resolution_dropdown.get()

        if video_url and save_path:
            if selected_format == 'mp3':
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
                    'ffmpeg_location': os.path.join('C:', 'Program Files', 'ffmpeg', 'bin', 'ffmpeg.exe'),
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
            else:
                ydl_opts = {
                    'format': f'{selected_format}+bestvideo[height<={selected_resolution}]+bestaudio/best',
                    'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
                    'ffmpeg_location': os.path.join('C:', 'Program Files', 'ffmpeg', 'bin', 'ffmpeg.exe')
                }

            progress_light.config(image=red_light)

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(video_url, download=False)
                title = info.get('title', '')
                file_name_label.config(text=f"Downloading: {title}")

                ydl.add_default_info_extractors()
                result = ydl.extract_info(video_url, download=True)

            progress_light.config(image=green_light)
            file_name_label.config(text="Download Successful!")

    download_thread = threading.Thread(target=start_download)
    download_thread.start()


def browse_save_location():
    save_path = filedialog.askdirectory()
    save_path_entry.delete(0, tk.END)
    save_path_entry.insert(tk.END, save_path)


def download_as_mp3():
    format_dropdown.set('mp3')
    download_video()


def on_button_hover(event):
    event.widget.config(bg="#FF0000")


def on_button_leave(event):
    event.widget.config(bg="black")


window = tk.Tk()
window.title("A H B A Downloader free 2023")
window.geometry("650x420")
window.configure(bg="#f2f2f2")


background_images = []
image_files = ["jpeg 1.jpeg", "jpeg 2.jpeg", "jpeg 3.jpeg", "jpeg 4.jpeg", "jpeg 5.jpeg"]

for file in image_files:
    image = Image.open(file)
    resized_image = image.resize((650, 420))
    background_images.append(ImageTk.PhotoImage(resized_image))

background_label = tk.Label(window, image=background_images[0])
background_label.place(x=0, y=0, relwidth=1, relheight=1)

title_label = tk.Label(window, text="A H B A Youtube Downloader Free 2023", font=("Times New Roman", 20, "bold"),
                       bg="#FFFF00")
title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

url_label = tk.Label(window, text="YouTube Video URL:", bg="#088F8F", fg="white")
url_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
url_entry = tk.Entry(window, width=50, bg="white")
url_entry.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

save_path_label = tk.Label(window, text="Save Path:", bg="#0096FF", fg="white")
save_path_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
save_path_entry = tk.Entry(window, width=50, bg="white")
save_path_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

browse_button = tk.Button(window, text="Browse", command=browse_save_location, bg="#FF0000", fg="white")
browse_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

format_label = tk.Label(window, text="Video Format:", bg="yellow")
format_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
format_options = ['bestvideo', 'bestaudio', 'mp4', 'webm', 'mkv']
format_dropdown = ttk.Combobox(window, values=format_options, state="readonly")
format_dropdown.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

resolution_label = tk.Label(window, text="Resolution:", bg="yellow")
resolution_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
resolution_options = ['144', '240', '360', '480', '720', '1080', '1440', '2160']
resolution_dropdown = ttk.Combobox(window, values=resolution_options, state="readonly")
resolution_dropdown.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

download_button = tk.Button(window, text="Download", command=download_video, bg="black", fg="white")
download_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
download_button.bind("<Enter>", on_button_hover)
download_button.bind("<Leave>", on_button_leave)

download_mp3_button = tk.Button(window, text="Download as MP3", command=download_as_mp3, bg="black", fg="white")
download_mp3_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
download_mp3_button.bind("<Enter>", on_button_hover)
download_mp3_button.bind("<Leave>", on_button_leave)

red_light = ImageTk.PhotoImage(Image.open("jpeg 6.jpeg"))
green_light = ImageTk.PhotoImage(Image.open("jpeg 7.jpeg"))

progress_light = tk.Label(window, image=green_light, width=50, height=50)
progress_light.place(relx=0.02, rely=0.1)

file_name_label = tk.Label(window, text="", bg="#f2f2f2")
file_name_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def change_background_image():
    current_image_index = 0

    def update_background():
        nonlocal current_image_index
        background_label.config(image=background_images[current_image_index])
        current_image_index = (current_image_index + 1) % len(background_images)
        window.after(2000, update_background)

    update_background()
copyright_label = tk.Label(window, text="CopyRighted By A-B-A-H  \U0001F600 2023", font=("Arial", 10), bg="#00FFFF", fg="#000000")
copyright_label.place(relx=0.5, rely=0.98, anchor=tk.S)


window.after(5000, change_background_image)
window.mainloop()
