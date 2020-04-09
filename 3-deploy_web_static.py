#!/usr/bin/python3
# this script create and distributed a file in a servers


import os
from fabric.api import local
from datetime import datetime
from fabric.api import *

env.hosts = ['35.237.185.211', '54.160.144.29']
path_file = None


def do_pack():
    """ this function generates a file .tgz from web_static file """

    date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz web_static".format(date)

    try:
        local("mkdir -p versions")
        local("tar --create --verbose -z --file={} ./web_static"
              .format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """ distributes an archive to my servers """
    if not os.path.exists(archive_path):
        return False
    try:
        file_path = archive_path.split("/")[-1]
        path_fi = '/data/web_static/releases'
        put("{}".format(archive_path), '/tmp/{}'.format(file_path))
        spl = file_path.split(".")
        sudo('mkdir -p {}/{}/'.format(path_fi, spl[0]))
        new_file = ".".join(spl)
        sudo('tar -xzf /tmp/{} -C {}/{}/'.format(new_file, path_fi, spl[0]))
        sudo('rm /tmp/{}'.format(file_path))
        sudo('mv {}/{}/web_static/* {}/{}/'.format(
            path_fi, spl[0], path_fi, spl[0]))
        sudo('rm -rf {}/{}/web_static'.format(path_fi, spl[0]))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}/{} /data/web_static/current'.format(path_fi, spl[0]))
        print('its is a deployment')
        return True
    except:
        return False


def deploy():
    """ creates and distibutesan archive in my servers """
    global path_file
    if path_file is None:
        path_file = do_pack()
    if path_file is None:
        return False
    return do_deploy(path_file)
