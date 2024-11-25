# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/suffixarray

import pyrival.misc.FastIO  # noqa
from pyrival.strings.suffix_array import SAIS


def main():
    S = input()
    print(*SAIS([ord(Si) - 97 for Si in S]))


if __name__ == "__main__":
    main()
