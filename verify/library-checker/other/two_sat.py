# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/two_sat

import pyrival.misc.FastIO  # noqa
from pyrival.data_structures.TwoSat import TwoSat


def main():
    _, _, N, M = input().split()
    N, M = int(N), int(M)

    two_sat = TwoSat(N)

    for _ in range(M):
        a, b, _ = map(int, input().split())
        a -= a > 0
        b -= b > 0
        two_sat.either(a, b)

    sat, sol = two_sat.solve()

    if sat:
        print("s SATISFIABLE")
        print("v", *[i if sol_i else -i for i, sol_i in enumerate(sol, start=1)], 0)
    else:
        print("s UNSATISFIABLE")


if __name__ == "__main__":
    main()
