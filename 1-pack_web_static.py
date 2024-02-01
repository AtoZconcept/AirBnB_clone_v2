#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the content of the
# web_static folder of your AirBnB Clone repo, using the function do_pack


from fabric.api import local
from datetime import datetime


def do_pack():
	"""generates a .tgz archive from the contents of the web_static"""
	# create the versions folder if it doesn't exist
	local("mkdir -p versions")

	# generate achieve filename with timestamp
	timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
	filename = "versions/web_static_{}.tgz".format(timestamp)

	# create a tar zipped achieved
	file_zip = local("tar -cvzf {} web_static".format(filename))

	if file_zip.succeeded:
		return filename
	else:
		return None
