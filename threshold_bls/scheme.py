import environment as env


def key_gen():
    sk = env.o.random()
    pk = sk*env.g2
    return sk, pk


def sign(m, sk):
    assert len(m) > 0
    m = env.hash(m)
    h = env.G.hashG1(m)
    sigma = sk*h
    return sigma


def verify(pk, sigma, m):
    assert len(m) > 0
    m = env.hash(m)
    h = env.G.hashG1(m)
    return not h.isinf() and env.e(sigma, env.g2) == env.e(h, pk)


def main():
    (sk, pk) = key_gen()
    m = 'Hi Alice'
    sigma = sign(m, sk)
    assert verify(pk, sigma, m)
    print('Success!')


if __name__ == '__main__':
    main()
