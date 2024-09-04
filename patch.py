import bsdiff4

class NDSPatch:
    def __init__(self,filepath):
        with open(filepath,mode='rb') as f:
            magic = f.read(4)
            if magic != b'NDSP':
                raise Exception("Bad magic")
            credits_size = int.from_bytes(f.read(4),'little')
            patch_offset = int.from_bytes(f.read(4),'little')
            patch_size = int.from_bytes(f.read(4),'little')
            self.source_hash = f.read(16)
            self.credits = f.read(credits_size).decode('utf-8')
            f.seek(patch_offset)
            self.patch = f.read(patch_size)


    def patch_file(self,src_file,dst_file):
        with open(src_file,mode='rb') as f:
            data = f.read()
        patched_data = bsdiff4.patch(data,self.patch)
        with open(dst_file,mode='wb') as f:
            f.write(patched_data)
