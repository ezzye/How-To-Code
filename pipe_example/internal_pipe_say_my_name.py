# internal_pipe_say_my_name.py
import subprocess
import sys

proc = subprocess.Popen(["python","say_my_name.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

proc.stdin.write("matthew\n")
proc.stdin.write("Errol Elliott\n")
proc.stdin.write("Buzz Lightyear\n")
proc.stdin.close()

while proc.returncode is None:
    proc.poll()

print "I got back from the program this:\n{0}".format(proc.stdout.read())
