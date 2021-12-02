import re

def changeFile(name):
    in_file = open(name, "rb")
    data = in_file.read()
    in_file.close()

    data = data.replace(b"cheatengine", b"checkcached")
    data = data.replace(b"CheatEngine", b"CheckCached")
    data = data.replace(b"Cheatengine", b"Checkcached")
    data = data.replace(b"cheatEngine", b"checkCached")
    data = data.replace(b"Cheat Engine", b"Check Cached")
    data = data.replace(b"CHEATENGINE", b"CHECKCACHED")

    out_file = open(name, "wb")
    out_file.write(data)
    out_file.close()
    
    return data

files = ["cheatengine-i386.exe", "cheatengine-x86_64.exe"]

for i in files:
    changeFile(i)
    print(f"File {i} patched")
