#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import paramiko


def sftp_upload_file(host, user, pwd):
    try:
        transport = paramiko.transport((host, 22))
        transport.connect(username=user, password=pwd)
        sftp = paramiko.SFTPClient.from_transport(transport)
        for root, dirs, files in os.walk("pyinstaller", topdown=False):
        	for name in files:
        		sftp.put(os.path.join(root, name),('~/bak/'+os.path.join(root, name)))
        pass
    except Exception as e:
        print e

if __name__ == '__main__':
	host = "114.215.142.52"
	user = "root"
	pwd = "Cm19960330!"
	sftp_upload_file(host,user,pwd)