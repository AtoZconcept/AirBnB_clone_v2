#!/usr/bin/python3
# Deploy archive!


from fabric.api import run, env, put
from os.path import exists

env.hosts = ['100.26.167.191', '54.173.241.59']


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

        # Delete the symbolic links from the web server
        run("rm -rf /data/web_static/current")

        # Create a new the symbolic link
        run("ln -s {} /data/web_static/current".format(path))

        print("New version deployed!")
    except Exception:
        return False
    return True
