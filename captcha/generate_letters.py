from shutil import copyfile

from os import listdir
from os.path import isfile, join
import hashlib

salt = "fUn@m3nT@L777"

only_files = [f for f in listdir("./source") if isfile(join("./source", f))]

for filename in only_files:
    hash_object = hashlib.md5((filename + salt).encode())
    newname = hash_object.hexdigest()
    print(filename + " >>> " + newname)
    copyfile("./source/" + filename, "./output/" + newname + ".png")
