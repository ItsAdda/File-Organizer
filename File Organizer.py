import os
import shutil
import logging
from tqdm import tqdm
import tkinter as tk

root = tk.Tk()
root.title("File Organizer")
root.geometry("600x300")

label = tk.Label(root, text="File Organizer")
label.pack()

path_entry = tk.Entry(root, width=50)
path_entry.pack()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

fileSizes = {
    "Small": 10 * 1024 * 1024,
    "Medium": 250 * 1024 * 1024
}

Home = os.path.expanduser("~")
DownloadPath = os.path.join(Home, "Downloads")


def start_organizing():
    path = path_entry.get()
    Recursive = recursive_var.get()
    Flag = True if Recursive else False
    GetFileSize(path, Flag)


def GetFileSize(path, Flag):
    os.chdir(path)
    for file in tqdm(os.listdir(path), desc="Organizing files"):
        file_path = os.path.join(path, file)

        if os.path.isdir(file_path) and Flag:
            GetFileSize(file_path, Flag)
            continue

        if os.path.isfile(file_path):
            size = os.path.getsize(file_path)
            if size < fileSizes["Small"]:
                if os.path.exists(os.path.join(path, "Small")):
                    small_path = os.path.join(path, "Small")
                    shutil.move(file_path, small_path)
                    logging.info(f"Moved {file} -> {small_path}")
                else:
                    os.makedirs(os.path.join(path, "Small"))
                    small_path = os.path.join(path, "Small")
                    shutil.move(file_path, small_path)
                    logging.info(f"Moved {file} -> {small_path}")
                    continue
            elif fileSizes["Medium"] > size > fileSizes["Small"]:
                if os.path.exists(os.path.join(path, "Medium")):
                    medium_path = os.path.join(path, "Medium")
                    shutil.move(file_path, medium_path)
                    logging.info(f"Moved {file} -> {medium_path}")
                else:
                    os.makedirs(os.path.join(path, "Medium"))
                    medium_path = os.path.join(path, "Medium")
                    shutil.move(file_path, medium_path)
                    logging.info(f"Moved {file} -> {medium_path}")
                    continue
            else:
                if os.path.exists(os.path.join(path, "Large")):
                    large_path = os.path.join(path, "Large")
                    shutil.move(file_path, large_path)
                    logging.info(f"Moved {file} -> {large_path}")
                else:
                    os.makedirs(os.path.join(path, "Large"))
                    large_path = os.path.join(path, "Large")
                    shutil.move(file_path, large_path)
                    logging.info(f"Moved {file} -> {large_path}")
                    continue


if __name__ == "__main__":
    recursive_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Organize subfolders", variable=recursive_var).place(x = 230, y = 80)
    tk.Button(root, text="Organize", command=start_organizing).place(x=270, y=150)
    root.mainloop()




