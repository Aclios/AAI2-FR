import hashlib

def check_hash(filepath,hash):
    with open(filepath,mode='rb') as f:
        data = f.read()
    md5 = hashlib.md5(data).digest()
    return md5 == hash






