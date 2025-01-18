import time
import numpy as np
import struct
import io
import dis

from exbip.framework.parsers.WriterBase import WriterBase
from exbip.descriptors.Primitive import PRIMITIVE_DESCRIPTORS, PRIMITIVE_ENDIAN_DESCRIPTORS

struct_cls = struct.Struct(">I")
pack       = struct_cls.pack
unpack     = struct_cls.unpack


    
class Writer(WriterBase.extended_with(PRIMITIVE_DESCRIPTORS, PRIMITIVE_ENDIAN_DESCRIPTORS)):
    def rw_uint32_test(self, value, endianness=None):
        if endianness is None:
            endianness = self._endianness
        self._bytestream.write(struct.pack(endianness+'I', value))
        return value


repeats = 100
writes  = 100000

for i in range(repeats):
    print(f"Warming up")
    wt = Writer()
    with wt.BytestreamIO() as rw:
        with rw.as_bigendian():
            # (dis.dis(rw.rw_uint32_be))
            # (dis.dis(rw.rw_uint32))
            # assert 0
            for _ in range(writes):
                rw.rw_uint32(10)
            
    
        
t2 = []
for i in range(repeats):
    print(f"Testing write method 2... [{i}]")
    wt = Writer()
    start = time.time()
    with wt.BytestreamIO() as rw:
        for _ in range(writes):
            rw.rw_uint32_e(10, ">")
    t2.append(time.time()-start)
    
t3 = []
for i in range(repeats):
    print(f"Testing write method 3... [{i}]")
    wt = Writer()
    start = time.time()
    with wt.BytestreamIO() as rw:
        for _ in range(writes):
            rw.rw_uint32_be(10)
    t3.append(time.time()-start)

t1 = []
for i in range(repeats):
    print(f"Testing write method 1... [{i}]")
    wt = Writer()
    start = time.time()
    with wt.BytestreamIO() as rw:
        for _ in range(writes):
            rw.rw_uint32(10)
    t1.append(time.time()-start)
    
t4 = []
for i in range(repeats):
    print(f"Testing write method 4... [{i}]")
    wt = Writer()
    start = time.time()
    with wt.BytestreamIO() as rw:
        for _ in range(writes):
            rw.rw_uint32_test(10)
    t4.append(time.time()-start)

t5 = []
for i in range(repeats):
    print(f"Testing write method 5... [{i}]")
    wt = Writer()
    start = time.time()
    stream = io.BytesIO()
    write = stream.write
    for _ in range(writes):
        stream.write(pack(10))
    t5.append(time.time()-start)
    
    
def fmt_res(results):
    r = sorted(results)
    sz = len(results)
    #r = r[int(.33*sz):int(.67*sz)]
    #std = r[int(.67*sz)] - r[int(.33*sz)]
    std = np.std(r)
    return (np.mean(r), std)

def fmt_mn_std(mn, std):
    return f"{mn:.5f}({std:.5f})"


print("=======")
for (mean, std), tag in sorted([(fmt_res(r), i) for i, r in [("patched", t1), ("runtime", t2), ("hardcoded", t3), ("old", t4), ("bare", t5)]]):
    print(f"Timing {tag.ljust(9, ' ')}: [W]", fmt_mn_std(mean, std))
