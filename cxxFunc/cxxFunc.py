import ctypes
import os

cxxFunc = ctypes.cdll.LoadLibrary("./ctypes/cxxFunc.so")
cxxFunc.cMonteCarloPi.argtypes = [ctypes.c_int]
cxxFunc.cMonteCarloPi.restype = ctypes.c_double
cxxFunc.cFWA.argtypes = [
    ctypes.POINTER(ctypes.c_char_p),
    ctypes.POINTER(ctypes.c_double), ctypes.c_int
]
cxxFunc.cFWA.restype = None


def cFWA(E):
    # 把字串變成 bytes !!
    keys = [_str.encode("utf8") for _str in list(E.keys())]
    vals = list(E.values())
    # 把 list 轉成 ctypes pointer
    p_keys = (ctypes.c_char_p * len(keys))(*keys)
    p_vals = (ctypes.c_double * len(vals))(*vals)
    # 這邊不回傳 !!
    cxxFunc.cFWA(p_keys, p_vals, len(vals))

def cMonteCarloPi(num):
    return cxxFunc.cMonteCarloPi(num)


if __name__ == '__main__':
    print(cMonteCarloPi(10000000))
