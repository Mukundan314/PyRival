# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum

import pyrival.misc.FastIO  # noqa
from pyrival.data_structures.FenwickTree import FenwickTree


def main():
    N, Q = map(int, input().split())
    a = FenwickTree([int(ai) for ai in input().split()])

    for _ in range(Q):
        t, *args = map(int, input().split())

        if t == 0:
            a.update(args[0], args[1])
        else:
            print(a.query(args[1]) - a.query(args[0]))


if __name__ == "__main__":
    main()
