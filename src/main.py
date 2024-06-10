from textnode import *
import os
import shutil

from copy_static import copy_dir_contents
from page_generation import generate_pages_recursive



def main():
    source_directory = "./static"
    destination_directory = "./public"
    #Clear the contents of the destination directory if it exists
    if os.path.exists(destination_directory):
        shutil.rmtree(destination_directory)

    #Copy the contents of the source directory to the destination directory
    print("copying static files to public directory...")
    copy_dir_contents(source_directory, destination_directory)
    generate_pages_recursive("./content", "./template.html", destination_directory)
    
    


if __name__== "__main__":
    main()
