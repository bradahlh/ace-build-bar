import os, sys

# Store root folder name
root_app_name = os.path.basename(os.getcwd())

# Store all folder names in 'projects' in list
dirs = next(os.walk("projects"))[1]

# Concatenate all 'projects' folders to string
folders = ' '.join(dirs)

# Get environment from CLI argument
env_arg = sys.argv[1]
valid_envs = ['local', 'test', 'qa', 'prod']
if env_arg in valid_envs:
    command = f'cmd /k "ace & mqsipackagebar -w projects -a {root_app_name}.{env_arg}.bar -k {folders}"'
else:
    print('Invalid argument - exiting script...')
    sys.exit()

print(command)

# os.system(command)
