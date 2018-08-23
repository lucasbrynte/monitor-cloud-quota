#!/usr/bin/python3
import os
import sys
import misc

conf = misc.get_conf()

print('='*40)
print('Budget Monitor')
print('-'*40)

if not os.path.exists(conf['budget_hours_file']):
    print('No budget set, exiting.')
    print('='*40)
    sys.exit()

uptime_hours = misc.get_uptime_seconds() / 3600.
with open(conf['budget_hours_file'], 'r') as f:
    budget_hours = float(f.readline().split()[0])
print('{:.2f} / {} hours consumed.'.format(uptime_hours, budget_hours))

if uptime_hours > budget_hours:
    assert os.system('sudo rm {}'.format(conf['budget_hours_file'])) == 0
    os.system('sudo mkdir -p {}'.format(conf['log_path']))
    os.system('sudo sh -c \'date >> {}\''.format(os.path.join(conf['log_path'], 'shutdowns')))
    print('Out of budget! Shutting down machine.')
    print('='*40)
    os.system('sudo poweroff')
else:
    print('='*40)
