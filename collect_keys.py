#!/usr/bin/env python

import yaml

class ReadYaml(object):
    
    def __init__(self, config_file='./keys.yml'):
        self.config_file = config_file

    def return_yaml_data(self):
        with open(self.config_file, 'r') as stream:
            return yaml.load(stream)

if __name__ == '__main__':
    print ReadYaml().return_yaml_data()['keys']
