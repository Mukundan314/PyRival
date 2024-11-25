# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/staticrmq

import pyrival.misc.FastIO  # noqa
from pyrival.data_structures.RangeQuery import RangeQuery


def main():
    N, Q = map(int, input().split())
    a = RangeQuery([int(ai) for ai in input().split()])

    for _ in range(Q):
        l, r = map(int, input().split())
        print(a.query(l, r))


if __name__ == "__main__":
    main()
