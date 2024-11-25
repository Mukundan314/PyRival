# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/shortest_path

import pyrival.misc.FastIO  # noqa
from pyrival.graphs.dijkstra import dijkstra


def main():
    N, M, s, t = map(int, input().split())

    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    dist, parent = dijkstra(graph, s)

    if dist[t] == float('inf'):
        print(-1)
    else:
        path = [t]
        while path[-1] != s:
            path.append(parent[path[-1]])

        print(dist[t], len(path) - 1)
        for i in range(len(path) - 1)[::-1]:
            print(path[i + 1], path[i])


if __name__ == "__main__":
    main()
