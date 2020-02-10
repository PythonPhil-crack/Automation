import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        extensions = {
            "png": "/Users/Admin/Pictures/Download/png",
            "jpg": "/Users/Admin/Pictures/Download/jpg",
            "zip": "/Users/Admin/Documents/zip",
            "exe": "/Users/Admin/Documents/Anwendungen"
        }

        for filename in os.listdir(folder_to_track):
            for key in extensions:
                if filename[-3:] == key:
                    src = "{}/{}".format(folder_to_track, filename)
                    new_destination = "{}/{}".format(extensions[key], filename)
                    os.rename(src, new_destination)
                    print(
                        f"{filename} has been succesfully moved to {extensions[key]}")


folder_to_track = "/Users/Admin/Downloads"
event_Handler = MyHandler()
my_observer = Observer()

my_observer.schedule(event_Handler, folder_to_track, True)

my_observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
