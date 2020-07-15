#!/usr/bin/env python
## -*- python -*-
#
# Copyright(c) 2020 BD7MQB Michael Choi <bd7mqb@qq.com>
# This is free software, licensed under the GNU GENERAL PUBLIC LICENSE, Version 2.0
#

PATH = './tmp/records/'

STATIONS = {
    'szsdr': {                                      ## name of kiwisdr station
        'server_host': 'szsdr.ddns.net',            ## url of your kiwisdr station
        'server_port': 8073,                        ## port of kiwi
        'password': 'passwor0d',                    ## password if needed
        'tlimit_password': 'passwor0d',             ## password to bypass time limited, if needed
        'callsign': 'BD7MQB',                       ## your callsign
        'grid': 'OL72an',                           ## your grid
    },
    
    'czsdr': {
        'server_host': 'cz.kiwisdr.go1982.com', 
        'server_port': 8073,
        'password': 'passwor0d',
        'tlimit_password': 'passwor0d',
        'callsign': 'BD7MQB-2',
        'grid': 'OM88co',
    },
    
    'cdsdr': {                                      ## name of kiwisdr station
        'server_host': 'cdkiwisdr.ddns.net',        ## url of your kiwisdr station
        'server_port': 8073,                        ## port of kiwi
        'password': 'passwor0d',                    ## password if needed
        'tlimit_password': 'passwor0d',             ## password to bypass time limited, if needed
        'callsign': 'BD7MQB-3',                     ## your callsign
        'grid': 'OM10wq',                           ## your grid
    },
}

SCHEDULES = {
    '*': {'cdsdr': [20]},

    # '21:00-08:00': {'czsdr': [20, 30, 40, 60, 80, 160]},
    # '08:00-14:30': {'czsdr': [10, 12, 15, 17, 20, 30]},
    # '14:30-21:00': {'czsdr': [10, 15, 17, 20, 30, 40]},


    ## for test
    # '*': {'cdsdr': [20]},
    # '*': {'szsdr': [20,30], 'czsdr': [20,30]},
    # '14:00-17:08': {'szsdr': [40, 20], 'czsdr': [40]},
    # '20:00-20:51': {'szsdr': [20, 60]},
    # '20:51-22:00': {'szsdr': [40, 30, 20], 'czsdr': [20, 40]},
    # '*': {'szsdr': [10, 12, 15, 17, 20, 30, 40, 60, 80, 160]},
    # '21:00-08:00': {'szsdr': [10, 12, 15, 17, 20, 30, 40, 60, 80, 160], 'czsdr': [20, 30, 40, 60, 80, 160]},
    # '08:00-14:30': {'szsdr': [10, 12, 15, 17, 20, 30, 40, 60, 80, 160], 'czsdr': [10, 12, 15, 17, 20, 30]},
    # '14:30-21:00': {'szsdr': [10, 12, 15, 17, 20, 30, 40, 60, 80, 160], 'czsdr': [10, 15, 17, 20, 30, 40]},
    # end for test
}