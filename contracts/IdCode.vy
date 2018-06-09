# Flag that only allows contract initialization to happen once
initialised: public(bool)
# Who deployed the contract and who can change pool_signature
owner: public(address)
# pk of the signature intended to be used in pool
signature: public(address)


@public
def init( _signature: address):
    assert not self.initialised
    
    self.initialised = True
    self.owner = msg.sender
    self.signature = _signature
