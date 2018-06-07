from bplib.bp import BpGroup
import sha3

G = BpGroup()
g1 = G.gen1()
g2 = G.gen2()
e = G.pair
o = G.order()


def hash(m):
    m = str(m)
    enc = m.encode('utf-8')
    return sha3.keccak_256(enc).digest()
