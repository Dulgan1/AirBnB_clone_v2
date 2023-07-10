#!/usr/bin/python3
"""
Fabric Script containing do_deploy:
    Deploys archive of static file created by do_pack
"""
import os
from fabric.api import env, run, put
import datetime

env.hosts = ['52.87.255.181', '100.25.119.104']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """do_deploy:
        deploys archive file packed as .tgz to servers
    """
    if not os.path.exists(archive_path):
        return False

    file_name = archive_path.split('/')
    new_name = file_name[1]
    new_var = new_name.split('.')
    path_to_tar = "/data/web_static/releases/{}/".format(new_var[0])
    sym_link = "/data/web_static/current"
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_to_tar))
        run("tar -xzf /tmp/{} -C {}".format(new_name, path_to_tar))
        run("rm /tmp/{}".format(new_name))
        run("mv {}web_static/* {}".format(path_to_tar, path_to_tar))
        run("rm -rf {}".format(sym_link))
        run("ln -s {} {}".format(path_tar, sym_link))
        return True
    except:
        return False
