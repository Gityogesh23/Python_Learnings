import os

command="uptime"#load avg
commannd="date" #date

def check_cpu(command): #defining a function
    print(os.system(command))
def check_date(command): #defining a function
    print(os.system(command))
def check_ram(command):
    print(os.system(command))

#check_ram("free -h") #to check RAM usage on Ubuntu
check_ram("sudo dmidecode -t memory") #on windows -->To check RAM