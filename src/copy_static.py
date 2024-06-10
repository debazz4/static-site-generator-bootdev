import os
import shutil


def copy_dir_contents(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        dest_item = os.path.join(dest_dir, item)

        if os.path.isdir(source_item):
            copy_dir_contents(source_item, dest_item)
        elif os.path.isfile(source_item):
            shutil.copy(source_item, dest_item)
            print(f"Copied: {source_item} to {dest_item}")
