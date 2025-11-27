import os

def check_date():
    os.system("date /T")     # Works on Windows

def check_df():
    os.system("wsl df -h")   # Runs Linux df

check_date()
check_df()

"""
Understanding Your df -h Output in WSL
✔ /usr/lib/wsl/drivers

This is a virtual filesystem containing Windows → WSL drivers
(used for GPU, network, file I/O, etc.)

in output you see--->/dev/sdd mounted twice

WSL sometimes mounts the same disk in multiple places internally

⚠️ You should NOT modify or delete anything inside these.

✔ /usr/lib/wsl/lib, /dev, /run, /run/lock

These are ephemeral filesystem strored in RAM ,not a physical Disk.
eg. .run , /dev, /run/lock, /tmp

# Note that-->
1) You should not edit or delete these directories

2) Your df -h is showing healthy mounts

3) The repetition /dev/sdd is expected due to WSL2 virtualization

"""