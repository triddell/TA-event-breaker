#!/usr/bin/env python3

import configparser, csv

config = configparser.RawConfigParser(allow_no_value=True)
config.optionxform = str


with open('gen/index-time-props.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    cfgfile = open('default/props.conf', 'w')
    
    for row in reader:
        config.add_section(row['SOURCETYPE'])
        config.set(row['SOURCETYPE'],'EVENT_BREAKER_ENABLE','true')
        config.set(row['SOURCETYPE'],'EVENT_BREAKER', row['LINE_BREAKER'])

    config.write(cfgfile)
    cfgfile.close()