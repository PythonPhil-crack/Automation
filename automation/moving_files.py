import os


def moveFiles():
    extensions = {
        "png": "/Users/Admin/Pictures/Download/png",
        "jpg": "/Users/Admin/Pictures/Download/jpg",
        "zip": "/Users/Admin/Documents/zip",
        "exe": "/Users/Admin/Documents/Anwendungen"
    }

    folder_to_track = "/Users/Admin/Downloads"
    for filename in os.listdir(folder_to_track):
        for key in extensions:
            if filename[-3:] == key:
                src = "{}/{}".format(folder_to_track, filename)
                new_destination = "{}/{}".format(extensions[key], filename)
                os.rename(src, new_destination)


moveFiles()
