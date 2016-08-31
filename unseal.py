#!/usr/bin/env python

from hvac import Client
from vaults import GetVaults
from args import GetArgs

class UnsealVault(object):

    def __init__(self):
        self.hosts = GetVaults().return_ecs_vaults()
        self.args = GetArgs().get_args()

    def client(self, host):
        return hvac.Client(url="https://{0}:8200".format(host), token=self.args.token, verify=False)

    def key_list(self):
        return [self.args.key1, self.args.key2, self.args.key3]

    def check_seal(self):
        'Will return a list of all vault instances that are SEALED'
        print "Checking Vaults to determine if they are sealed"
        return [host for host in self.hosts if self.client(host).is_sealed()]

    def unseal_vault(self):
        'For every vault that is sealed, we will unseal with all keys at once (3)'
        sealed_vaults = self.check_seal()
        if sealed_vaults:
            for vault in sealed_vaults:
                self.client(vault).unseal_multi(self.key_list())
                print "Unsealed vault: {0}".format(vault)


if __name__ == '__main__':
    vault = UnsealVault()
    vault.unseal_vault()
