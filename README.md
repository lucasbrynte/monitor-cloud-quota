## Install dependencies
```
sudo apt-get update
sudo apt-get install tuptime
```

## Setup tool
```
./setup.sh
```

## Run at login - visible to user
```
sudo sh -c 'echo python3 /monitor-cloud-quota/check_quota.py >> /etc/bash.bashrc'
```

## Schedule cron jobs
Run
```
sudo crontab -e
```
and enter:
```
*/10 * * * * python3 /monitor-cloud-quota/check_quota.py
@reboot python3 /monitor-cloud-quota/update.sh
```

## Enable shutdown feature
## Add custom metadata to VM instance:
key:
```
startup-script
```
value:
```
#! /bin/bash
echo 20 > /tmp/cloud_budget_hours
```
