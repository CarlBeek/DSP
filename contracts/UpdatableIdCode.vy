# Flag that only allows contract initialization to happen once
initialised: public(bool)
# Who deployed the contract and who can change pool_signature
owner: public(address)
# pk of the signature intended to be used in pool
signature: public(address)
# Staged verison of the new signature
proposed_signature: public(address)
# When the signature update will be possible in blocks
update_block: public(uint256)


# ****** Pre-defined Constants ******
EPOCH_LENGTH: uint256


@public
def init( _signature: address):
    assert not self.initialised
    
    self.initialised = True
    self.owner = msg.sender
    self.signature = _signature
    self.proposed_signature = _signature
    self.update_block = block.number
    
    self.EPOCH_LENGTH = 50
    

@public
def propose_new_signature(_proposed_signature: address):
    assert msg.sender == self.owner
    # Signature may only be updated next epoch
    self.update_block = (block.number/self.EPOCH_LENGTH + 1) * self.EPOCH_LENGTH
    self.proposed_signature = _proposed_signature


@public
def update_signature():
    assert msg.sender == self.owner
    assert block.number >= self.update_block
    self.signature = self.proposed_signature
