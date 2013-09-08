#!/usr/bin/env python

from distutils.core import setup
import os

version = '0.01'

data = dict(
    name = 'mythtv-monitor',
    version = version,
    description = 'mythtv-monitor is used to monitor and handle System Events from MythTV',
    author = 'David Whyte',
    author_email = 'david@thewhytehouse.org',
    packages =      ['monitor'],
    scripts = ['mythtv-monitor'],
    data_files = [('/etc/init', ['mythtv-monitor.conf'])],
    )


setup(**data)