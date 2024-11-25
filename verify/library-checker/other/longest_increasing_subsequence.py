# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/longest_increasing_subsequence

import pyrival.misc.FastIO  # noqa
from pyrival.misc.lis import lis


def main():
    N = int(input())
    A = [int(Ai) for Ai in input().split()]

    i = lis(A)
    print(len(i))
    print(*i)


if __name__ == "__main__":
    main()
