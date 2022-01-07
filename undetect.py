import re

strtorepl = b"Cheat Engine"
repldastr = b"Check Cached"

def changeFile(fname, strrepl, replstr):
    f = open(fname, "rb")
    data = f.read()
    f.close()
    
    data = data.replace(strrepl, replstr)
    
    f = open(fname, "wb")
    f.write(data)
    f.close()
    
files = ["cheatengine-x86_64.exe", "cheatengine-i386.exe", "cheatengine-x86_64-SSE4-AVX2.exe"]

for file in files:
    changeFile(file, strtorepl, repldastr)
    print(f"File {file} patched")
