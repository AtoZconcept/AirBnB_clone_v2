#!/usr/bin/python3
# Full deployment


from fabric.api import env, local, put, run, runs_once
from os.path import exists
from datetime import datetime

env.hosts = ['100.26.167.191', '54.173.241.59']


@runs_once
def do_pack():
    """generates a .tgz archive from the contents of the web_static"""
    # create the versions folder if it doesn't exist
    local("mkdir -p versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # create a tar zipped achieved
    local("tar -cvzf versions/web_static_{}.tgz web_static".format(timestamp))

    return ("versions/web_static_{}.tgz".format(timestamp))

def do_deploy(archive_path):
    """
    Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")

        basename = archive_path.split("/")[-1]
        filename = basename.split('.')[0]
        path = "/data/web_static/releases/{}/".format(filename)

        # Uncompress the archive to a folder
        run("mkdir -p {}".format(path))
        run('tar -xzf /tmp/{} -C {}'.format(basename, path))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(basename))

        # move the files
        run("mv {0}web_static/* {0}".format(path))

        # Delete the symbolic links from the web server
        run("rm -rf {}web_static".format(path))
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link
        run("ln -s {} /data/web_static/current".format(path))

        print("New version deployed!")
    except Exception:
        return False
    return True

def deploy():
    """
    Fabric script that creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
