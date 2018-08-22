import os
import misc

conf = misc.get_conf()

uptime_hours = misc.get_uptime_seconds() / 3600.
print('{:.2f} / {} hours consumed.'.format(uptime_hours, conf['budget_hours']))

if uptime_hours > conf['budget_hours']:
    if os.path.exists(conf['toggle_shutdown_file']):
        print('Out of budget! Shutting down machine.')
        os.remove(conf['toggle_shutdown_file'])
        os.system('sudo poweroff')
