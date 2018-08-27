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
    sys.exit(0)

uptime_hours = misc.get_uptime_seconds() / 3600.
with open(conf['budget_hours_file'], 'r') as f:
    budget_hours = float(f.readline().split()[0])
print('{:.2f} / {} hours consumed.'.format(uptime_hours, budget_hours))

print('='*40)
if uptime_hours > budget_hours:
    sys.exit(1)
else:
    sys.exit(0)
