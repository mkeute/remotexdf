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
        cfg.read('/home/marius/Documents/servercfg.ini')        
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect( hostname = cfg['server']['IP'], username = cfg['server']['username'], key_filename=cfg['server']['keyfile'])
        self.client = client.open_sftp()
        
        
        
server = SFTP()

# import pyxdf
# from pyxdf.pyxdf import open_xdf
xdf_example = '/mnt/data/data03/sleep_study/Study_1_data/Raw_data/Calibration/0RCB4IRJ_2_calibration/recording_R001.xdf'
xdf_local='/home/marius/Downloads/recording_R001.xdf'
# dat = load_remotexdf(xdf_local)
# def load(xdf_example):

f = server.client.open(xdf_example, 'rb')
f.prefetch()
dat = load_remotexdf(f)
f.close()