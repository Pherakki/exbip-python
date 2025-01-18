# Getting Started

## Installation
Either install `exbip` from the package root directory with `pip install -e .`, or copy-and-paste the `exbip` folder from the repository into your repository as a sub-package.

## Creating a Serializable Structure
`exbip` comes equipped with a standard library designed to cover basic serialization needs. The parsing classes contained in the standard library are also a good base to extend the framework with user code from, so familiarity with the standard library is a good foundation for any use case.

Due to Python's duck-typing, to create an `exbip`-compatible serializable we need only conform to the `exbip` serialization interface. This takes the form of equipping a class with an `exbip_rw` function that accepts a parser object as the first non-self argument, alongside arbitrary following arguments.

``` python
class MyStruct:
    def __init__(self, a : int, b : int, c : float):
        self.a = a
        self.b = b
        self.c = c
    
    def exbip_rw(self, rw):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_uint16(self.b)
        self.c = rw.rw_float32(self.c)
```

There are a few things requiring explanation here.

1. The `rw` argument to `exbip_rw` is a parser object. This can be a file writer, a stream reader, or something else entirely that conforms (in abstract) to the parser interface the class is written against. We will see how to pass a valid `rw` into the struct in the following sections.
2. The parser possesses a number of methods that are used to perform operations on data. In this example we are using the standard library functions `rw_uint32`, `rw_uint16`, and `rw_float32`, which respectively operate on an IEEE unsigned 32-bit integer, an IEEE unsigned 16 bit integer, and an IEEE 32-bit floating-point number. Note the language used here: these functions signify an arbitrary operation related to a particular binary data representation, with a parser providing a common theme behind these operations (such as reading or writing this data type from or to a stream).
3. The syntax for `rw_uint32` _etc_. does look a bit odd: the variable in question is both passed into the function and assigned the result of the function. In short, this is to enable to interface to support both reading and writing: the input argument will be ignored for these functions when reading, and the output will be the same as the input when writing. This syntax is used because Python does not support reference or pointer types for immutable data types.
4. We have not yet mentioned endianness. The standard library provides explicit little- and big-endian versions of these functions (*e.g.* `rw_uint32_le`, `rw_uint32_be`), and the ones we have invoked here have context-sensitive endianness. In other words, the endianness of `rw_uint32` is defined by the parser state. This will also be addressed fully in the section on [serialization context](#serialization-context).

Now that we have a serializable object, we will see what we can do with it.

## Writing to a Stream
We can serialize our class using the exbip `Writer` parser. We can do this in a few lines:

```python
from exbip import Writer

class MyStruct:
    def __init__(self, a : int, b : int, c : float):
        self.a = a
        self.b = b
        self.c = c
    
    def exbip_rw(self, rw):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_uint16(self.b)
        self.c = rw.rw_float32(self.c)

s = MyStruct(5, 1, 0.6)

with Writer().FileIO("test.bin") as rw:
    rw.rw_obj(s)
```

A few explanatory notes are once more required.

1. We are opening a file stream using the `FileIO()` method of the `Writer` class. There is a second option, `BytestreamIO()`, which will instead serialize to an `io.BytesIO()` stream.
2. The stream held by the `Writer` is opened and closed by a context manager. All interactions with the stream must happen in this scope.
3. We invoke the `exbip_rw` method of the struct by calling the `rw_obj` method of `Writer`. This is implemented as a simple wrapper function that calls the `exbip_rw` method of the given object. Note that since the received object is required to be mutable, there is no need for the interface to require assignment to `s` for this to work correctly.
4. By default, the `Writer` serializes to **little-endian** data. We will address how to change this in the section on [serialization context](#serialization-context).

To check that the file contains what we expect, we can just open it and read the contents using regular Python.

```python
with open("test.bin", 'rb') as FILE:
    print(FILE.read(10))
    # Check that we've read the whole file
    assert FILE.read(1) == b''
```
This should give you the bytestring
```
>> b'\x05\x00\x00\x00\x01\x00\x9a\x99\x19?'
     |^^^^^^^^^^^^^^||^^^^^^||^^^^^^^^^^^|
          5 (u32)    1 (u16)   0.6 (f32)
```
as expected.

## Reading from a Stream

Deserialization works very similarly to serialization; we need only swap out the `Writer` class for a `Reader` class and we can re-use the same logic.

```python
from exbip import Reader

class MyStruct:
    def __init__(self, a : int, b : int, c : float):
        self.a = a
        self.b = b
        self.c = c
    
    def exbip_rw(self, rw):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_uint16(self.b)
        self.c = rw.rw_float32(self.c)

s = MyStruct(None, None, None)

with Reader().FileIO("test.bin") as rw:
    rw.rw_obj(s)

print(s.a, s.b, s.c) # Prints "5 1 0.6000000238418579"
```

## Simplifying with Traits
Although it is no more than two lines, it is cumbersome to write out the entire context-manager scope for every object you wish to serialize. Moreover, converting a struct to a bytestring can be somewhat tedious, since it requires some extra lines of code:

```python
with Writer().BytestreamIO() as rw:
    rw.rw_obj(s)
    rw._bytestream.seek(0)
    s_bytes = rw._bytestream.read()
```

You could wrap this up into a method on the serializable class instead to encapsulate the boilerplate. `exbip` provides a number of "trait" mix-in classes that define member functions to automate this for you.

The following snippet shows how to use these traits with your object.
```python
from exbip import Reader, ReadableTrait
from exbip import Writer, WriteableTrait

class MyStruct(ReadableTrait(Reader), WriteableTrait(Writer)):
    def __init__(self, a : int, b : int, c : float):
        self.a = a
        self.b = b
        self.c = c
    
    def exbip_rw(self, rw):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_uint16(self.b)
        self.c = rw.rw_float32(self.c)
```
You will see that these traits require a particular parser as an argument. This is so that if you [extend the interface with custom data types](#extending-with-new-operations), you can use these objects to provide the required set of operations without needing to implement the trait definitions yourself.

Let's now see what these traits do for you.
If you execute

```python
print(dir(MyStruct))
```
you will see that there are four new methods:

- read
- frombytes
- write
- tobytes

The first two are defined by the `ReadableTrait`, and the latter two by the `WriteableTrait`. You can now avoid the boilerplate context-manager setup and initiate a (de)serialization process as

```python
from exbip import Reader, ReadableTrait
from exbip import Writer, WriteableTrait

class MyStruct(ReadableTrait(Reader), WriteableTrait(Writer)):
    def __init__(self, a : int, b : int, c : float):
        self.a = a
        self.b = b
        self.c = c
    
    def exbip_rw(self, rw):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_uint16(self.b)
        self.c = rw.rw_float32(self.c)

s = MyStruct(None, None, None)

# In all the below examples, the mandatory arguments
# are given. Any additional arguments are passed to 
# the exbip_rw function on that class.
 
# Read from file
s.read("test.bin")
# Deserialize bytes into this object
s.frombytes(b'\x05\x00\x00\x00\x01\x00\x9a\x99\x19?')
# Write to file
s.write("test.bin")
# Serialize this object to bytes
print(s.tobytes())
```

If you have multiple objects that you might want to serialize independently of each other, you can bundle these traits into a base serializable class which your structs can then inherit from.

```python
class MySerializable(ReadableTrait(Reader),
                     WriteableTrait(Writer)):
    pass

class MyStruct(MySerializable):
    ...

class MyStruct2(MySerializable):
    ...
```

## Objects

We have already encountered the required function to read and write objects: `rw_obj`:

```python
from exbip import Writer

class MyStruct:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def exbip_rw(self, rw):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_float32(self.b)

o = MyStruct(1, 0.5)

with Writer().FileIO("test.bin") as rw:
    rw.rw_obj(o)
```

We can also read or write different objects by passing in a constructor to a diffrent function, `rw_dynamic_obj`:

```python
from exbip import Reader, ReadableTrait
from exbip import Writer, WriteableTrait

class MyStruct:
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c
    
    def exbip_rw(self, rw, c):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_float32(self.b)
        self.c = c

class MyStruct2:
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c
    
    def exbip_rw(self, rw):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_float32(self.b)

class MyBiggerStruct(ReadableTrait(Reader), WriteableTrait(Writer)):
    def __init__(self):
        self.obj  = None
        self.obj2 = None
    
    def exbip_rw(self, rw):
        self.obj  = rw.rw_dynamic_obj(self.obj,  MyStruct, 10)
        self.obj2 = rw.rw_dynamic_obj(self.obj2, lambda: MyStruct2(None, None, 10))

b = MyBiggerStruct()
b.obj = MyStruct(1, 0.2, None)
b.obj2 = MyStruct2(2, 0.4, 10)

b.write("test.bin")

# Look ma, no explicit construction!
c = MyBiggerStruct()
c.read("test.bin")

# 1 0.20000000298023224 10
print(c.obj.a, c.obj.b, c.obj.c)

```

Note that, unlike `rw_obj`, you **must** allocate the return value of `rw_dynamic_obj` to a variable, because it will return a completely new object when deserializing, rather than acting on a mutable object like `rw_obj` (because the object it acts on is created within the function call).

There is also nothing stopping you from declaring additional functions that use a parser and calling them directly on your class:

```python
from exbip import Writer

class MyStruct:
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c
    
    def exbip_rw(self, rw, c):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_float32(self.b)
        self.c = c

class MyStruct2:
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c
    
    def exbip_rw(self, rw):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_float32(self.b)

class MyBiggerStruct:
    def __init__(self):
        self.obj  = None
        self.obj2 = None
    
    def exbip_rw(self, rw):
        self.obj  = rw.rw_dynamic_obj(self.obj,  MyStruct, 10)
    
    def another_rw_function(self, rw):
        self.obj2 = rw.rw_dynamic_obj(self.obj2, lambda: MyStruct2(10))

b = MyBiggerStruct()
b.obj = MyStruct(1, 0.2, None)
b.obj2 = MyStruct2(2, 0.4, 10)

with Writer().FileIO("test.bin") as rw:
    rw.rw_obj(b) # Invokes exbip_rw. We could also do b.exbip_rw(rw)
    b.another_rw_function(rw) # Just calling a regular function on b
```


## Arrays

Clearly, arrays pose a bit of an issue with the current paradigm: if we're reading, the array hasn't yet been constructed, so we can't iterate through it and act on each element.

`exbip` provides two strategies to mitigate this: providing descriptors to read full arrays, and providing some "iterator" methods that construct elements during an iteration process. Both of these strategies are described in the following sections.

### Primitive Arrays

You can read and write arrays of primitives with a similar set of functions to single primitives. These functions all share the convention of having the same name as their single counterparts, with an `s` attached to the end of the type name, and taking an additional `shape` argument that will transform the array into a nested list if it is more than one dimensional. A few examples:

```python
from exbip import Writer

with Writer().FileIO("test.bin") as rw:
    rw.rw_uint32s([1,2,3,4,5], shape=5)
    rw.rw_float32s([(0.1,0.1,0.1), (0.2,0.2,0.2)], shape=(2, 3))
```

### Object Arrays

We've read one object so far, but what about a dynamic number of objects? We have two methods to help here, `rw_dynamic_objs` and `rw_dynamic_objs_while`:

```python
from exbip import Writer

class MyStruct:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b
    
    def exbip_rw(self, rw):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_float32(self.b)

objs = [MyStruct(1, 0.5), MyStruct(2, 1.0)]
with Writer().FileIO("test.bin") as rw:
    objs = rw.rw_dynamic_objs(objs, MyStruct, 2)
```

Providing the constructor and count may seem unnecessary in this example (and indeed, they are), but they are necessary for the deserialization implementation of this function call, since it needs to know _what_ to construct and _how many times to construct it_.

As for `rw_dynamic_objs_while`, this is a version of `rw_dynamic_objs` that uses a stopping condition rather than a count when deserializing:

```python
from exbip import Reader, Writer

class MyStruct:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b
    
    def exbip_rw(self, rw):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_float32(self.b)

objs = [MyStruct(1, 0.5), MyStruct(2, 1.0)]
with Writer().FileIO("test.bin") as rw:
    objs = rw.rw_dynamic_objs_while(objs, MyStruct, lambda rw: rw.tell() < 0x10)

with Reader().FileIO("test.bin") as rw:
    objs2 = rw.rw_dynamic_objs_while(objs, MyStruct, lambda rw: rw.tell() < 0x10)

# 2 2
print(objs2[1].a, len(objs2))
```

For a `Reader`, the above script will continue reading objects as long as the stream position is less than `0x10`. Since each of our structs occupies 8 bytes, in this example it will stop after reading two structs.

You can, of course, provide any boolean-valued callable as a stop condition. For complicated conditions, you may wish to provide a functor rather than a function or lambda:

```python
from exbip import Reader, Writer

class MyStruct:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b
    
    def exbip_rw(self, rw):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_float32(self.b)

class MyStopCondition:
    def __init__(self, pos):
        self.pos = pos
    
    def __call__(self, rw):
        return rw.tell() < self.pos

objs = [MyStruct(1, 0.5), MyStruct(2, 1.0)]
with Writer().FileIO("test.bin") as rw:
    objs = rw.rw_dynamic_objs_while(objs, MyStruct, MyStopCondition(0x10))

with Reader().FileIO("test.bin") as rw:
    objs2 = rw.rw_dynamic_objs_while(None, MyStruct, MyStopCondition(0x10))

# 2 2
print(objs2[1].a, len(objs2))

```

### Iterators

Sometimes you need to get even more complicated than a simple loop where each object is operated on in sequence. For these situations, `exbip` provides two "iterators": the `array_iterator` and `array_while_iterator`.

These act like Python iterators.

```python
from exbip import Writer, OffsetCalculator, OffsetMarker

class MyStruct:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def exbip_rw(self, rw):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_float32(self.b)


objs = [MyStruct(1, 0.5), MyStruct(2, 1.0)]
lst = []
count = len(objs)

with Writer().FileIO("test.bin") as rw:
    for obj in rw.array_iterator(objs, MyStruct, count):
        rw.rw_obj(obj)
        # Contrived example...
        lst.append(obj.a)
    
# [1, 2]
print(lst)
```

`array_while_iterator` works analogously to `rw_dynamic_objs_while`:

```python
from exbip import Writer

class MyStruct:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b
    
    def exbip_rw(self, rw):
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_float32(self.b)

class MyStopCondition:
    def __init__(self, pos):
        self.pos = pos
    
    def __call__(self, rw):
        return rw.tell() < self.pos

objs = [MyStruct(1, 0.5), MyStruct(2, 1.0)]
lst = []
with Writer().FileIO("test.bin") as rw:
    for obj in rw.array_while_iterator(objs, MyStruct, MyStopCondition(0x10)):
        rw.rw_obj(obj)
        # Contrived example...
        lst.append(obj.a)

# [1, 2]
print(lst)
```

## Stream Alignment and Offsets
Commonly, binary files contain offsets that point to the location of particular sections of data. Depending on the parse operation you are performing, you may want to do one of several things:

- [Seek to the offset](#offset-management) (for non-contiguous deserialization)
- [Verify that your stream is currently at that offset](#offset-management) (for contiguous deserialization and parse-like operations such as writing)
- [Automatically calculate the value the offset should take](#automatic-offset-calculation)
- [Some user-defined operation](#extending-with-new-operations)

Data sections in binary files are also often aligned to a cache-friendly width (for example, a data section may begin at a multiple of 0x10 bytes rather than at an arbitrary location).

`exbip` provides several utilities in the standard library for interacting with streams in this way, as described in the following sub-sections.

### Seeks and Tells
When needing to seek or align the stream, it is necessary to know where in the stream you currently are. Less commonly, you may also need to explicity seek within the file, such as if you need to write [a chunk of deserialization-specific logic](#dispatching-to-split-serialization-logic) or [define a custom operation](#extending-with-new-operations).

Multiple seek and tell operations are provided at a framework level.
In all of these, 'seek' operations move the stream offset to a particular position, and 'tell' operations report a particular stream position.

- `global_seek(offset)` and `global_tell(offset)` seek and tell relative to the beginning of the stream. These act like the `seek` and `tell` operations on the built-in Python stream objects (_e.g._ those returned by `open()` or `io.BytesIO()`)
- `seek(offset)` and `tell(offset)` work slightly differently: these are context-sensitive seeks and tells that operate relative to the origin defined by the parser context. This is useful if, for example, you want to operate on a subfile that can be embedded within another file, but measures its offsets from the start of the subfile: by using context-sensitive seeks and tells, your code can work whether the struct is embedded or not, if you set a contextual origin. This is detailed in [a later section](#context-origin).
- `relative_global_seek(offset, base)` and `relative_global_tell(offset, base)` are context-free seeks and tells relative to the position `base`.
- `relative_seek(offset, base)` and `relative_tell(offset, base)` are context-dependent seeks and tells relative to the position `base`.

### Alignment

There are two stream alignment functions provided by the standard library:

- `align(position, alignment[, pad_value=b'\x00'])` will round the `position` up to the nearest multiple of `alignment`. If deserializing, it will read the bytes required to perform the alignment, and throw an exception if the read bytes are not equal to an array of the pad value. If the length of the read bytes is not divisible by the length of the pad value, an exception to this effect is thrown instead. When serializing, enough pad values to complete the alignment are written, and an exception is again thrown if the length of the pad value is not a factor of the length of alignment.
- `fill(position, alignment[, fill_value=b'\x00'])` behaves exactly as `align`, except it will not validate deserialized bytes against the `fill_value`.

A typical usage might be:

```python
class MyStruct:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def exbip_rw(self, rw):
        self.a = rw.rw_uint32(self.a)  # Offset 0x00 -> 0x04
        self.b = rw.rw_uint16(self.b)  # Offset 0x04 -> 0x06
        self.c = rw.rw_float32(self.c) # Offset 0x06 -> 0x0A
        rw.align(rw.tell(), 0x10);     # Offset 0x0A -> 0x10
```

### Offset Management
For validation or navigation purposes, `exbip` provides a few way to move around the file depending on the parser you are using. The relevant functions for this section are:

- `enforce_stream_offset(offset, message[, formatter=None, marker=None])`
- `navigate_stream_offset(offset, message[, formatter=None, marker=None])`
- `verify_stream_offset(offset, message[, formatter=None, marker=None])`
- `check_stream_offset(offset, message[, formatter=None, marker=None])`

In each of these, `offset` is a context-relative offset to be acted on, `message` is a debug message that will be included in any raised exceptions, `formatter` is an `exbip` formatter object that will safely format offsets without propagating `TypeError` or `ValueError` (_e.g._ caused by trying to format `None` to a hexstring), and `marker` is a special argument used for [automatic offset calculation](#automatic-offset-calculation).

`enforce_` will seek to the provided `offset` in `deserialize` mode, raise an exception in `serialize` mode if `offset` is not at `rw.tell()`, and is ignored in `count` mode. This can be used for non-contiguous reads of a file.

`navigate_` will seek to the provided `offset` in `deserialize` mode, and is ignored in `serialize` and `count` mode. This can also be used for trickier non-contiguous reads of a file.

`verify_` will raise an exception in `deserialize` and `serialize` mode if `offset` is not at `rw.tell()`, and is ignored in `count` mode. This can be used for validating contiguous reads of a file.

`check_` is an alias that is set to `verify_` on all parsers except the `NonContiguousReader`. Generally this is the preferred function to use, since it gives you flexibility in whether you want to limit yourself to purely contiguous, strongly validated reads, or a flexible, but unvalidated, non-contiguous read. For most purposes, contiguous reads are fine since files are typically written in a strict structure, although a non-contiguous read is technically permitted by a format and may be the "correct" implementation.

!!! tip
    When developing the serialization code for your structs, you may want to do this with a contiguous `Reader` class to take advantage of the offset validation. After the serialization routine is complete, you could then swap out the `Reader` in the `ReadableTrait` for a `NonContiguousReader`.


### Automatic Offset Calculation

The offsets of various significant locations within a file can be annoying to calculate, despite the fact that they are entirely predictable. `exbip` comes with a parser designed to perform a virtual write of the object, and during that write, it can report its current position as an offset to be stored in a variable.

This is achieved with the `OffsetMarker` class. After constructing it, you can either:
- Call `subscribe(obj, attr_name)` to add the `attr_name` attribute of `obj` to the list of variables to receive the offset reported by the marker,
- Call `subscribe_callback(callback)` to provide a lambda that accepts the `OffsetCalculator` parser as its only argument, e.g. `marker.subscribe_callback(lambda rw: setattr(self, "offset", rw.tell() - 0x20))`

These `OffsetMarker`s can be invoked only by parsers that use the `calculate_offsets` descriptor method in two ways:
- Calling `rw.dispatch_marker(marker)`,
- Passing the marker as the fourth argument (`marker`) of `(enforce_/navigate_/verify_/check_)stream_offset`.

Given below is an example of using the `OffsetMarker` to automatically calculate a list of offsets of some objects.

```python
from exbip import Reader, Writer, OffsetCalculator, OffsetMarker
from exbip import ReadableTrait, WriteableTrait, OffsetsCalculableTrait
from exbip import HEX32_formatter

class MyStruct:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

        self.offset = 0

        # Used by OffsetCalculator
        self.marker = OffsetMarker().subscribe(self, "offset")
    
    def exbip_rw(self, rw):
        self.offset = rw.rw_uint32(self.offset)
    
    def rw_data(self, rw):
        rw.verify_stream_offset(self.offset, "Object offset", HEX32_formatter, self.marker)
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_float32(self.b)

class MyBiggerStruct(ReadableTrait(Reader), WriteableTrait(Writer), OffsetsCalculableTrait(OffsetCalculator)):
    def __init__(self):
        self.obj_count   = 0
        self.objects     = []
    
    def exbip_rw(self, rw):
        self.obj_count   = rw.rw_uint32(self.obj_count)
        self.objects = rw.rw_dynamic_objs(self.objects, MyStruct, self.obj_count)
        
        for obj in self.objects:
            obj.rw_data(rw)


b = MyBiggerStruct()
b.objects.append(MyStruct(1, 0.5))
b.objects.append(MyStruct(2, 1.0))
b.obj_count = len(b.objects)

# Let the OffsetCalculator automatically calculate the offsets of each object

print("Before calculation:", b.objects[0].offset, b.objects[1].offset)
b.calculate_offsets()
print("After calculation:", b.objects[0].offset, b.objects[1].offset)
b.write("test.bin")

c = MyBiggerStruct()
c.read("test.bin")
print("Newly-read object:", c.objects[0].offset, c.objects[1].offset)
```

## Binary Validation

You will commonly find that the data you need to serialize contains more data than the classes you want to use in your program. You may therefore want to employ specific "serializable" classes that represent the data structures in your files, and transform between your "real" classes when deserializing or serializing, or simply (de)serialize some data to/from placeholder variables. To detect bugs in this transformation process, the `Validator` can be extremely useful, and will pinpoint the exact data members that differ between two files/bytestrings.

It is easiest to use the `Validator` with its corresponding trait, `ValidatableTrait`, since setting it up manually is a little bit involved. This gives you access to four functions:

- `validate_file_against_file(primary_filepath, reference_filepath, *args, **kwargs)`
- `validate_file_against_bytes(primary_filepath, reference_bytes, *args, **kwargs)`
- `validate_bytes_against_file(primary_bytes, reference_filepath, *args, **kwargs)`
- `validate_bytes_against_bytes(primary_bytes, reference_bytes, *args, **kwargs)`

In each case, the required arguments are hopefully self-expanatory: you can use these functions to validate either a file or a bytestring against another file or bytestring, using an `exbip`-compatible object as the data structure for it. `*args` and `**kwargs` are passed to the `exbip_rw` function in all cases.

Running one of these functions will throw a `ValidationError` if there is even a single byte that is different between your two deserialization sources. This is trivial to do in Python without the need for a class: you could simply `zip` two bytestrings together and check if all characters in the strings match. However, the `Validator` will throw the `ValidationError` from the exact read call that returns disagreeing bytes, giving you a full stacktrace through your deserialization procedure from the disagreeing data member up to the root validation call. This makes identifying exactly what has gone wrong significantly easier to diagnose.

Let's take a look at an example to round out this section.

```python
from exbip import Reader, Writer, OffsetCalculator, Validator,  OffsetMarker
from exbip import ReadableTrait, WriteableTrait, OffsetsCalculableTrait, ValidatableTrait
from exbip import HEX32_formatter

class MyStruct:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

        self.offset = 0

        # Used by OffsetCalculator
        self.marker = OffsetMarker().subscribe(self, "offset")
    
    def exbip_rw(self, rw):
        self.offset = rw.rw_uint32(self.offset)
    
    def rw_data(self, rw):
        rw.verify_stream_offset(self.offset, "Object offset", HEX32_formatter, self.marker)
        self.a = rw.rw_uint32(self.a)
        self.b = rw.rw_float32(self.b)

class MyBiggerStruct(ReadableTrait(Reader), WriteableTrait(Writer), OffsetsCalculableTrait(OffsetCalculator), ValidatableTrait(Validator)):
    def __init__(self):
        self.obj_count   = 0
        self.objects     = []
    
    def exbip_rw(self, rw):
        self.obj_count   = rw.rw_uint32(self.obj_count)
        self.objects = rw.rw_dynamic_objs(self.objects, MyStruct, self.obj_count)
        
        for obj in self.objects:
            obj.rw_data(rw)


b = MyBiggerStruct()
b.objects.append(MyStruct(1, 0.5))
b.objects.append(MyStruct(2, 1.0))
b.obj_count = len(b.objects)

# Let the OffsetCalculator automatically calculate the offsets of each object

b.calculate_offsets() # Oops, forgot to calculate the offsets!
bstring1 = b.tobytes()
# Contrived example, but it demonstrates the principle:
b.objects[0].a = 10
bstring2 = b.tobytes()

# Read b'\x01\x00\x00\x00' from primary stream, reference data is b'\n\x00\x00\x00'
# Provides a stacktrace stemming from "self.a = rw.rw_uint32(self.a)"
MyBiggerStruct().validate_bytes_against_bytes(bstring1, bstring2)
```

## Serialization Context
### Endianness
A data structure can be little-endian, big-endian, and sometimes it can contain both endiannesses. In addition to standard library functions to explicitly operate on data types of a particular endianness, it also supports functions that contextually use either little- or big-endianness at a framework level. Examples of these functions are `rw_uint32` and `rw_float32`.

Whether these functions are in little- or big-endian mode depends on the parsing context; _i.e._ the state of the current parser. It is very easy to change this state using the framework-level context-manager functions `as_littleendian()`, `as_bigendian()`, and `as_endian(endianness)`. Below is an example of these functions in action.

```python
from exbip import Writer

with Writer().FileIO("test.bin") as rw:
    with rw.as_bigendian():
        rw.rw_uint32(1) # Writes a big-endian int 1
        with rw.as_littleendian():
            rw.rw_uint32(2) # Writes a little-endian int 2
        rw.rw_uint32(3) # Writes a big-endian int 3
    rw.rw_uint32(4) # Default context: Writes a little-endian int 4
    with rw.as_endian('little'): # Also '<', '>', or 'big'
        rw.rw_uint32(5) # Writes a little-endian int 5
```

!!! note
    In order to mitigate performance loss, endian-aware functions are
    not implemented as wrapper functions or with runtime if/else statements. Instead, they are placeholder labels that the explicit little-endian and big-endian versions of an operator are monkey-patched onto. This monkey-patching occurs every time the endianness-context is switched. Therefore, if you need to extend a parser with your own functions that need to execute **different functions** for little-endian and big-endian invocations, you need to implement both versions and [extend the parser with them](#extending-with-new-endian-aware-operators).

### Context Origin
If you need to measure your `seek()`s and `tell()`s from somewhere other than the stream origin, you can set a context origin with a context manager object:
```python
from exbip import Writer

with Writer().FileIO("test.bin") as rw:
    rw.rw_uint32s([0,1,2,3,4,5], 6) # Offset 0x00->0x18
    print(hex(rw.tell())) # Prints 0x18
    with rw.new_origin():
        print(hex(rw.tell()), hex(rw.global_tell())) # Prints 0x0, 0x18
    print(hex(rw.tell())) # Prints 0x18 again
```
This can also be combined with the endianness context switches, _e.g._
```python
from exbip import Writer

with Writer().FileIO("test.bin") as rw:
    rw.rw_uint32s([0,1,2,3,4,5], 6) # Offset 0x00->0x18
    print(hex(rw.tell())) # Prints 0x18
    with rw.new_origin(), rw.as_bigendian():
        print(hex(rw.tell()), hex(rw.global_tell())) # Prints 0x0, 0x18
    print(hex(rw.tell())) # Prints 0x18 again
```

## Dispatching to split serialization logic
Sometimes, the provided functionality is not sufficient and you need to write explicitly different code for your deserialization and serialization paths. To do this, you can capture your code in a 'descriptor' object:

```python
class MyDescriptor:
    def deserialize(binary_parser, ...):
        ... # Here is the logic for deserialization
    
    def serialize(binary_parser, ...):
        ... # Here is the logic for serialization
    
    def count(binary_parser, ...):
        ... # Here is the logic for calculating how many bytes this invocation moves the stream offset
```

These three functions are the main ones used by the standard library: `Reader`-like parsers call into `deserialize`, `Writer`-like classes call into `serialize`, and `Counter`-like classes call into `count`. You can optionally define a `calculate_offsets` function that will be picked up by the `OffsetCalculator` instead of the `count` function.

As example of this might be
```python
class MyDescriptor:
    """
    A class that reads or writes one of two objects depending on the value of a bitvector.
    """
    def deserialize(binary_parser, value, ctor1, ctor2, bitvector, count):
        value.clear()

        bv = bitvector
        for _ in range(count):
            if (bv & 1):
                value.push_back(ctor1())
            else:
                value.push_back(ctor2())
            rw.rw_obj(value[-1])

            bv >>= 1
    
    def serialize(binary_parser, value, ctor1, ctor2, bitvector, count):
        # You could do some validation here against the bitvector and/or count.
        for obj in value:
            rw.rw_obj(obj)
    
    def count(binary_parser, value, ctor1, ctor2, bitvector, count):
        for obj in value:
            rw.rw_obj(obj)
```

The standard library provides the `rw_descriptor` function that can be used to dispatch to whichever of these functions is appropriate for the parser in use. To use it, simply pass in the descriptor along with any non-parser arguments it needs:

```python
rw.rw_descriptor(MyDescriptor, arr, ctor1, ctor2, bitvector, count)
```

## Extending with new Operations
Once you know how to [dispatch to split serialization logic](#dispatching-to-split-serialization-logic), it is easy to create an operator extension for `exbip`. Instead of using your descriptor with `rw_descriptor`, we will simply promote its functionality to member functions of your parser classes.

To do this, you just need to give it a class variable `FUNCTION_NAME` that will be the name of the member function, _e.g._

```python
class MyDescriptor:
    FUNCTION_NAME = "my_op"

    # deserialize, serialize, count, etc.
```

You can now extend any parser that uses the functions defined on your descriptor. To do this, you simply define a new parser that inherits from the object returned by the `extended_with` method of a parser. For example, you can make your own `Reader` and `Writer` like

```python

class MyReader(Reader.extended_with([MyDescriptor])):
    pass

class MyWriter(Writer.extended_with([MyDescriptor])):
    pass
```

You will notice that `MyDescriptor` is in a list, allowing you to extend with multiple descriptors. In fact, it is wise to collect all your custom descriptors into a single list and extend your parsers with this list.

```python
MyDescriptors = [MyDescriptor1, MyDescriptor2, MyDescriptor3]

class MyReader(Reader.extended_with(MyDescriptors)):
    pass

class MyWriter(Writer.extended_with(MyDescriptors)):
    pass
```

You can then use `my_op` whereever you use `MyReader` or `MyWriter`:

```python
with MyWriter().FileIO("test.bin") as rw:
    rw.my_op(...)
```

You can also use `MyReader` and `MyWriter` as the parsers for traits, which can be packaged up into a convenient base class for your structs:

```python
class MySerializable(ReadableTrait(MyReader),
                     WriteableTrait(MyWriter)):
    pass

class MyStruct1(MySerializable):
    def __init__(self):
        self.a = 10
    
    def exbip_rw(self, rw):
        rw.my_op(...)
```

You can create sub-libraries for `exbip` by providing these lists of descriptors for custom data types that others can use to extend `exbip` with.

## Extending with new endian-aware operators
The `extended_with` function described in [the previous section](#extending-with-new-operations) can take a second argument: a list of endian-aware functions. This is a little bit more complicated to set up and is aided by a framework class from `exbip`.

To start with, you need to define your little-endian and your big-endian descriptors:

```python
class MyLEDescriptor:
    FUNCTION_NAME = "my_op_le"
    
    # deserialize, serialize, count

class MyBEDescriptor:
    FUNCTION_NAME = "my_op_be"
    
    # deserialize, serialize, count
```

From here we can define an `EndianPairDescriptor`:

```python
from exbip.framework import EndianPairDescriptor

MyDescriptor = EndianPairDescriptor("my_op", "my_op_le", "my_op_be")
```

where the first argument is the endian-aware function name, the second argument is the name of the little-endian function, and the third argument is the big-endian function name. You could of course alternatively write this as

```python
from exbip.framework import EndianPairDescriptor

MyDescriptor = EndianPairDescriptor("my_op", MyLEDescriptor.FUNCTION_NAME, MyBEDescriptor.FUNCTION_NAME)
```

You can then install your endian-aware function in the second argument of the `extended_with` function:

```python
class MyReader([MyLEDescriptor, MyBEDescriptor], [MyDescriptor]):
    pass
```

## Extending with new parsers
You can define entirely new parser types as long as they conform to the `exbip` interface. In principle, you only need a few things: a member variable called `_bytestream`, a static `_get_rw_method` method that retreives the appropriate operator implementation from a descriptor, an implementation for `global_seek` and `global_tell`, and to inherit from `IBinaryParser`.

As an example, here is a somewhat arbitrarily-defined custom parser.

```python
class MyCustomParserBase(IBinaryParser):
    def __init__(self):
        super().__init__()
        self._bytestream = None

    @classmethod
    def new(cls, initializer):
        instance = cls()
        instance._bytestream = io.BytesIO(initializer)
        return instance

    def global_tell(self):
        return self._bytestream.tell()

    def global_seek(self, offset):
        return self._bytestream.seek(offset)

    @staticmethod
    def _get_rw_method(descriptor):
        if hasattr(descriptor, "custom_op"):
            return descriptor.custom_op
        else:
            return descriptor.count
```

You can install the standard library descriptors onto this like 

```python
from exbip import STANDARD_DESCRIPTORS, STANDARD_ENDIAN_DESCRIPTORS
class MyCustomParser(MyCustomParserBase.extended_with(STANDARD_DESCRIPTORS, STANDARD_ENDIAN_DESCRIPTORS)):
    pass
```

and use it like

```python
# No reason why we also couldn't have written the constructor
# to take an initializer, or to set the _bytestream to something
# directly. The programmer should design their parser to solve
# the particular problem they need it to solve.
with MyCustomParser.new(b'') as rw:
    ... # operations
```

If appropriate, you could also write yourself a trait for this class that can be used as a mix-in for any serializables you write:

```python
def CustomParseableTrait(CustomParser):
    class CustomParseableTraitImpl:
        def custom_parse(self, *args, **kwargs):
            custom_parser = CustomParser()
            custom_parser.rw_obj(self, *args, **kwargs)
    
    return CustomParseableTraitImpl
```

To summarise, this is a parser that wraps an `io.BytesIO` stream and will call the `custom_op` function of a descriptor if it exists, and otherwise fall back to the `count` operator. You could make it depend only on the `custom_op` function existing -- however, your parser would then not be compatible with the standard library descriptors since this function does not exist on any of these. You would either need to define new descriptors inheriting from the standard library that implement this operation and extend your base class with these, or write a completely custom set of descriptors that conform to a different interface than that implemented by the standard library descriptors.

## What's next?
This article should have covered the main features of `exbip`. A listing of all standard descriptors and framework functionality is provided in the Standard Library and Framework pages, which this article as hopefully prepared you to understand.
