#!/usr/bin/python3
""" this script that geneartes a .tgz archive from all the web_static """


from fabric.api import local
from datetime import datetime


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
