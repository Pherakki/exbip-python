import io
import random
import time
import numpy as np

class BytestreamIO:
    def __init__(self, rw, initializer):
        self.rw = rw
        self.initializer = initializer

    def __enter__(self):
        self.rw._bytestream = io.BytesIO(self.initializer)
        self.rw.read_bytes  = self.rw._bytestream.read
        return self.rw

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.rw._bytestream.close()
        self.rw._bytestream = None
        self.rw.read_bytes = self.rw._default_read_bytes

class ByteReader:
    def __init__(self):
        self._bytestream = None

    def BytestreamIO(self, initializer):
        return BytestreamIO(self, initializer)

    def _default_read_bytes(self, length):
        return self._bytestream.read(length)

    read_bytes = _default_read_bytes

def read_default(rw, data, iters, msg, chunksize):
    times = []
    with rw.BytestreamIO(data):
        rw._bytestream.seek(0)
    
        for _ in range(iters):
            print(msg, _+1)
            st = time.time()
            for j in range(len(data)//chunksize):
                rw._default_read_bytes(chunksize)
            times.append(time.time()-st)
    return times

def read_wrapper(rw, data, iters, msg, chunksize):
    times = []
    with rw.BytestreamIO(data):
        rw._bytestream.seek(0)
    
        for _ in range(iters):
            print(msg, _+1)
            st = time.time()
            for j in range(len(data)//chunksize):
                rw.read_bytes(chunksize)
            times.append(time.time()-st)
    return times

def read_direct(rw, data, iters, msg, chunksize):
    times = []
    with rw.BytestreamIO(data):
        rw._bytestream.seek(0)
    
        for _ in range(iters):
            print(msg, _+1)
            st = time.time()
            for j in range(len(data)//chunksize):
                rw._bytestream.read(chunksize)
            times.append(time.time()-st)
    return times

def execute_benchmark(fn, msg, times):
    times.append((msg, fn(msg)))

def summary(times):
    longest_label = max(len(t[0]) for t in times)
    for label, ttimes in times:
        print(label + ":" + " "*(longest_label-len(label)), np.mean(ttimes), "+/-", np.std(ttimes))
    
random.seed(507569)
DATA = random.randbytes(0x1000000) # 16 MiB
ITERS = 100

chunksizes = [0x1000000, 0x100000, 0x10000, 0x1000, 0x100, 0x10, 0x01]

rw = ByteReader()
times = []
for chunksize in chunksizes:
    subt = []
    execute_benchmark(lambda msg: read_default(rw, DATA, ITERS, msg, chunksize), f"Read Default [{hex(chunksize)}]", subt)
    execute_benchmark(lambda msg: read_wrapper(rw, DATA, ITERS, msg, chunksize), f"Read Wrapper [{hex(chunksize)}]", subt)
    execute_benchmark(lambda msg: read_direct (rw, DATA, ITERS, msg, chunksize), f"Read Direct  [{hex(chunksize)}]", subt)
    times.append(subt)

print("############################")
print(f"# STREAM ACCESS BENCHMARK #")
print("############################")
for subt in times:
    summary(subt)
    print("=====")
