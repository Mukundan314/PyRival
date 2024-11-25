# disabled: PROBLEM https://judge.yosupo.jp/problem/kth_term_of_linearly_recurrent_sequence

import pyrival.misc.FastIO  # noqa
import pyrival.numerical.berlekamp_massey
from pyrival.numerical.berlekamp_massey import linear_rec

pyrival.numerical.berlekamp_massey.MOD = 998244353


def main():
    d, k = map(int, input().split())
    a = [int(ai) for ai in input().split()]
    c = [int(ai) for ai in input().split()]

    print(linear_rec(a, c, k))


if __name__ == "__main__":
    main()
