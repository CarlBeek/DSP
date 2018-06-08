import scheme as bls
from utils import *
from environment import *
from functools import reduce
from random import SystemRandom

t = None
n = None


def key_gen():
    # Todo: Move away from centralised key_generation
    if t is None or n is None:
        raise Exception('t or n not initialized')
    if t > n or t <= 0:
        raise AssertionError('t must be <= n and t > 0')
    v = [o.random() for _ in range(0, t)]
    sk = [poly_eval(v, i) % o for i in range(1, n + 1)]
    pk = [xi*g2 for xi in sk]
    return sk, pk


def partial_sign(m, sk):
    return bls.sign(m, sk)


def partial_verify(pk, sig, m):
    return verify(pk, sig, m)


def public_key_reconstruction(pks):
    pks = [pks[i] * lagrange_coefficient(t, o, i + 1) for i in range(t)]
    pk = reduce(lambda a, b: a + b, pks)
    return pk


def signature_reconstruction(m, sigmas):
    # # Filter out the invalid signatures by checking all of them (required for robustness)
    # sigmas = list(filter(lambda a: partial_verify(m, a), sigmas))

    # Check that there are sufficient signatures remaining
    if len(sigmas) <= t:
        raise AssertionError('At least t + 1 valid signatures are needed to recover a valid group signature.')

    # Raise each sigma to it's lagrangian co-efficient
    sigmas = [sigmas[i]*lagrange_coefficient(t, o, i+1) for i in range(t)]
    # combine sigmas via multiplication
    sigma = reduce(lambda a, b: a+b, sigmas)
    return sigma


def verify(pk, sig, m):
    return bls.verify(pk, sig, m)


if __name__ == '__main__':
    t = 3
    n = 6

    (sks, pks) = key_gen()
    pk = public_key_reconstruction(pks)
    m = 'Banana'
    sigmas = [partial_sign(m, s) for s in sks]
    ver = [partial_verify(pks[i], sigmas[i], m) for i in range(len(sigmas))]
    sigma = signature_reconstruction(m, sigmas)
    print(verify(pk, sigma, m))
