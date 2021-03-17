import os, sys, fnmatch

def argument_is_valid(env_arg):
    valid_envs = ['local', 'test', 'qa', 'prod']
    if env_arg in valid_envs:
        return True
    else:
        return False

# Store root folder name
root_app_name = os.path.basename(os.getcwd())

# Store all folder names in 'projects' in list
dirs = next(os.walk("projects"))[1]

# Concatenate all 'projects' folders to string
folders = ' '.join(dirs)

# Get environment from CLI argument
env_arg = sys.argv[1]
if argument_is_valid(env_arg):
    bar_filename = f'{root_app_name}.{env_arg}.bar'
    override_file = f'config/{env_arg}/baroverides/{root_app_name}.{env_arg}.properties'

    print(override_file)

    command = (
        f'cmd /k "'
        f'ace & '
        f'mqsipackagebar -w projects -a {bar_filename} -k {folders} & '
        f'mqsiapplybaroverride -b {bar_filename} -p {override_file} -k {folders} & '
        f'move {bar_filename} config/{env_arg}/bars'
        f'"'
    )
else:
    print(f'Invalid argument "{env_arg}" - exiting script...')
    sys.exit()

# print(command)

os.system(command)
