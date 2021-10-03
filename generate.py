# written by Deya Eldeen Elkhawaldeh, 03/10/2021
# requires python3.x

import os
import json
import sys

output_file = ""
target_folder = ""
include_types = []

args = sys.argv[1:]

if len(args) == 0:
    # Opening config file
    with open('config.json') as json_file:
        data = json.load(json_file)
        include_types = data['include_types']
        output_file = data['output_file']
        target_folder = data['target_folder']
elif len(args) == 3:
    include_types = args[0]
    output_file = args[1]
    target_folder = args[2]
else:
    print("invalid number of arguments.")
    sys.exit()

original_pwd = os.getcwd()

os.chdir(target_folder)
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

# Open target_file in write mode
with open(output_file, 'w') as outfile:
    for names in filenames:
        with open(names) as infile:
            try:
                outfile.write(infile.read())
                print(f"scanned {names}")
            except Exception as e:
                print("skipped",names)
        outfile.write("\n")
