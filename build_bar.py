import os, sys
from pathlib import Path

# Store root folder name
root = Path.cwd()
git_repo_name = Path.cwd().name

# Store all folder names in 'projects' in list and concat to string
# dirs = next(os.walk("projects"))[1]
folders = [folder for folder in root.glob('projects/*') if folder.is_dir()]
folders_string = ' '.join(folder.name for folder in folders)

print("Folders string: " + folders_string)

# Get environment from CLI argument
valid_envs = ['readyapi', 'local', 'test', 'qa', 'prod']
if len(sys.argv) >= 2:
    env_arg = sys.argv[1]
else:
    env_arg = input(f'Choose one of the following environments ({valid_envs}): ')

if env_arg in valid_envs:
    bar_filename = f'{git_repo_name}.{env_arg}.bar'
    override_file = f'config/{env_arg}/baroverides/{git_repo_name}.{env_arg}.properties'

    mqsipackagebar_cmd = f'mqsipackagebar -w projects -a {bar_filename} -k {folders_string} & '
    mqsiapplybaroverride_cmd = f'mqsiapplybaroverride -b {bar_filename} -p {override_file} -r & '

    print(f'Run: {mqsipackagebar_cmd}')
    print(f'Run: {mqsiapplybaroverride_cmd}')

    command = (
        f'cmd /k "'
        f'ace & '
        f'{mqsipackagebar_cmd}'
        f'{mqsiapplybaroverride_cmd}'
        f'move {bar_filename} config/{env_arg}/bars'
        f'"'
    )
else:
    print(f'Invalid argument "{env_arg}" - exiting script...')
    sys.exit()

os.system(command)
