import time
import numpy as np
import struct
import io
import dis
import ctypes

from exbip.framework.parsers.WriterBase import WriterBase
from exbip.descriptors.Primitive import PRIMITIVE_DESCRIPTORS, PRIMITIVE_ENDIAN_DESCRIPTORS

struct_cls = struct.Struct("<IIIIfIfi")
pack       = struct_cls.pack
unpack     = struct_cls.unpack

class TestStruct1:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40
        self.e = 10.
        self.f = 20
        self.g = 30.
        self.h = -40
        
    def readwrite(self, rw):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_uint32(self.b)
        self.c = rw.rw_uint32(self.c)
        self.d = rw.rw_uint32(self.d)
        self.e = rw.rw_float32(self.e)
        self.f = rw.rw_uint32(self.f)
        self.g = rw.rw_float32(self.g)
        self.h = rw.rw_int32(self.h)

class TestStruct2:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40
        self.e = 10.
        self.f = 20
        self.g = 30.
        self.h = -40
    
    def readwrite(self, rw):
        mems = (self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h)
        rw._bytestream.write(pack(*mems))

def exbip_struct(cls):
    print(cls)
    
    format_string = ""
    
    def mk_fn(index):
        def getter(self):
            return self.buffer[index]
        def setter(self, value):
            self.buffer[index] = value
        
        return property(getter, setter)
    
    initial_buffer = []
    for i, (k, v) in enumerate(cls.__annotations__.items()):
        print(k, v)
        format_string += v.TYPECODE
        setattr(cls, k, mk_fn(i))
        initial_buffer.append(v.value)
    
    setattr(cls, "STRUCT_LE", struct.Struct('<'+format_string))
    setattr(cls, "STRUCT_BE", struct.Struct('>'+format_string))
    
    def init_obj(self):
        self.buffer = initial_buffer
    
    pack   = cls.STRUCT_LE.pack
    unpack = cls.STRUCT_LE.unpack
    iter_unpack = cls.STRUCT_LE.iter_unpack
    def rw(self, rw):
        rw._bytestream.write(pack(*self.buffer))
    
    setattr(cls, "__init__", init_obj)
    setattr(cls, "readwrite", rw)

    return cls
    
    
class uint32:
    TYPECODE = 'I'
    
    def __init__(self, value):
        self.value = value
    
class float32:
    TYPECODE = 'f'
    
    def __init__(self, value):
        self.value = value
    
class int32:
    TYPECODE = 'i'
    
    def __init__(self, value):
        self.value = value
    
@exbip_struct
class TestStruct3:
    a: uint32(10)
    b: uint32(20)
    c: uint32(30)
    d: uint32(40)
    e: float32(10.)
    f: uint32(20)
    g: float32(30.)
    h: int32(-40)
    
    
class TestStruct4(ctypes.Structure):
    _fields_ = [("a", ctypes.c_uint32),
                ("b", ctypes.c_uint32),
                ("c", ctypes.c_uint32),
                ("d", ctypes.c_uint32),
                ("e", ctypes.c_float),
                ("f", ctypes.c_uint32),
                ("g", ctypes.c_float),
                ("h", ctypes.c_int32),
                ('i', ctypes.c_float*3)]
    
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40
        self.e = 10.
        self.f = 20
        self.g = 30.
        self.h = -40
        self.i = (1,2,3)


    def readwrite(self, rw):
        rw._bytestream.write(self)

class TestStruct5(ctypes.Structure):
    _fields_ = [("a", ctypes.c_uint32),
                ("b", ctypes.c_uint32),
                ("c", ctypes.c_uint32),
                ("d", ctypes.c_uint32),
                ("e", ctypes.c_float),
                ("f", ctypes.c_uint32),
                ("g", ctypes.c_float),
                ("h", ctypes.c_int32),
                ('i', ctypes.c_float*3)]
    
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40
        self.e = 10.
        self.f = 20
        self.g = 30.
        self.h = -40
        self.i = (1,2,3)


    def readwrite(self, rw):
        rw._bytestream.write(bytes(self))
        
# ctypes.cast(..., TestStruct4)

class Writer(WriterBase.extended_with(PRIMITIVE_DESCRIPTORS, PRIMITIVE_ENDIAN_DESCRIPTORS)):
    pass

repeats = 100
writes  = 100000

for i in range(10):
    print(f"Warming up")
    wt = Writer()
    with wt.BytestreamIO() as rw:
        with rw.as_bigendian():
            # (dis.dis(rw.rw_uint32_be))
            # (dis.dis(rw.rw_uint32))
            # assert 0
            for _ in range(writes):
                rw.rw_uint32(10)
            
    
    
t1 = []
for i in range(repeats):
    print(f"Testing write method 1... [{i}]")
    wt = Writer()
    start = time.time()
    s = TestStruct1()
    with wt.BytestreamIO() as rw:
        for _ in range(writes):
            s.readwrite(rw)
    t1.append(time.time()-start)
        
t2 = []
for i in range(repeats):
    print(f"Testing write method 2... [{i}]")
    wt = Writer()
    start = time.time()
    s = TestStruct2()
    with wt.BytestreamIO() as rw:
        for _ in range(writes):
            s.readwrite(rw)
    t2.append(time.time()-start)
    
t3 = []
for i in range(repeats):
    print(f"Testing write method 3... [{i}]")
    wt = Writer()
    start = time.time()
    s = TestStruct3()
    with wt.BytestreamIO() as rw:
        for _ in range(writes):
            s.readwrite(rw)
    t3.append(time.time()-start)
    
t4 = []
for i in range(repeats):
    print(f"Testing write method 4... [{i}]")
    wt = Writer()
    start = time.time()
    s = TestStruct4()
    with wt.BytestreamIO() as rw:
        for _ in range(writes):
            s.readwrite(rw)
    t4.append(time.time()-start)
    
t5 = []
for i in range(repeats):
    print(f"Testing write method 5... [{i}]")
    wt = Writer()
    start = time.time()
    s = TestStruct5()
    with wt.BytestreamIO() as rw:
        for _ in range(writes):
            s.readwrite(rw)
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
for (mean, std), tag in sorted([(fmt_res(r), i) for i, r in [("rw_obj: default", t1), 
                                                             ("rw_obj: autogen", t2), 
                                                             ("rw_obj: autogen2", t3),
                                                             ("rw_obj: cstruct", t4),
                                                             ("rw_obj: cstruct2", t5)]]):
    print(f"Timing {tag.ljust(16, ' ')}: [W]", fmt_mn_std(mean, std))