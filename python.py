#! /usr/bin/python3



import cgi
import subprocess
import time

print("content-type:text/html")
print()

#time.sleep(10)

f = cgi.FieldStorage()
cmd = f.getvalue("x")
#print(cmd)
o=subprocess.getoutput("sudo " + cmd)
print(o)