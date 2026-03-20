import os
import shutil


def _clear_directory(path):
    if not os.path.exists(path):
        return

    for item in os.listdir(path):
        item_path = os.path.join(path, item)

        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
        else:
            os.remove(item_path)


def copy_files_recursive(src, dst):
    if not os.path.exists(src):
        raise FileNotFoundError(f"Source directory does not exist: {src}")

    os.makedirs(dst, exist_ok=True)
    _clear_directory(dst)
    _copy_directory_contents(src, dst)


def _copy_directory_contents(src, dst):
    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dst_item = os.path.join(dst, item)

        if os.path.isdir(src_item):
            os.makedirs(dst_item, exist_ok=True)
            _copy_directory_contents(src_item, dst_item)
        else:
            shutil.copy2(src_item, dst_item)
            print(f"Copied file: {src_item} -> {dst_item}")
