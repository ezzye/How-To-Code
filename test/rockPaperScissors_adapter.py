"""
API adapter for rockPaperScissors CLI (command line interface)
written in python
"""

from subprocess import Popen, PIPE, STDOUT
from tempfile import NamedTemporaryFile
import os

_interpreter_and_script = ['python', 'rockPaperScissors.py']

def run_rockPaperScissors(input_text):
    """
    The default method when we don't care which method to use.
    """
    return run_rockPaperScissors_pipe(input_text)


def run_rockPaperScissors_pipe(input_text):
    """
    Simulate: echo 'some input' | python rockPaperScissors.py
    """
    pipe = Popen(_interpreter_and_script, stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    output = pipe.communicate(input=input_text)[0]
    return output.rstrip()

def run_rockPaperScissors_file(input_text):
    """
    Simulate: python rockPaperScissors.py fileName
    """
    temp_file = NamedTemporaryFile(delete=False)
    temp_file.write(input_text)
    temp_file.close()
    interp_script_and_fileName = _interpreter_and_script
    interp_script_and_fileName.append(temp_file.name)
    pipe = Popen(interp_script_and_fileName, stdout=PIPE, stderr=STDOUT)
    output = pipe.communicate()[0]
    os.unlink(temp_file.name)
    return output.rstrip()
