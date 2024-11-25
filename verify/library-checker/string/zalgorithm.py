# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/zalgorithm

import pyrival.misc.FastIO  # noqa
from pyrival.strings.z_algorithm import z_function


def main():
    S = input()
    print(*z_function(S))


if __name__ == "__main__":
    main()
