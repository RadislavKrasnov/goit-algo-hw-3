"""Copy files module"""
import sys
import os
from pathlib import Path, PurePath
from shutil import copy

def copy_file(path: str, dist: str) -> None:
    """Copy file from path to desctination directory.
    
    Args:
        path: String with name of directory whose files should be copied.
        dist: String with name of destination directory.

    Returns:
        None.

    Raises:
        Permission Error. If path or destination folder are restricted.
    """
    pure_path = PurePath(path)
    file_extension = pure_path.suffix
    dist = os.path.join(dist, file_extension.strip('.'))
    dist = Path(dist)

    if not dist.exists():
        os.makedirs(dist, exist_ok=True)

    dist_file = dist / pure_path.name
    counter = 1

    if dist_file.exists():
        dist = dist / f"{dist_file.stem}{counter}{file_extension}"
        counter += 1

    copy(path, dist)

def copy_files(path: str, dist: str) -> None:
    """Copy files from one directory to another.

    Args:
        path: String with name of directory whose files should be copied.
        dest: String with name of destination directory.

    Returns:
        None.

    Raises:
        Index Error. When no arguments are passed.
        Permission Error. If path or destination folder are restricted.
    """
    path = Path(path)

    if not path.exists():
        return None
    
    if path.is_dir():
        for path_item in sorted(path.iterdir()):
            if path_item.is_dir():
                copy_files(path_item, dist)
            else:
                copy_file(path_item, dist)
    else:
        copy_file(path, dist)

if __name__ == '__main__':
    try:
        path = sys.argv[1]
        dist = sys.argv[2] if len(sys.argv) > 2 else 'dist'
        copy_files(path, dist)
    except IndexError as e:
        print('Error: ', e)
    except PermissionError as e:
        print(e)
