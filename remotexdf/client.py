#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 08:35:18 2020

@author: marius
"""

import paramiko
import configparser
from pathlib import Path
from remotexdf import load_remotexdf
class SFTP():
    def __init__(self):
        cfg = configparser.ConfigParser()
        cfg.read('~/Documents/servercfg.ini')        
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect( hostname = cfg['server']['IP'], username = cfg['server']['username'], key_filename=cfg['server']['keyfile'])
        self.client = client.open_sftp()
        
        
