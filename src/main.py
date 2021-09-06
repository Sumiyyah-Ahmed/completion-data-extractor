import os
import csv
from urllib.parse import urlparse
from src.sequence import Sequence
# import pandas as pd

parsed_url = urlparse("https://datavillagesa.blob.core.windows.net/volve?sv=2018-03-28&sr=c&sig=Kaw%2BYSeWVnRqalRJcRoiTOpL%2BC4HrIjPd2cba2gGr34%3D&se=2021-09-30T04%3A29%3A07Z&sp=rl")
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
input_directory = os.path.join(BASE_DIR, 'input')
output_directory = os.path.join(BASE_DIR, 'output')
sequence = Sequence()
input_files = []

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
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        count = 0
        for row in csv_reader:
            if count == 1: break
            file_to_extract = row[0][6:]
            print(get_deposit_path(file_to_extract))
            sequence.add_process(
                "azcopy",
                "cp",
                get_file_url(file_to_extract),
                get_deposit_path(file_to_extract),
            )
            count += 1


def get_file_url(az_file_path):
    return f"\"{parsed_url.netloc}{parsed_url.path}/{az_file_path}?{parsed_url.query}\""

def get_deposit_path(az_file_path):
    return f"\"{BASE_DIR}/output{parsed_url.path}/{os.path.dirname(az_file_path)}\""



def main():
    populate_input_files()
    for file_path in input_files:
        extract_data_from_csv(file_path)
    sequence.execute()

if __name__ == '__main__':
    main()
