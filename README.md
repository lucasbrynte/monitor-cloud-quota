# How to set up on a Google Cloud VM instance

## Install dependencies
```
sudo apt-get update
sudo apt-get install tuptime
```

## Setup tool
```
cd /
sudo git clone -b latest-release https://github.com/lucasbrynte/monitor-cloud-quota.git
cd monitor-cloud-quota
sudo ./setup.sh
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
@reboot /monitor-cloud-quota/update.sh
```

## Enable shutdown feature
In this example, a 20 hour budget is set.
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
