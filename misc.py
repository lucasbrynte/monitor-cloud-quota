import os
import subprocess
import json

def get_curr_dir():
    return os.path.dirname(__file__)

with open(os.path.join(get_curr_dir(), 'conf.json'), 'r') as f:
    conf = json.load(f)

def get_conf():
    return conf

def get_state():
    with open(os.path.join(get_curr_dir(), 'state.json'), 'r') as f:
        state = json.load(f)
    return state

def update_state(update_dict):
    state = get_state()
    state.update(update_dict)
    with open(os.path.join(get_curr_dir(), 'state.json'), 'w') as f:
        json.dump(state, f)

def read_uptime_raw():
    cmd_list = ['tuptime', '-s']
    identifier = 'System uptime:'
    tuptime_output = subprocess.check_output(cmd_list).decode('utf-8').splitlines()
    # print('\n'.join(tuptime_output))
    for row in tuptime_output:
        if row.startswith(identifier):
            uptime_seconds = float(row.split()[-1])
            return uptime_seconds
    raise Exception("\'{}\' not found in output from command:  \'{}\'".format(identifier, ' '.join(cmd_list)))

def get_uptime_seconds():
    return read_uptime_raw() - get_state()['initial_uptime_seconds']
