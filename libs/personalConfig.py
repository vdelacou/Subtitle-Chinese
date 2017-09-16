#!/usr/bin/env python3

import configparser

config = configparser.ConfigParser()
config.read('properties.ini')


def closePersonalConfig():
    with open('properties.ini', 'w') as configfile:
        config.write(configfile)
