import sys
from pathlib import Path

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
    print(f'Invalid argument "{env_arg}" - exiting script...')
    sys.exit()

# Create BAR and override directories
Path.mkdir(bar_dir, exist_ok=True, parents=True)
Path.mkdir(override_dir, exist_ok=True, parents=True)