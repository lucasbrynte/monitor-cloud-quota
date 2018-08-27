import os
import misc

conf = misc.get_conf()

print('Out of budget!')

print('Logging...')
assert os.system('sudo rm {}'.format(conf['budget_hours_file'])) == 0
os.system('sudo mkdir -p {}'.format(conf['log_path']))
os.system('sudo sh -c \'date >> {}\''.format(os.path.join(conf['log_path'], 'shutdowns')))

print('Shutting down machine.')
os.system('sudo poweroff')
