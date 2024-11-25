# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/discrete_logarithm_mod

import pyrival.misc.FastIO  # noqa
from pyrival.algebra.discrete_log import discrete_log


def main():
    T = int(input())

    for _ in range(T):
        X, Y, M = map(int, input().split())
        K = discrete_log(X, Y, M)

        if Y == 1 or M == 1:
            print(0)
        elif K is None:
            print(-1)
        else:
            print(K)


if __name__ == "__main__":
    main()
