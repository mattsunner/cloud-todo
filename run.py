"""
run.py - Orchestrator script for launching environments with docker-compose

Script uses a CLI flag of either '-dev' or '-prod' to launch the appropriate docker-compose envionment based
the YAML files in the repo. 

TODO: Setup logging strategies for both dev and prod envs


Author: Matthew Sunner, 2022
"""



from asyncio import subprocess
import sys
import getopt
import subprocess

def capture_command():
    """capture_command - Arg parser to capture CLI -f command to run env in either dev or prod

    Returns:
        str: String command captured from cli parser.
    """

    command: str = ''
  
    argv: list = sys.argv[1:]
  
    try:
        opts, args = getopt.getopt(argv, "f:")
      
    except:
        print("Error")
  
    for opt, arg in opts:
        if opt in ['-f']:
            command = arg
        else:
            print("error")
      
  
    return command


def env_launcher(command: str):
    """env_launcher - command parse router function

    Args:
        command (str): CLI command string
    """
    if command == 'prod':
        subprocess.run(['docker-compose', '-f', 'docker-compose.yml', 'up'])
    elif command == 'dev':
        print('dev')
        subprocess.run(['docker-compose', '-f', 'docker-compose.dev.yml', 'up'])
  

# Application Loop
if __name__ == '__main__':
    env_launcher(capture_command())