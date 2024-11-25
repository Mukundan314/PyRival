# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/factorize

import pyrival.misc.FastIO  # noqa
from pyrival.algebra.factors import prime_factors


def main():
    Q = int(input())

    for _ in range(Q):
        a = int(input())

        x = []
        for p, e in prime_factors(a).items():
            x.extend([p] * e)
        x.sort()

        print(len(x), *x)


if __name__ == "__main__":
    main()
