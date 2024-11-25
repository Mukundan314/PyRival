# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/enumerate_primes

import pyrival.misc.FastIO  # noqa
from pyrival.algebra.sieve import prime_list


def main():
    N, A, B = map(int, input().split())

    p = prime_list(N)

    print(len(p), len(range(B, len(p), A)))
    print(*p[B::A])


if __name__ == "__main__":
    main()
