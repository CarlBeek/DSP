from web3 import Web3, HTTPProvider
from collections import defaultdict
from random import random

web3_staking = Web3(HTTPProvider('http://localhost:8545'))


class Node:
    def __init__(self, inbox, uid):
        self.inbox = inbox
        self.id = uid
        self.num_nodes = len(inbox)
        self.address_book = defaultdict(lambda: {})

    def _gossip(self, m, p=.5):
        for k, v in self.inbox.items():
            if random() < p and k != self.id:
                v.put(m)

    def _broadcast(self, m):
        for k, v in self.inbox.items():
            if k != self.id:
                v.put(m)

    def _send(self, m, dest):
        try:
            self.inbox[dest].put(m)
        except KeyError:
            print('Node doesnt exist')


class Identity:
    def __init__(self):
        # The keys to the deployment wallet
        self.wallet_key = {'pk': 0x0, 'sk': 0x0}
        # The portion of the shared key
        self.shared_key = {'pk': 0x0, 'sk': 0x0}
        # The key used for Byzantine Agreement within the pool
        self.pool_key = {'pk': 0x0, 'sk': 0x0}

    def deploy_idcode(self):
        return None
        # Todo: assertion on valid keys
        # Todo: deploy idcode
