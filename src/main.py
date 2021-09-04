import os
from src.sequence import Sequence
# import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
input_directory = os.path.join(BASE_DIR, 'input')
output_directory = os.path.join(BASE_DIR, 'output')

input_files = []
extraction_locations = []

def is_csv_file(file_path):
    _, ext = os.path.splitext(file_path)
    return os.path.isfile(file_path) and ext == '.csv'

def populate_input_files():
    global input_files
    for file in os.listdir(input_directory):
        file_path = os.path.join(input_directory, file)
        if is_csv_file(file_path):
            input_files.append(file_path)

def extract_data_from_csv(file_path):
    pass

def main():
    populate_input_files()
    print(input_files)





    sequence = Sequence()
    sequence.add_process('echo', 'hello')
    sequence.add_process('echo', 'world1')
    sequence.execute()

if __name__ == '__main__':
    main()
