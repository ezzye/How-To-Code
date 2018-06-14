# run_say_my_name.py
import subprocess
import sys

proc = subprocess.Popen(["python","say_my_name.py"])

while proc.returncode is None:
    proc.poll()
