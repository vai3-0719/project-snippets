import os

def get_file_size(path):
    return os.path.getsize(path)

def list_files(dir_path):
    return os.listdir(dir_path)