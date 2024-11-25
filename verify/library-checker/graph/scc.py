# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/scc

import pyrival.misc.FastIO  # noqa
from pyrival.graphs.scc import find_SCC


def main():
    N, M = map(int, input().split())

    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)

    scc = find_SCC(graph)

    print(len(scc))
    for component in scc:
        print(len(component), *component)


if __name__ == "__main__":
    main()
