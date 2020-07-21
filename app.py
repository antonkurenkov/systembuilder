import argparse
import os

def file_path(path):
    if os.path.isfile(path):
        return path
    else:
        raise FileNotFoundError

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=file_path)
parser.parse_args()
