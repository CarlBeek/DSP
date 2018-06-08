import scheme as bls
from utils import *
from environment import *
from functools import reduce
from random import SystemRandom

t = None
n = None


def key_gen():
    if t is None or n is None:
        raise Exception('t or n not initialized')
    if t > n or t <= 0:
        raise AssertionError('t must be <= n and t > 0')
    # Todo: Finnish me!!
    return None


def key_gen_1():
    rng = SystemRandom()
    a = [rng.randint(0, int(G.ord)) for i in range(2 * t + 1)]
    b = [rng.randint(0, int(G.ord)) for i in range(2 * t + 1)]
    sigmas = list(map(lambda j: poly_eval(a, j), range(0, t))) % q
    rhos = list(map(lambda j: poly_eval(b, j), range(0, t))) % q
    As = [e(g*ak, h*bk) for (ak, bk) in (a, b)]
    return sigmas, rhos, As


def key_gen_2(sigmas, rhos, As):
    sigma = sum(sigmas) % q
    rho = sum(rhos) % q
    A = reduce(lambda a, b: a * b, As) % p
    return sigma, rho, A

def key_gen_3(a):
    return None


def partial_sign(m, sk):
    return bls.sign(m, sk)


def partial_verify(m, pk):
    return verify(m, pk)


def public_key_reconstruction(pks):
    # Todo: Finnish me!!
    return None


def signature_reconstruction(m, sigmas):
    # Filter out the invalid signatures by checking all of them (required for robustness)
    sigmas = filter(lambda a: partial_verify(m, a), sigmas)

    # Check that there are sufficient signatures remaining
    if len(sigmas) <= t:
        raise AssertionError('At least t + 1 valid signatures are needed to recover a valid group signature.')

    # Raise each sigma to it's lagrangian co-efficient
    sigmas = [sigmas[i]**lagrange_coefficient(t, o, i+1) for i in range(t)]
    # combine sigmas via multiplication
    sigma = reduce(lambda a, b: a*b, sigmas)
    return sigma


def verify(m, pk):
    return bls.verify(m, pk)
