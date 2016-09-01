#!/usr/bin/env python

from hvac import Client
from vaults import GetVaults
from collect_keys import ReadYaml

class UnsealVault(object):

    def __init__(self):
        self.hosts = GetVaults().return_ecs_vaults()
        self.secrets = ReadYaml.return_yaml_data()
        self.key_list = self.secrets()['keys']

    def client(self, host):
        return Client(url="https://{0}:8200".format(host), token=self.secrets['token'], verify=False)

    def check_seal(self):
        'Will return a list of all vault instances that are SEALED'
        print "Checking Vaults to determine if they are sealed"
        return [host for host in self.hosts if self.client(host).is_sealed()]

    def unseal_vault(self):
        'For every vault that is sealed, we will unseal with all keys at once (3)'
        sealed_vaults = self.check_seal()
        if sealed_vaults:
            print sealed_vaults
            for vault in sealed_vaults:
                self.client(vault).unseal_multi(self.key_list)
                print "Unsealed vault: {0}".format(vault)


if __name__ == '__main__':
    vault = UnsealVault()
    vault.unseal_vault()
