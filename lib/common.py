import os


def create_dir_if_not_exists(directory_path, verbose=True):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    if verbose:
        print(directory_path)
