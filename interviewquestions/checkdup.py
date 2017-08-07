# The below code will group two more identical files into a list

import os,sys
import hashlib

def findduplicates(dir):
    matches = []
    #outFiles = []
    hashes = {}
    for fname in os.walk(dir):
        md5 = hashlib.md5()
        hasher = md5.update(open(f).read())
        hashvalue = hasher.digest()
        #data = f.read()
        if hashes.has_key(hashValue):
            matches.append(fileName)
        else:
            hashes[hashValue] = fileName

    return matches
    return hashes

dir1 = "/home/user"
print findduplicates(dir1)
