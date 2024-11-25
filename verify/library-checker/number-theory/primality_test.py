# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/primality_test

import pyrival.misc.FastIO  # noqa
from pyrival.algebra.is_prime import is_prime


def main():
    Q = int(input())

    for _ in range(Q):
        N = int(input())
        print("Yes" if is_prime(N) else "No")


if __name__ == "__main__":
    main()
