from os.path import expanduser
import os,sys


## Set your SQL table or CSV table into /home/[uname]/data_sets directory
## In this template I used CSV format

####################################
home = expanduser("~")
ds_directory_name = "/data_sets/"
files_path = home + ds_directory_name
raw_csv = os.listdir(files_path)[0]
full_file_path = home + ds_directory_name + raw_csv
####################################


