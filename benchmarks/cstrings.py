import io
import itertools
import functools
import struct
import random
import time

import numpy as np

random.seed(507569)

MIN_STRING = 2
MAX_STRING = 56
STRING_COUNT = 4000
ITERS = 1000

alphabet = [struct.pack('B', c) for c in range(0x61, 0x61+26)]

strings = [
    b''.join(alphabet[random.randint(0, 25)] for _ in range(random.randint(MIN_STRING, MAX_STRING)))
    for i in range(STRING_COUNT)
]

strings = b'\x00'.join(strings) + b'\x00'

sstream = io.BytesIO(strings)

def basic_bytestring(f):
    ln = 0
    fb = f.read
    fr = fb(1)
    while fr != b'\x00' and len(fr):
        fr = fb(1)
        ln += 1
    f.seek(-(ln+1), 1)
    return fb(ln+2)[:-1]

def fancy_cbytestring(f):
    toeof = iter(functools.partial(f.read, 1), '')
    return b''.join(itertools.takewhile(b'\x00'.__ne__, toeof))

def buffered_cbytestring(f, size=0x40):
    sz = 0
    fr = f.read
    buf = fr(size)
    idx = buf.find(b'\x00')
    while idx == -1:
        sz += size
        buf = fr(size)
        idx = buf.find(b'\x00')
        if not len(buf):
            assert 0
    origin = sz + size
    sz += idx
    
    f.seek(-(origin), 1)
    return fr(sz+1)[:-1]

def buffered_dumb_cbytestring(f, size=0x40):
    fr = f.read
    s = b''
    buf = fr(size)
    idx = buf.find(b'\x00')
    while idx == -1:
        s += buf
        buf = fr(size)
        idx = buf.find(b'\x00')
    s += buf[:idx]
    f.seek(idx-size+1, 1)
    return s

def dumb_cbytestring(f, terminator=b'\x00'):
    fr= f.read
    out = b''
    cur_byte = b''
    while cur_byte != terminator:
        out += cur_byte
        cur_byte = fr(1)
    return out
        
for _ in range(STRING_COUNT):
    s = basic_bytestring(sstream)

basic_times = []
basic_reads = []
for _ in range(ITERS):
    sstream.seek(0)
    print("Basic read", _+1)
    st = time.time()
    for __ in range(STRING_COUNT):
        s = basic_bytestring(sstream)
    basic_times.append(time.time()-st)
    # basic_reads.append(s)


fancy_times = []
fancy_reads = []
for _ in range(ITERS):
    sstream.seek(0)
    print("Fancy read", _+1)
    st = time.time()
    for __ in range(STRING_COUNT):
        s = fancy_cbytestring(sstream)
    fancy_times.append(time.time()-st)
        # fancy_reads.append(s)

buffered_times = []
buffered_reads = []
for _ in range(ITERS):
    sstream.seek(0)
    print("Buffered read 0x10", _+1)
    st = time.time()
    for __ in range(STRING_COUNT):
        s = buffered_cbytestring(sstream, 0x10)
    buffered_times.append(time.time()-st)
    # buffered_reads.append(s)

buffered_times_0x20 = []
for _ in range(ITERS):
    sstream.seek(0)
    print("Buffered read 0x20", _+1)
    st = time.time()
    for __ in range(STRING_COUNT):
        s = buffered_cbytestring(sstream, 0x20)
    buffered_times_0x20.append(time.time()-st)
    
buffered_times_0x30 = []
for _ in range(ITERS):
    sstream.seek(0)
    print("Buffered read 0x30", _+1)
    st = time.time()
    for __ in range(STRING_COUNT):
        s = buffered_cbytestring(sstream, 0x30)
    buffered_times_0x30.append(time.time()-st)
    
buffered_times_0x40 = []
for _ in range(ITERS):
    sstream.seek(0)
    print("Buffered read", _+1)
    st = time.time()
    for __ in range(STRING_COUNT):
        s = buffered_cbytestring(sstream, 0x40)
    buffered_times_0x40.append(time.time()-st)

dumb_buffered_times_0x40 = []
dumb_buffered_reads_0x40 = []
for _ in range(ITERS):
    sstream.seek(0)
    print("Buffered read", _+1)
    st = time.time()
    for __ in range(STRING_COUNT):
        s = buffered_dumb_cbytestring(sstream, 0x40)
        dumb_buffered_reads_0x40.append(s)
    dumb_buffered_times_0x40.append(time.time()-st)


dumb_times = []
dumb_reads = []
for _ in range(ITERS):
    sstream.seek(0)
    print("Dumb read", _+1)
    st = time.time()
    for __ in range(STRING_COUNT):
        s = dumb_cbytestring(sstream)
    dumb_times.append(time.time()-st)
    # dumb_reads.append(s)

print("Basic reads:              ", np.mean(basic_times), "+/-", np.std(basic_times))
print("Fancy reads:              ", np.mean(fancy_times), "+/-", np.std(fancy_times))
print("Buffered reads 0x10:      ", np.mean(buffered_times), "+/-", np.std(buffered_times))
print("Buffered reads 0x20:      ", np.mean(buffered_times_0x20), "+/-", np.std(buffered_times_0x20))
print("Buffered reads 0x30:      ", np.mean(buffered_times_0x30), "+/-", np.std(buffered_times_0x30))
print("Buffered reads 0x40:      ", np.mean(buffered_times_0x40), "+/-", np.std(buffered_times_0x40))
print("Dumb Buffered reads 0x40: ", np.mean(dumb_buffered_times_0x40), "+/-", np.std(dumb_buffered_times_0x40))
print("Dumb reads:               ", np.mean(dumb_times), "+/-", np.std(dumb_times))
