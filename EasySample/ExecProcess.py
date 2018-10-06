import subprocess
cmd = "dir C:\\"
# subprocess.call(cmd , shell=True)

proc = subprocess.Popen(cmd, shell=True)
proc.wait()