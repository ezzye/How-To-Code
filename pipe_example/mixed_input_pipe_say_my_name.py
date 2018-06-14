# mixed_input_pipe_say_my_name.py
import subprocess
import sys

proc = subprocess.Popen(["python", "say_my_name.py"], stdin=subprocess.PIPE)

proc.stdin.write("matthew\n")
proc.stdin.write("Errol Elliott\n")
proc.stdin.write("Buzz Lightyear\n")

while proc.returncode is None:
    i = sys.stdin.read(1)
    # print "****{0}*****\n".format(i)
    if i == '':
        proc.stdin.close()
        break
    proc.stdin.write(i)
    proc.poll()

while proc.returncode is None:
    proc.poll()
