import array
import io
import itertools
import functools
import struct
import random
import time

import numpy as np

random.seed(507569)

class ExbipArray:
    def __init__(self, iterable, shape):
        self._buffer = iterable
        self._shape  = shape
        self._strides = [1 for _ in shape]
        _strides = self._strides
        n_dims = len(shape)
        for i, s in enumerate(shape[1::][::-1]):
            _strides[n_dims-i-2] = s*_strides[n_dims-i-1]
            

    @property
    def shape(self):
        return self._shape
    
    def __getitem__(self, index):
        print(index)
        if isinstance(index, int):
            index = (index,)


def benchmark(fn, shape, sstream, iters, msg):
    times = []
    for _ in range(iters):
        sstream.seek(0)
        print(msg, _+1)
        st = time.time()
        fn(sstream, shape)
        times.append(time.time()-st)
    return times


def benchmark_access(fn, data, iters, msg):
    times = []
    for _ in range(iters):
        print(msg, _+1)
        st = time.time()
        fn(data)
        times.append(time.time()-st)
    return times

def summary(times):
    longest_label = max(len(t[0]) for t in times)
    for label, ttimes in times:
        print(label + ":" + " "*(longest_label-len(label)), np.mean(ttimes), "+/-", np.std(ttimes))
    

def split_list(lst, chunksize):
    return [lst[i:i + chunksize] for i in range(0, len(lst), chunksize)]

def reshape_list(lst, shape):
    out = lst
    for subshape in shape[1::][::-1]:
        out = split_list(out, subshape)
    return out

def split_conv_list(lst, chunksize):
    return [list(lst[i:i + chunksize]) for i in range(0, len(lst), chunksize)]

def reshape_conv_list(lst, shape):
    out = lst
    for subshape in shape[1::][::-1]:
        out = split_conv_list(out, subshape)
    return out


def baseline_read(f, count):
    f.read(count*4)

def array_read(f, count):
    return array.array('f', f.read(count*4))

def array_list_read(f, count):
    return list(array.array('f', f.read(count*4)))

def array_matrix_read(f, shape):
    count = 1
    for s in shape:
        count *= s
    
    data = array.array('f', f.read(count*4))
    return reshape_list(data, shape)
    
def array_matrix_list_read(f, shape):
    count = 1
    for s in shape:
        count *= s
    
    data = array.array('f', f.read(count*4))
    return reshape_conv_list(data, shape)

unpack = struct.unpack
def struct_read(f, count):
    return unpack('f'*count, f.read(count*4))

def struct_list_read(f, count):
    return list(unpack('f'*count, f.read(count*4)))

def struct_matrix_read(f, shape):
    count = 1
    for s in shape:
        count *= s
    
    data = unpack('f'*count, f.read(count*4))
    return reshape_list(data, shape)
    
def struct_matrix_list_read(f, shape):
    count = 1
    for s in shape:
        count *= s
    
    data = unpack('f'*count, f.read(count*4))
    return reshape_conv_list(data, shape)


def numpy_read(f, count):
    return np.frombuffer(f.read(count*4), np.float32)

def numpy_matrix_read(f, shape):
    count = 1
    for s in shape:
        count *= s
    
    v = np.frombuffer(f.read(count*4), np.float32)
    return v.reshape(shape)


def define_access(shape):
    fndef = f"def access(data):\n"
    ranges = [range(s) for s in shape]
    for indices in itertools.product(*ranges):
        accessor = ''.join(f"[{idx}]" for idx in indices)
        fndef += f"    v = data{accessor}\n"
    
    scope = {}
    exec(fndef, {}, scope)
    return scope["access"]


        
DSIZE  = 4
ITERS  = 100

# Position vector, bone matrix, little mipmap, big mipmap, bone matrix array
shapes = [(2000, 3), (4,4), (16,16), (1024, 1024), (100, 4, 4)]

all_times = []
for shape in shapes:
    submsg = f"[{'x'.join(str(e) for e in shape)}]"
    count = 1
    for s in shape:
        count *= s
    
    data_buffer = struct.pack('f'*count, *[random.random() for _ in range(count)])
    sstream = io.BytesIO(data_buffer)
    
    benchmark_runs = [
        # Check if any significant perf gains are available by providing an
        # exclusively flat-list version.
        (baseline_read,           count,    f"Baseline {submsg}"),
        (struct_read,             count,    f"Struct {submsg}"),
        (struct_list_read,        count,    f"Struct List {submsg}"),
        (array_read,              count,    f"Array {submsg}"),
        (array_list_read,         count,    f"Array List {submsg}"),
        (numpy_read,              count,    f"Numpy {submsg}"),
        
        # Compare these two methods to see the impact of reshaping the list
        # on each method.
        (struct_matrix_read,      (count,), f"Struct Flat Matrix {submsg}"),
        (struct_matrix_list_read, (count,), f"Struct Flat Matrix List {submsg}"),
        (array_matrix_read,       (count,), f"Array Flat Matrix {submsg}"),
        (array_matrix_list_read,  (count,), f"Array Flat Matrix List {submsg}"),
        (numpy_matrix_read,       (count,), f"Numpy Flat Matrix {submsg}"),
        
        (struct_matrix_read,      shape,    f"Struct Matrix {submsg}"),
        (struct_matrix_list_read, shape,    f"Struct Matrix List {submsg}"),
        (array_matrix_read,       shape,    f"Array Matrix {submsg}"),
        (array_matrix_list_read,  shape,    f"Array Matrix List {submsg}"),
        (numpy_matrix_read,       shape,    f"Numpy Matrix {submsg}"),
    ]
    
    times = []
    for fn, shp, msg in benchmark_runs:
        times.append((msg, benchmark(fn, shp, sstream, ITERS, msg)))
    
    sstream.seek(0)
    list_of_arrays = array_matrix_read(sstream, shape)
    sstream.seek(0)
    numpy_array    = array_matrix_read(sstream, shape)
    sstream.seek(0)
    list_of_lists  = list(numpy_array)
    
    benchmark_access_runs = [
        (define_access(shape), shape, list_of_lists,  f"List of Lists Access {submsg}"),
        (define_access(shape), shape, list_of_arrays, f"List of Arrays Access {submsg}"),
        (define_access(shape), shape, numpy_array,    f"Numpy Array Access {submsg}"),
    ]
    
    for fn, shp, data, msg in benchmark_access_runs:
        times.append((msg, benchmark_access(fn, data, ITERS, msg)))
        
    all_times.append((shape, times))

# Conclusions:
# - Conversion to native lists is expensive.
# - 'struct' is much slower than 'array', and 'array' is slower than 'numpy'
#   for large arrays.
# - the cost of reading a flat list vs a 1-D shape is unresolvable
# - Array access seems to be indistinguishable between the produced objects.
#
# Based on this, numpy should be used as a backend. If the user does not have
# numpy available on their system, exbip should fall back to list-of-arrays.
for shape, times in all_times:
    label = str(shape)
    print("####################" + len(label)*'#')
    print(f"# ARRAY BENCHMARK {label} #")
    print("####################" + len(label)*'#')
    summary(times)

