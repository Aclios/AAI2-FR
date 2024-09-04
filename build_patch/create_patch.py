import bsdiff4
import hashlib
import sys

class NDSPatch:
    def __init__(self,source_file,dist_file,credits_file):
        self.magic = b'NDSP'
        with open(source_file,mode='rb') as f:
            source_data = f.read()
        self.source_hash = hashlib.md5(source_data).digest()
        with open(dist_file,mode='rb') as f:
            dist_data = f.read()
        self.patch = bsdiff4.diff(source_data,dist_data)
        with open(credits_file,mode='rb') as f:
            self.credits = f.read()

    def write_patch(self,path):
        with open(path,mode='wb') as f:
            f.write(self.magic)
            f.write(bytes(12))
            f.write(self.source_hash)
            f.write(self.credits)
            patch_pos = f.tell()
            f.write(self.patch)
            f.seek(4)
            f.write(len(self.credits).to_bytes(4,'little'))
            f.write(patch_pos.to_bytes(4,'little'))
            f.write(len(self.patch).to_bytes(4,'little'))


if __name__ == '__main__':
    print("Calcul du patch...")
    ndsp = NDSPatch(sys.argv[1],sys.argv[2],sys.argv[3])
    print("Ecriture...")
    ndsp.write_patch('patch.ndspatch')
    print("Fini!")