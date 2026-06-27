import os
import platform
import subprocess
import shutil
import time


p_name = platform.system()

accepted = r"accepted"
denied = r"denied"
unknown = r"unknown"

if p_name == "Windows":
    folder_path = r"H:\project"



    acc = os.path.join(folder_path, accepted)
    den = os.path.join(folder_path, denied)
    unk = os.path.join(folder_path, unknown)

    if not os.path.isdir(acc):
        os.makedirs(acc)

    if not os.path.isdir(den):
        os.makedirs(den)

    if not os.path.isdir(unk):
        os.makedirs(unk)

    files_path = acc
    sub = subprocess.Popen(["explorer", folder_path])



elif p_name == "Linux":
    folder_path = "/mnt/data2/project/"
    files_path = "/mnt/data2/project/accepted/"

    acc = os.path.join(folder_path, accepted)
    den = os.path.join(folder_path, denied)
    unk = os.path.join(folder_path, unknown)

    if not os.path.isdir(acc):
        os.makedirs(acc)

    if not os.path.isdir(den):
        os.makedirs(den)

    if not os.path.isdir(unk):
        os.makedirs(unk)
    
    sub = subprocess.Popen(["thunar", folder_path]) 


safe_extensions = (
".txt", ".docx", ".pdf",
".jpg", ".jpeg", ".png", ".gif", ".bmp",
".mp3", ".wav", ".aac",
".mp4", ".avi", ".mkv", ".mov",
".zip", ".rar"
)

dangerous_extensions = (
".exe", ".bat", ".msi", ".com",
".js", ".vbs", ".ps1",
".docm", ".xlsm",
".dll", ".sys"
)


categories = {
    "text" : (".txt", ".docx", ".pdf"),
    "image" :(".jpg", ".jpeg", ".png", ".gif", ".bmp"),
    "audio" : (".mp3", ".wav", ".aac"),
    "video" : (".mp4", ".avi", ".mkv", ".mov"),
    "compressed" : (".zip", ".rar"),
}

text = os.path.join(files_path, r"text")
image = os.path.join(files_path, r"image")
audio = os.path.join(files_path, r"audio")
video = os.path.join(files_path, r"video")
compressed = os.path.join(files_path, r"compressed")

if not os.path.isdir(text):
    os.makedirs(text)
if not os.path.isdir(image):
    os.makedirs(image)
if not os.path.isdir(audio):
    os.makedirs(audio)
if not os.path.isdir(video):
    os.makedirs(video)
if not os.path.isdir(compressed):
    os.makedirs(compressed)



while True:
    for file in os.listdir(folder_path):
        full_file_path = os.path.join(folder_path, file)

        if file in ["accepted", "denied", "unknown"]:
            pass

        elif file.endswith(safe_extensions):
            shutil.move(full_file_path, acc)

        elif file.endswith(dangerous_extensions):
            shutil.move(full_file_path, den)

        else:
            shutil.move(full_file_path, unk)


    
    for file in os.listdir(files_path):
        the_full_path = os.path.join(files_path, file)

        split = file.split(".")

        if file in ["text", "image", "audio", "video", "compressed"]:
            continue


        for folder_name, extension in categories.items():
                if file.endswith(extension):
                    destination_folder = os.path.join(files_path, folder_name)
                    shutil.move(the_full_path, destination_folder)
                    break

    time.sleep(10)

                    