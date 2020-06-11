import os
import platform
import shutil

PLATFORM_NAME = platform.system()



#======================================================================================================================================================================================================================
# ctypes 系列
def ctypes_cpp2o(cppfile):
    if PLATFORM_NAME == "Linux":
        ofile = "{}.o".format(cppfile.split(".cpp")[0])
        commands = [
            "gcc",
            "-pthread",
            "-DNDEBUG",
            "-g",
            "-fwrapv",
            "-O2",
            "-Wall",
            "-g",
            #"-fstack-protector-strong",
            "-Wformat",
            "-Werror=format-security",
            #"-Wdate-time",
            "-D_FORTIFY_SOURCE=2",
            "-fPIC",
            "-I.",
            "-I/usr/include/python3.6m",
            "-c",
            cppfile,
            "-o",
            ofile,
            "-std=c++11"
        ]
        print(" ".join(commands))
        os.system(" ".join(commands))
        return ofile
    else:
        exit()


def ctypes_o2so(ofile):
    if PLATFORM_NAME == "Linux":
        sofile = "{}.so".format(ofile.split(".o")[0])
        commands = [
            "g++",
            "-pthread",
            "-shared",
            "-Wl,-O1",
            "-Wl,-Bsymbolic-functions",
            "-Wl,-Bsymbolic-functions",
            "-Wl,-z,relro",
            "-Wl,-Bsymbolic-functions",
            "-Wl,-z,relro",
            "-g",
            #"-fstack-protector-strong",
            "-Wformat",
            "-Werror=format-security",
            #"-Wdate-time",
            "-D_FORTIFY_SOURCE=2",
            ofile,
            "-o",
            sofile
        ]
        print(" ".join(commands))
        os.system(" ".join(commands))
        return sofile
    else:
        exit()


def ctypes_compile(cppfile):
    # 啟動 msvc x86_64
    if PLATFORM_NAME == "Linux":
        ofile = ctypes_cpp2o(cppfile)
        sofile = ctypes_o2so(ofile)
        print("[ctypes_compile] {} --> {} --> {}".format(
            cppfile, ofile, sofile))
