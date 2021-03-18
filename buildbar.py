import os, sys

# Store root folder name
git_repo_name = os.path.basename(os.getcwd())

# Store all folder names in 'projects' in list and concat to string
dirs = next(os.walk("projects"))[1]
folders = ' '.join(dirs)

# Get environment from CLI argument
valid_envs = ['local', 'test', 'qa', 'prod']
if len(sys.argv) >= 2:
    env_arg = sys.argv[1]
else:
    env_arg = input(f'Choose one of the following environments ({valid_envs}): ')

if env_arg in valid_envs:
    bar_filename = f'{git_repo_name}.{env_arg}.bar'
    override_file = f'config/{env_arg}/baroverides/{git_repo_name}.{env_arg}.properties'

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

os.system(command)
