import os #import os → lets you run system-level commands (like dir, ls, uptime, etc.).
import datetime #import datetime → used for working with dates and time.

command ="winget "
def run_command(command):
    return os.system(command) #It takes a command string (like "uptime" or "date").
#os.system() gives the output in the terminal and
# returns the command’s exit code (0 = success).
def show_date(): #define fun
    return datetime.datetime.today()

today=show_date() #call fun which defined above
print(today)
