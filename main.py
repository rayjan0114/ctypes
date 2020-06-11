import timeit
import os
import sys
import platform
import ctypes
from compileDIY import ctypes_compile

E = {
    "c-Q": 2,
    "p-b": 3,
    "0-P": 1,
    "^-&": 20,
    "!-a": 1,
    "d-a": 2,
    "x-q": 1,
    "c-B": 2,
    "a-b": 3,
    "a-v": 1,
    "1-3": 10,
    "1-2": 100,
    "Z-S": 1,
    "A-B": 2,
    "A-C": 3,
    "C-E": 10,
    "A-D": 11,
    "B-D": 2,
    "C-A": 12,
    "A-E": 13,
    "A-Z": 2,
    "G-H": 1,
    "C-G": 5,
    "D-C": 10,
    "A-D": 2,
    "R-A": 3,
    "T-D": 12,
    "C-H": 17,
    "B-X": 10,
    "X-T": 1,
    "E-Q": 3,
    "U-V": 1,
    "V-A": 2,
    "V-B": 3,
    "C-A": 2,
    "E-A": 12,
    "B-C": 100,
    "D-A": 2,
    "A-S": 3,
    "S-Q": 1,
    "Q-A": 2,
    "3-4": 1,
    "4-5": 1,
    "5-6": 1,
    "6-7": 1,
    "7-8": 1,
    "8-9": 1,
    "9-0": 1,
    "9-a": 1,
    "8-a": 1,
    "7-a": 1,
    "z-A": 1,
    "a-B": 1
}



if __name__ == '__main__':
    ROOTPATH = os.path.dirname(os.path.abspath(__file__))

    try:
        #=========================================================================================
        if sys.argv[1] == "--compile-ctypes":
            os.chdir("./ctypes")
            ctypes_compile("cxxFunc.cpp")
            os.chdir(ROOTPATH)
        #=========================================================================================
        if sys.argv[1] == "--run-python":
            from pythonFunc import pythonFunc
            t1 = timeit.default_timer()
            print(pythonFunc.Floyd_Warshall_Algorithm(E))
            print(pythonFunc.MonteCarloPi(10000000))
            t2 = timeit.default_timer()
            print("{} ms".format(1000 * (t2 - t1)))
        #=========================================================================================
        if sys.argv[1] == "--run-ctypes":
            import cxxFunc
            t1 = timeit.default_timer()
            # 這邊不回傳 !!
            cxxFunc.cFWA(E)
            print(cxxFunc.cMonteCarloPi(10000000))
            t2 = timeit.default_timer()
            print("{} ms".format(1000 * (t2 - t1)))

    except Exception as e:
        print(e)
