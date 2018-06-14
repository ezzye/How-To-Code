# external_pipe_say_my_name_constant.py

# mkfifo input_pipe
# mkfifo output_pipe

import subprocess

with open("output_pipe", "w") as output_pipe:
    proc = subprocess.Popen(["gstdbuf", "-o0", "python", "say_my_name.py"],
        stdin=subprocess.PIPE, stdout=output_pipe)

    while True:
        proc.poll()
        if proc.returncode is not None:
            break
        with open("input_pipe","r") as input_pipe:
            proc.stdin.write(input_pipe.read())
