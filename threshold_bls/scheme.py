from environment import *


def key_gen():
    sk = o.random()
    pk = sk*g2
    return sk, pk


def sign(m, sk):
    assert len(m) > 0
    m = hash(m)
    h = G.hashG1(m)
    sigma = sk*h
    return sigma


def verify(pk, sigma, m):
    assert len(m) > 0
    m = hash(m)
    h = G.hashG1(m)
    return not h.isinf() and e(sigma, g2) == e(h, pk)


def main():
    (sk, pk) = key_gen()
    m = 'Hi Alice'
    sigma = sign(m, sk)
    assert verify(pk, sigma, m)
    print('Success!')


if __name__ == '__main__':
    main()
