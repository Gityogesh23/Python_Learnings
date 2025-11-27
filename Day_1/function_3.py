import psutil
import platform
import datetime
import os

def get_os_info():
    print("===== Operating System Info =====")
    print("OS:", platform.system())
    print("Version:", platform.version())
    print("Release:", platform.release())
    print()

def get_ram_info():
    print("===== RAM Information =====")
    ram = psutil.virtual_memory()
    print(f"Total RAM: {ram.total / (1024**3):.2f} GB")
    print(f"Available RAM: {ram.available / (1024**3):.2f} GB")
    print(f"Used RAM: {ram.used / (1024**3):.2f} GB")
    print(f"RAM Usage: {ram.percent}%")
    print()

def get_cpu_info():
    print("===== CPU Information =====")
    print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
    print("CPU Cores:", psutil.cpu_count(logical=True))
    print("Physical Cores:", psutil.cpu_count(logical=False))
    print()

def get_disk_info():
    print("===== Disk Information =====")
    disk = psutil.disk_usage('/')
    print(f"Total Disk: {disk.total / (1024**3):.2f} GB")
    print(f"Used Disk: {disk.used / (1024**3):.2f} GB")
    print(f"Free Disk: {disk.free / (1024**3):.2f} GB")
    print(f"Disk Usage: {disk.percent}%")
    print()

def get_uptime():
    print("===== System Uptime =====")
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    now = datetime.datetime.now()
    uptime = now - boot_time

    print("Boot Time:", boot_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Uptime:", uptime)
    print()

def main():
    get_os_info()
    get_ram_info()
    get_cpu_info()
    get_disk_info()
    get_uptime()

main()

"""
# Note:
psutil-->psutil is a cross-platform python library used to retrieve info on running 
processes and system utilization,such as CPU,memory,Disk & network usage.
It is commonly used for system monitoring ,profiling
and process management.
It's functionality is same as UNIX command-line tools like top and ps .
You can install it first before use.-->pip install psutil

# Why do we need pip?

Because Python only comes with built-in libraries, and for advanced features we need external packages:

1) Working with Excel → openpyxl

2) Working with cloud APIs → boto3

3) Web development → flask, django

4) Machine learning → numpy, pandas, scikit-learn

5) Monitoring → psutil

6) GUI → tkinter (built-in) but others need install

7) So pip helps install everything that is not included by default
"""
