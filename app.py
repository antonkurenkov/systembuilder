import argparse
import os

def inner_function(path):
    if os.path.isfile(path):
        return path
    else:
        raise FileNotFoundError

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=inner_function)
parser.parse_args()
