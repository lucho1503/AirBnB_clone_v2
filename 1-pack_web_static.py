#!/usr/bin/python3
#this script that geneartes a .tgz archive from all the web_static

import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """ this function generates a file .tgz from web_static file """
    if not os.path.exists('versions'):
        local("mkdir -p versions")

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = local("tar -cvzf versions/web_static_{}.tgz web_static".
                      format(date))

    if file_name is None:
        return None
    else:
        return ("versions/web_static_{}".format(date))
