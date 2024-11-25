# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/primitive_root

import pyrival.misc.FastIO  # noqa
from pyrival.algebra.primitive_root import primitive_root


def main():
    Q = int(input())

    for _ in range(Q):
        p = int(input())
        r = primitive_root(p)
        print(1 if r == p else r)


if __name__ == "__main__":
    main()
