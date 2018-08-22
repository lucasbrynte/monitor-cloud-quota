import os
import misc

conf = misc.get_conf()

uptime_hours = misc.get_uptime_seconds() / 3600.
print('{:.2f} / {} hours consumed.'.format(uptime_hours, conf['budget_hours']))

if uptime_hours > conf['budget_hours']:
    print('Out of budget - shutting down machine.')
    # os.system('sudo poweroff')
