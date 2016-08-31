#!/usr/bin/env python

from boto3 import client as botoclient

class GetVaults(object):

    def __init__(self, region='us-west-2'):
        self.region = region
        self.client = botoclient('ec2', region_name=self.region)

    def return_ecs_vaults(self):
        return [x['Instances'][0]['PrivateIpAddress'] for x in self.client.describe_instances(Filters=[{'Name':'tag:Name', 'Values':['ecs-services']}])['Reservations']]


if __name__ == '__main__':
    hosts = GetVaults()
    print hosts.return_ecs_vaults()
