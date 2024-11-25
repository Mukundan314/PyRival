# competitive-verifier: PROBLEM https://judge.yosupo.jp/problem/convolution_mod

import pyrival.misc.FastIO  # noqa
from pyrival.algebra.ntt import ntt_conv


def main():
    N, M = map(int, input().split())
    a = [int(ai) for ai in input().split()]
    b = [int(bi) for bi in input().split()]
    print(*ntt_conv(a, b))


if __name__ == "__main__":
    main()
