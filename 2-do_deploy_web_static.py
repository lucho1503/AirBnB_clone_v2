#!/usr/bin/python3
# this script distributes an archive in my servers

from fabric.api import *
import os

env.hosts = ['35.237.185.211', '54.160.144.29']


def do_deploy(archive_path):
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
