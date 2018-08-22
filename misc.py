import json

with open('conf.json', 'r') as f:
    conf = json.load(f)

def get_conf():
    return conf

def get_state():
    with open('state.json', 'r') as f:
        state = json.load(f)
    return state

def update_state(update_dict):
    state = get_state()
    state.update(update_dict)
    with open('state.json', 'w') as f:
        json.dump(state, f)

def read_uptime_raw():
    with open(get_conf()['uptimed_records_file'], 'r') as f:
        line = f.readline()[:-1]
    tokens = line.split(':')
    uptime_seconds = int(tokens[0])
    return uptime_seconds

def get_uptime_seconds():
    return read_uptime_raw() - get_state()['initial_uptime_seconds']
