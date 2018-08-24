# How to set up on a Google Cloud VM instance

## Install dependencies
```
sudo apt-get update
sudo apt-get install -y tuptime
```

## Setup tool
```
cd /
sudo git clone -b latest-release https://github.com/lucasbrynte/monitor-cloud-quota.git
cd monitor-cloud-quota
sudo ./setup.sh
```

## Create symlink
```
sudo ln -s /monitor-cloud-quota/check_output /usr/local/bin/check_output
```

## Run at login - visible to user
```
sudo sh -c 'echo check_quota >> /etc/bash.bashrc'
```

## Schedule cron jobs
Run
```
sudo crontab -e
```
and enter:
```
*/10 * * * * check_quota
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

## Reset the timer
```
sudo python3 /monitor-cloud-quota/reset_state.py
```
