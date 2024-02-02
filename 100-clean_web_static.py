#!/usr/bin/python3
# Keep it clean!


from fabric.api import *

env.hosts = ['100.26.167.191', '54.173.241.59']
env.user = "ubuntu"

def clean_local_archieve(number):
	"""clean out-dated achieve files"""

	local(
		"cd versions/ && ls -t | tail -n +{} | sudo xargs rm -rf"
		.format(number)
	)


def clean_remote_archieve(number):
	"""clean out-dated remote achieve"""

	path = "/data/web_static/releases"
	run("cd {} && ls -t | tail -n +{} | sudo xargs rm -rf"
	 .format(path, number))


@task
def do_clean(number=0):
	"""to execute the clean method"""

	number =  int(number)
	if number < 1:
		number = 2
	else:
		number += 1
	clean_local_archieve(number)
	clean_remote_archieve(number)