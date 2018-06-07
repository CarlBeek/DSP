import scheme as bls

t = None
n = None


def key_gen():
    if t is None or n is None:
        raise Exception('t or n not initialized')
    if t > n or t <= 0:
        raise AssertionError('t must be <= n and t > 0')
    return None


def partial_sign(m):
    return None


def partial_verify(m, pk):
    return verify(m, pk)

def public_key_reconstruction(pks):
    return None

def signature_reconstruction(m, sigmas):
    return None


def verify(m, pk):
    return bls.verify(m, pk)
