# written by Deya Eldeen Elkhawaldeh, 03/10/2021
# requires python3.x

import os
import json
  
output_file = ""
target_folder = ""
include_types = []

# Opening config file
with open('config.json') as json_file:
    data = json.load(json_file)
    include_types = data['include_types']
    output_file = data['output_file']
    target_folder = data['target_folder']

original_pwd = os.getcwd()

os.chdir(target_folder) #os.getcwd()
thisdir = os.getcwd()

# r=root, d=directories, f = files
filenames = []
for r, d, f in os.walk(thisdir):
    for file in f:
        for ext in include_types:
            if file.endswith(ext):
                filenames.append(os.path.join(r, file))

os.chdir(original_pwd)
thisdir = os.getcwd()

# Open file3 in write mode
with open(output_file, 'w') as outfile:
    for names in filenames:
        with open(names) as infile:
            outfile.write(infile.read())
        print(f"writing {names}")
        outfile.write("\n")
