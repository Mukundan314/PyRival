# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/lca

import pyrival.misc.FastIO  # noqa
from pyrival.graphs.lca import LCA


def main():
    N, Q = map(int, input().split())
    p = [int(pi) for pi in input().split()]

    tree = [[] for _ in range(N)]
    for i, pi in enumerate(p, start=1):
        tree[pi].append(i)

    lca = LCA(0, tree)

    for _ in range(Q):
        u, v = map(int, input().split())
        print(lca(u, v))


if __name__ == "__main__":
    main()
