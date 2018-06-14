from radish import given, when, then
import subprocess
import sys
import time

# {NAME:TYPE} as argument see http://radish.readthedocs.io/en/latest/tutorial.html

@given("I have input {number1:g}")
def have_input(step, number1):
    step.context.number1 = number1
# see https://lyceum-allotments.github.io/2017/03/python-and-pipes-part-5-subprocesses-and-pipes/

@when("I check them")
def check_them(step):
    fw = open("tmpout", "wb")
    fr = open("tmpout", "r")
    proc = subprocess.Popen(["python","rockPaperScissors.py"], stdin=subprocess.PIPE, stdout=fw, stderr = fw, bufsize = 1)
    proc.stdin.write(str(int(step.context.number1))+"\n")
    proc.stdin.write("n\n")
    proc.stdin.close()

    while proc.returncode is None:
        proc.poll()

    step.context.result = fr.read()
    print step.context.result


@then("I expect to play then asked, {result:w}")
def win_or_lose(step,result):
    assert result in step.context.result
