#!/usr/bin/python3
"""
Fabric Script with function do_pack:
    zips in format .tgz the static files
"""
import os
from fabric.api import local
import datetime


def do_pack():
    ctime = datetime.datetime.now()
    time_format = ctime.strftime("%Y%m%d%H%M%S")
    version_n = "versions/web_static_{}.tgz".format(time_format)

    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static/".format(version_n))
        return version_n
    except:
        return None
