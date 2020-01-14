#!/usr/bin/python3
# this script distributes an archive in my servers

from fabric.api import *
import os

env.user = 'ubuntu'
env.hosts = ['35.243.129.221', '35.231.144.56']


def do_deploy(archive_path):
    if os.path.exists(archive_path):
        put(archive_path, '/tmp/')
        file_path = archive_path.split("/")[-1]
        path_f = '/data/web_static/releases/{}'.format(file_path.split(".")[0])
        run('mkdir -p {}'.format(path_fi))
        run('tar -xzf /tmp/{} -C {}'.format(file_path, path_fi))
        run('rm /tmp/{}'.format(file_path))
        run('mv {}/web_static/* {}'.format(path_fi, path_fi))
        run('rm -rf {}/web_static'.format(path_fi))
        run('rm -rf /data/web_static/current')
        run('ls -s {} /data/web_static/current'.format(path_fi))
        print('its is a deployment')
        return True
    return False
