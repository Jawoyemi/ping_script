#This code pings a server 

import subprocess
import platform

def ping_server(host):
    # Use the correct ping command depending on the OS
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '4', host]

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        print(f"Ping output for {host}:\n{output}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to ping {host}. Error:\n{e.output}")

ping_server('google.com')        