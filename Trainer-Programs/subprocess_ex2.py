import subprocess

p = subprocess.Popen(["python", "script2.py"], stdout=subprocess.PIPE)

print p.communicate()

