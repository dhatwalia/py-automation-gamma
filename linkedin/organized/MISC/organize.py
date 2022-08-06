import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', '.txt'],
    "AUDIO": ['.m4a', '.m4b', '.mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}


def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'  # If filetype doesn't exist in our dictionary


def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue

        source = Path(item)
        filetype = source.suffix.lower()

        organizedPath = Path('../organized/')
        if not organizedPath.is_dir():
            organizedPath.mkdir()

        directoryPath = Path('../organized/' + pickDirectory(filetype))
        if not directoryPath.is_dir():
            directoryPath.mkdir()

        destination = directoryPath.joinpath(source)
        destination.write_bytes(source.read_bytes())


organizeDirectory()
