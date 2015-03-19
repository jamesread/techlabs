import os
from sys import exit
import subprocess

def execute(cmd, shell = False):
	res = subprocess.Popen(cmd.split(" "), stdout = subprocess.PIPE, shell = shell);

	return {
		"output": "",
		"exit": res
	}

def testRoot():
	if (os.getuid() == 0):
		test(True, "You are root")
	else:
		test(False, "You are not running this script as root")

def testExecOutputContains(cmd, search, comment):
	if search in execute(cmd)['output']:
		test(True, comment)
	else:
		test(False, comment)

def testServiceUp(service):
	if execute("systemctl is-active " + service)['output']:
		test(False, service + " is not running")
	else:
		test(True, service + " is running")

def test(result, comment):
	if result:
		resultString = "PASS"
	else:
		resultString = "FAIL"

	print "[ ", resultString, " ] ", comment

	if not result:
		exit(1)
