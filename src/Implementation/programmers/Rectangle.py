from math import gcd


def solution(w, h):
    a = gcd(w, h)
    ww = int(w / a)
    hh = int(h / a)
    t = ww * hh - (ww - 1) * (hh - 1)

    return w * h - a * t