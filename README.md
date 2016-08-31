# vault-ecs

This code will check all vault instances and check if they are sealed. If they return sealed, it will unseal them.

## Requirements:

1) Vault token which is passed in as a parameter

2) Vault unseal keys (3 are required to unseal the vault)

## Usage:

```
usage: unseal.py [-h] -t TOKEN -k1 KEY1 -k2 KEY2 -k3 KEY3

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Token
  -k1 KEY1, --key1 KEY1
                        First Unseal Key
  -k2 KEY2, --key2 KEY2
                        Second Unseal Key
  -k3 KEY3, --key3 KEY3
                        Third Unseal Key
```
