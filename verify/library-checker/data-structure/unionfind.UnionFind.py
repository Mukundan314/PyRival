# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/unionfind

import pyrival.misc.FastIO  # noqa
from pyrival.data_structures.DisjointSetUnion import UnionFind


def main():
    N, Q = map(int, input().split())

    uf = UnionFind(N)

    for _ in range(Q):
        t, u, v = map(int, input().split())

        if t == 0:
            uf.union(u, v)
        elif t == 1:
            print(1 if uf.find(u) == uf.find(v) else 0)


if __name__ == "__main__":
    main()
