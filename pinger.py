import subprocess
import re

control_path = "www.gmail.com"

ping = subprocess.Popen(
    ["ping", "-s", "4", control_path],
    stdout = subprocess.PIPE,
    stderr = subprocess.PIPE
)

out, err = ping.communicate()
print (out)
