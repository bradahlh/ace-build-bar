import sys
from pathlib import Path

# Store root folder name
root = Path.cwd()

valid_envs = ['readyapi', 'local', 'test', 'qa', 'prod']
if len(sys.argv) >= 2:
    env_arg = sys.argv[1]
else:
    env_arg = input(f'Choose one of the following environments ({valid_envs}): ')

if env_arg in valid_envs:
    env_path = Path(f'config/{env_arg}')
    bar_dir = Path.joinpath(env_path, 'bars')
    override_dir = Path.joinpath(env_path, 'baroverides')
else:
    env_arg = input(f'Choose one of the following environments ({valid_envs}): ')
    if env_arg not in valid_envs:
        print(f'Invalid argument "{env_arg}" - exiting script...')
        sys.exit()

# Create BAR and override directories and files
Path.mkdir(bar_dir, exist_ok=True, parents=True)
Path(bar_dir / f'{root.name}.{env_arg}.bar').touch()

Path.mkdir(override_dir, exist_ok=True, parents=True)
Path(override_dir / f'{root.name}.{env_arg}.properties').touch()
