# GITHUB LINK: https://gist.github.com/slavakurilyak/ea12b15d21ce9722fa98143f5392488a

import urllib.request
from csv import reader
import os.path

csv_filename = "csv/Lenskart_products_recruitment_challenge.csv"
col_id_num = 2
col_url_num = 4
col_id_name = "product_id"
col_url_name = "Image_Front"
save_folder = "provided_dataset/"
file_format = ".jpg"

with open(csv_filename, 'r') as csv_file:
    for line in reader(csv_file):
        try:
            if os.path.isfile(save_folder + line[col_id_num] + file_format):
                print("Image skipped for {0}".format(line[col_id_num]))
            else:
                if line[col_url_num] != col_url_name and line[col_id_num] != col_id_name:
                    urllib.request.urlretrieve(line[col_url_num], save_folder + line[col_id_num] + file_format)
                    print("Image saved for {0}".format(line[col_id_num]))
                else:
                    print("No result for {0}".format(line[col_id_num]))
        except:
            print("Exception occurred for line"+str(line))