# This program to extract individual records form the html file created by stringify

from bs4 import BeautifulSoup
import re

def data_to_dict(file_path):
    print('Extracting from ', file_path)

    with open(file_path, 'r') as data_file:
        soup = BeautifulSoup(data_file, features='html.parser')
        spans_9px = [s for s in soup.find_all('span') if 'font-size:9px' in str(s)]

        data_str = ''.join([span.text for span in spans_9px ])
        data_str = " ".join(data_str.split('\n'))
        return get_records(data_str)

def get_records(data_str):
        records = {}
        missed_records = []
        for i in range (1, 58):
                regex = r"((?=\*{}).*(?=\*{}\s))".format(i, i+1)
                record = re.findall(regex, data_str)

                if len(record) != 0:
                        record_str = bytes(record[0], 'unicode_escape').decode('unicode_escape')
                        record_str = "(".join(record_str.split('['))
                        records[i] = record_str
                else:
                        missed_records.append(i)
        print("-> {} records missed, they are {}".format(len(missed_records), missed_records))
        return records, missed_records