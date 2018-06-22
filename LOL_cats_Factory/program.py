import os
import platform
import subprocess

import cat_service


def print_header():
    print('--------------------------')
    print('------LOLCAT FACTORY------')
    print('--------------------------')


def create_output_folder():
    folder = 'cat_pictures'
    full_path = os.path.abspath(os.path.join('.', folder))
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):

    cat_count = 8
    for i in range(1,cat_count+1):
        name = "lolcat_{}".format(i)
        print('Downloading cat {}'.format(name))
        cat_service.get_cat(name, folder)
    print('Done!')

def open_folder(folder ):
    print('Displaying cats in OS Window')
    if platform.system() == "Darwin":
        subprocess.call(['open', folder])
    elif platform.system() == "Linux":
        subprocess.call(['xdg-open', folder])
    elif platform.system() == "Windows":
        subprocess.call(['explorer', folder])
    else:
        print("OS {} is not supported".format(platform.system()))


def main():
    print_header()
    folder = create_output_folder()
    download_cats(folder)
    open_folder(folder)


if __name__ == '__main__':
    main()
