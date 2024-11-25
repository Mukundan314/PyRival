# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/sqrt_mod

import pyrival.misc.FastIO  # noqa
from pyrival.algebra.mod_sqrt import mod_sqrt


def main():
    T = int(input())

    for _ in range(T):
        Y, P = map(int, input().split())
        X = mod_sqrt(Y, P)
        print(-1 if X is None else X)


if __name__ == "__main__":
    main()
