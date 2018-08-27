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
sudo sh -c 'echo '"'"'check_quota || { rm /tmp/monitor-cloud-quota/cloud_budget_hours && echo Logging off. && exit; }'"'"' >> /etc/bash.bashrc'
```

## Schedule cron jobs
Run
```
sudo crontab -e
```
and enter:
```
*/3 * * * * /monitor-cloud-quota/check_quota || python3 /monitor-cloud-quota/out_of_budget_shutdown.py
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
mkdir -p /tmp/monitor-cloud-quota && echo 20 > /tmp/monitor-cloud-quota/cloud_budget_hours && chmod -R 777 /tmp/monitor-cloud-quota
```

## Reset the timer
```
sudo python3 /monitor-cloud-quota/reset_state.py
```
