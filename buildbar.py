import os, sys

# Store root folder name
root_app_name = os.path.basename(os.getcwd())

# Store all folder names in 'projects' in list
dirs = next(os.walk("projects"))[1]

# Concatenate all 'projects' folders to string
folders = ' '.join(dirs)

# env = {sys.argv[1]}
env = 'qa'

command = f'cmd /k "ace & mqsipackagebar -w projects -a {root_app_name}.{env}.bar -k {folders}"'

# print(command)

os.system(command)
