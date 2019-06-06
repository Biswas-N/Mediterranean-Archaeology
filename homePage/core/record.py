import re
from pprint import pprint

class Record():

    def __init__(self, vase_num, fabric = 'South Italian', technique = 'Red-Figure', shape_name = 'NULL', provenance = 'NULL', date_range = '450-300 BC', collection = 'NULL', scholor_name = 'A.D.Trendall', publication = 'The Red Figure Vases of Paestum, Rome 1987'):
        self.vase_num = vase_num # Done
        self.fabric = fabric # Done
        self.technique = technique # Done
        self.shape_name = shape_name # TODO: Get the last part of before elements
        self.provenance = provenance # TODO: Get the string after 'FROM'
        self.date_range = date_range # Done
        self.collection = collection # TODO: Get the thing after the id number
        self.scholor_name = scholor_name # Done
        self.publication = publication # Done

    def __str__(self):
        return """
        -------- {} --------
        fabric = {}
        technique = {}
        shape_name = {}
        provenance = {}
        date_range = {}
        collection = {}
        scholor_name = {}
        publication = {}
        """.format(
            self.vase_num,
            self.fabric,
            self.technique,
            self.shape_name,
            self.provenance,
            self.date_range,
            self.collection,
            self.scholor_name,
            self.publication
        )

def get_provenance(data, n):
    if 'fro' in data:
        regex = r"{}.* fro[mn](.*)Ht".format(n)
        provenance = re.findall(regex, data)
        if len(provenance) != 0:
            return provenance[0].strip()
        else:
            return 'NULL'
    else:
        return 'NULL'

def get_collection(data, n):
    if 'fro' in data:
        regex = r"{}\s(.*),\sfro".format(n)
        collection = re.findall(regex, data)
    elif 'Gi' in data:
        regex = r"{}\s(.*)\.\sGi".format(n)
        collection = re.findall(regex, data)
    else:
        regex = r"{}\s(.*)\.\sHt".format(n)
        collection = re.findall(regex, data)
    if n == 2:
        return 'New York 1985.74'
    elif len(collection) != 0:
        return collection[0].strip()
    else:
        return 'NULL'

def create_records(data_dict, missed_records):
    records_dict = {}
    found_records = [n for n in range(1,58) if n not in missed_records]
    for n in found_records:
        temp_record = Record(
            vase_num = n, 
            provenance = get_provenance(data_dict[n], n),
            collection = get_collection(data_dict[n], n)
        )
        records_dict[n] = temp_record
    return records_dict