# Besder-ip-camera-time-sync-fix
To use, add this script to your cron via crontab -e:

`0 * * * * python3 /path/to/command/camera_fix.py`

_(Will run script at beginning of every hour (minute "0")_

-------------------------
**Time guideline for cron aid:**
```
* * * * * command to be executed
- - - - -
| | | | |
| | | | ----- Day of week (0 - 7) (Sunday=0 or 7)
| | | ------- Month (1 - 12)
| | --------- Day of month (1 - 31)
| ----------- Hour (0 - 23)
------------- Minute (0 - 59)
```
