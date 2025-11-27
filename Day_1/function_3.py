import psutil
import platform
import datetime
import os

def get_os_info():
    print("===== Operating System Info =====")
    print("OS:", platform.system())  #Windows
    print("Version:", platform.version()) #vesrion-->10.0...
    print("Release:", platform.release())  #11
    print()

def get_ram_info():
    print("===== RAM Information =====")
    ram = psutil.virtual_memory()  
    print(f"Total RAM: {ram.total / (1024**3):.2f} GB")          #15.40 ~total =16 GB
    print(f"Available RAM: {ram.available / (1024**3):.2f} GB")  #5.47 GB
    print(f"Used RAM: {ram.used / (1024**3):.2f} GB")            #9.94 GB
    print(f"RAM Usage: {ram.percent}%")
    print()

def get_cpu_info():
    print("===== CPU Information =====")
    print("CPU Usage:", psutil.cpu_percent(interval=1), "%")  #3.9 %
    print("CPU Cores:", psutil.cpu_count(logical=True))       #12
    print("Physical Cores:", psutil.cpu_count(logical=False)) # 6
    print()

def get_disk_info():
    print("===== Disk Information =====")
    disk = psutil.disk_usage('/')
    print(f"Total Disk: {disk.total / (1024**3):.2f} GB")  #475.48 GB
    print(f"Used Disk: {disk.used / (1024**3):.2f} GB")    #379.53 GB
    print(f"Free Disk: {disk.free / (1024**3):.2f} GB")    #95.95 GB
    print(f"Disk Usage: {disk.percent}%")                  #79.8 %
    print()

def get_uptime():
    print("===== System Uptime =====")
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    now = datetime.datetime.now()
    uptime = now - boot_time

    print("Boot Time:", boot_time.strftime("%Y-%m-%d %H:%M:%S"))  #Boot Time: 2025-11-24 09:31:30
    print("Uptime:", uptime)   #Uptime: 3 days, 10:22:30.895134
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
