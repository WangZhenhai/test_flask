# encoding = utf-8
import subprocess
import sys

print ("run test script for python")

exec = sys.executable
file = "test/test.py"
subprocess.check_output ([exec, file], stderr=subprocess.STDOUT, timeout=5)
