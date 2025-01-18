# Framework
Namespace: `exbip.framework`


## Descriptors<a name="EndianPairDescriptor"></a>
<code style="display: block; color: #FFA000;">
<span>EndianPairDescriptor <a href="#EndianPairDescriptor">#</a></code>

<div style="padding-left: 2em;">
Instantiate this class to create an endian-aware descriptor.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Functions:
</div>

<div style="padding-left: 4em; color: #2094F3;">
__init__(name, little_endian, big_endian):
</div>
<div style="padding-left: 6em;">
When installed on a parser, this will create an operation called <code>name</code> that is set to the operation with name <code>little_endian</code> in little-endian mode and with name <code>big_endian</code> when in big-endian mode.
</div>




## Parsers<a name="IBinaryParser"></a>
<code style="display: block; color: #FFA000;">
<span>IBinaryParser <a href="#IBinaryParser">#</a></code>

<div style="padding-left: 2em;">
A base class for <code>exbip</code> parsers.
</div><span style="padding-left: 2em; color: #2094F3;">
Descriptor Method:</span> <span><i>undefined</i></span><div style="padding-left: 2em;">
Additional Functions:
</div>
<div style="padding-left: 4em; color: #2094F3;">
_get_rw_method(descriptor):
</div>
<div style="padding-left: 6em;">
Pure virtual method. Must be implemented by an inheriting class. Intended to return a function on <code>descriptor</code> matching the theme of the parser.
</div>

<div style="padding-left: 4em; color: #2094F3;">
global_seek(position):
</div>
<div style="padding-left: 6em;">
Pure virtual method. Must be implemented by an inheriting class. Intended to set the stream offset to the given offset.
</div>

<div style="padding-left: 4em; color: #2094F3;">
global_tell():
</div>
<div style="padding-left: 6em;">
Pure virtual method. Must be implemented by an inheriting class. Intended to return the stream offset.
</div>

<div style="padding-left: 4em; color: #2094F3;">
[classmethod] extended_with(descriptors, endian_inlined):
</div>
<div style="padding-left: 6em;">
Returns a class derived from the current class that has the operators defined in <code>descriptors</code> defined on it, using the <code>rw_method</code> for that class. Also installs the endian-aware descriptors in <code>endian_inlined</code>.
</div>

<div style="padding-left: 4em; color: #2094F3;">
execute_descriptor(descriptor, \*args, \*\*kwargs):
</div>
<div style="padding-left: 6em;">
Fetches the required method from <code>descriptor</code> for this parser and executes it.
</div>

<div style="padding-left: 4em; color: #2094F3;">
__call__(descriptor, \*args, \*\*kwargs):
</div>
<div style="padding-left: 6em;">
Equal to <code>execute_descriptor</code>.
</div>

<div style="padding-left: 4em; color: #2094F3;">
[staticmethod] bytes_to_alignment(position, alignment):
</div>
<div style="padding-left: 6em;">
Calculates how many bytes are required to round <code>position</code> up to the nearest multiple of <code>alignmente</code>.
</div>

<div style="padding-left: 4em; color: #2094F3;">
is_unaligned(alignment):
</div>
<div style="padding-left: 6em;">
Returns True if the current stream position is not a multiple of <code>alignment</code>, else, False.
</div>

<div style="padding-left: 4em; color: #2094F3;">
relative_global_seek(offset, base_position):
</div>
<div style="padding-left: 6em;">
Seeks to <code>offset + base_position</code> relative to the stream origin.
</div>

<div style="padding-left: 4em; color: #2094F3;">
seek(offset):
</div>
<div style="padding-left: 6em;">
Seeks to <code>offset</code> relative to the context origin.
</div>

<div style="padding-left: 4em; color: #2094F3;">
relative_seek(offset, base_position):
</div>
<div style="padding-left: 6em;">
Seeks to <code>offset + base_position</code> relative to the context origin.
</div>

<div style="padding-left: 4em; color: #2094F3;">
relative_global_tell(base_position):
</div>
<div style="padding-left: 6em;">
Returns <code>global_tell() - base_position</code>.
</div>

<div style="padding-left: 4em; color: #2094F3;">
tell():
</div>
<div style="padding-left: 6em;">
Returns <code>global_tell()</code> relative to the context origin.
</div>

<div style="padding-left: 4em; color: #2094F3;">
relative_tell(base_position):
</div>
<div style="padding-left: 6em;">
Returns <code>global_tell() - base_position</code> relative to the context origin.
</div>

<div style="padding-left: 4em; color: #2094F3;">
local_to_global_offset(offset):
</div>
<div style="padding-left: 6em;">
Transforms <code>offset</code> from a local (context) offset to a global (stream) offset.
</div>

<div style="padding-left: 4em; color: #2094F3;">
global_to_local_offset(offset):
</div>
<div style="padding-left: 6em;">
Transforms <code>offset</code> from a global (stream) offset to a local (context) offset.
</div>

<div style="padding-left: 4em; color: #2094F3;">
current_origin():
</div>
<div style="padding-left: 6em;">
Returns the current stream position corresponding to the context origin.
</div>

<div style="padding-left: 4em; color: #2094F3;">
push_origin(offset):
</div>
<div style="padding-left: 6em;">
Sets <code>offset</code> as the current context origin.
</div>

<div style="padding-left: 4em; color: #2094F3;">
pop_origin():
</div>
<div style="padding-left: 6em;">
Restores the context origin to the previous context's origin.
</div>

<div style="padding-left: 4em; color: #2094F3;">
new_origin():
</div>
<div style="padding-left: 6em;">
Returns a context manager that will call <code>push_origin</code> when entered, and <code>pop_origin</code> when exited.
</div>

<div style="padding-left: 4em; color: #2094F3;">
[property] endianness():
</div>
<div style="padding-left: 6em;">
Returns the current context's endianness.
</div>

<div style="padding-left: 4em; color: #2094F3;">
set_endianness(endianness):
</div>
<div style="padding-left: 6em;">
Sets the current context's endianness. Valid values are <code>'<'</code> and <code>'>'</code>.
</div>

<div style="padding-left: 4em; color: #2094F3;">
as_littleendian():
</div>
<div style="padding-left: 6em;">
Returns a context manager that sets the context endianness to little endian for the scope of the context.
</div>

<div style="padding-left: 4em; color: #2094F3;">
as_bigendian():
</div>
<div style="padding-left: 6em;">
Returns a context manager that sets the context endianness to big endian for the scope of the context.
</div>

<div style="padding-left: 4em; color: #2094F3;">
as_endian(endianness):
</div>
<div style="padding-left: 6em;">
Returns a context manager that sets the context endianness to the provided endianness for the scope of the context. Valid values are <code>'<'</code>, <code>'>'</code>, <code>'little'</code>, and <code>'big'</code>.
</div>

<div style="padding-left: 4em; color: #2094F3;">
assert_equal(input_value, reference_value[, value_name=None, formatter=None]):
</div>
<div style="padding-left: 6em;">
Throws an exception if <code>input_value</code> does not equal <code>reference_value</code>. The <code>name</code> of the value is included in the exception if it is not <code>None</code>, and <code>formatter</code> is used to format the values if it is not <code>None</code>.
</div>



<div><br></div>


<a name="ReaderBase"></a>
<code style="display: block; color: #FFA000;">
<span>ReaderBase <a href="#ReaderBase">#</a></code>

<div style="padding-left: 2em;">
Inherits from <code>IBinaryParser</code>
. A base class for a parser that deserializes bytes to Python objects.
</div><span style="padding-left: 2em; color: #2094F3;">
Descriptor Method:</span> <span><code>deserialize</code></span><div style="padding-left: 2em;">
Additional Functions:
</div>
<div style="padding-left: 4em; color: #2094F3;">
FileIO(filepath):
</div>
<div style="padding-left: 6em;">
Constructs the Reader with an <code>io.BufferedReader</code> stream context. Sets <code>read_bytes</code> to the <code>read</code> method of the stream.
</div>

<div style="padding-left: 4em; color: #2094F3;">
BytestreamIO(initializer):
</div>
<div style="padding-left: 6em;">
Constructs the Reader with an <code>io.BytesIO</code> stream context. Sets <code>read_bytes</code> to the <code>read</code> method of the stream.
</div>

<div style="padding-left: 4em; color: #2094F3;">
_default_read_bytes(length):
</div>
<div style="padding-left: 6em;">
The default function assigned to <code>read_bytes</code> when not in a stream context.
</div>

<div style="padding-left: 4em; color: #2094F3;">
read_bytes(length):
</div>
<div style="padding-left: 6em;">
A label that which the bytes-reading method of the stream is intended to be monkey-patched onto to avoid an extra attribute lookup and provide a unified API over different streams, <i>i.e.</i> <code>rw.read_bytes</code> vs. <code>rw._bytestream.read</code>.
</div>

<div style="padding-left: 4em; color: #2094F3;">
peek_bytestring(length):
</div>
<div style="padding-left: 6em;">
Reads up to <code>length</code> bytes from the stream without advancing the stream offset.
</div>



<div><br></div>


<a name="ValidatorBase"></a>
<code style="display: block; color: #FFA000;">
<span>ValidatorBase <a href="#ValidatorBase">#</a></code>

<div style="padding-left: 2em;">
Inherits from <code>IBinaryParser</code>
. A base class for a parser that verifies whether two bytestreams deserialize to identical Python objects, and if not, to raises an error that originates at the first pair of read calls that deserialize to different values.
</div><span style="padding-left: 2em; color: #2094F3;">
Descriptor Method:</span> <span><code>deserialize</code></span><div style="padding-left: 2em;">
Additional Functions:
</div>
<div style="padding-left: 4em; color: #2094F3;">
PrimaryFileIO(filepath):
</div>
<div style="padding-left: 6em;">
Constructs the Validator's primary stream with an <code>io.BufferedReader</code> stream context.
</div>

<div style="padding-left: 4em; color: #2094F3;">
PrimaryBytestreamIO(initializer):
</div>
<div style="padding-left: 6em;">
Constructs the Validator's primary stream with an <code>io.BytesIO</code> stream context.
</div>

<div style="padding-left: 4em; color: #2094F3;">
ReferenceFileIO(filepath):
</div>
<div style="padding-left: 6em;">
Constructs the Validator's reference stream with an <code>io.BufferedReader</code> stream context.
</div>

<div style="padding-left: 4em; color: #2094F3;">
ReferenceBytestreamIO(initializer):
</div>
<div style="padding-left: 6em;">
Constructs the Validator's reference stream with an <code>io.BytesIO</code> stream context.
</div>

<div style="padding-left: 4em; color: #2094F3;">
_default_read_bytes(length):
</div>
<div style="padding-left: 6em;">
The default function assigned to <code>read_bytes</code> when not in a stream context.
</div>

<div style="padding-left: 4em; color: #2094F3;">
read_bytes(length):
</div>
<div style="padding-left: 6em;">
A label that which the bytes-reading method of the stream is intended to be monkey-patched onto to avoid an extra attribute lookup and provide a unified API over different streams, <i>i.e.</i> <code>rw.read_bytes</code> vs. <code>rw._bytestream.read</code>.
</div>

<div style="padding-left: 4em; color: #2094F3;">
peek_bytestring(length):
</div>
<div style="padding-left: 6em;">
Reads up to <code>length</code> bytes from the stream without advancing the stream offset.
</div>



<div><br></div>


<a name="WriterBase"></a>
<code style="display: block; color: #FFA000;">
<span>WriterBase <a href="#WriterBase">#</a></code>

<div style="padding-left: 2em;">
Inherits from <code>IBinaryParser</code>
. A base class for a parser that serializes Python objects to bytes.
</div><span style="padding-left: 2em; color: #2094F3;">
Descriptor Method:</span> <span><code>serialize</code></span><div style="padding-left: 2em;">
Additional Functions:
</div>
<div style="padding-left: 4em; color: #2094F3;">
FileIO(filepath):
</div>
<div style="padding-left: 6em;">
Constructs the Writer with an <code>io.BufferedReader</code> stream context.
</div>

<div style="padding-left: 4em; color: #2094F3;">
BytestreamIO(initializer):
</div>
<div style="padding-left: 6em;">
Constructs the Writer with an <code>io.BytesIO</code> stream context.
</div>

<div style="padding-left: 4em; color: #2094F3;">
write_bytes(length):
</div>
<div style="padding-left: 6em;">
A label that which the bytes-reading method of the stream is intended to be monkey-patched onto to avoid an extra attribute lookup and provide a unified API over different streams, <i>i.e.</i> <code>rw.write_bytes</code> vs. <code>rw._bytestream.write</code>.
</div>



<div><br></div>


<a name="CounterBase"></a>
<code style="display: block; color: #FFA000;">
<span>CounterBase <a href="#CounterBase">#</a></code>

<div style="padding-left: 2em;">
Inherits from <code>IBinaryParser</code>
. A base class for a parser that counts how many bytes a stream pointer will advance for each operator call.
</div><span style="padding-left: 2em; color: #2094F3;">
Descriptor Method:</span> <span><code>count</code></span><div style="padding-left: 2em;">
Additional Functions:
</div>
<div style="padding-left: 4em; color: #2094F3;">
advance_offset(value):
</div>
<div style="padding-left: 6em;">
Increments the stream offset by <code>value</code>.
</div>



<div><br></div>


<a name="OffsetCalculatorBase"></a>
<code style="display: block; color: #FFA000;">
<span>OffsetCalculatorBase <a href="#OffsetCalculatorBase">#</a></code>

<div style="padding-left: 2em;">
Inherits from <code>CounterBase</code>
. A base class for a parser that counts how many bytes a stream pointer will advance for each operator call, and using this calculates the value of stream-offset variables within a structure.
</div><span style="padding-left: 2em; color: #2094F3;">
Descriptor Method:</span> <span><code>calculate_offsets</code> if it exists. Else, <code>count</code></span>


## Streams<a name="ValidatorStream"></a>
<code style="display: block; color: #FFA000;">
<span>ValidatorStream <a href="#ValidatorStream">#</a></code>

<div style="padding-left: 2em;">
A stream used by ValidatorBase.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Functions:
</div>

<div style="padding-left: 4em; color: #2094F3;">
set_primary_stream(stream):
</div>
<div style="padding-left: 6em;">
Sets the primary stream of the ValidatorStream.
</div>

<div style="padding-left: 4em; color: #2094F3;">
set_reference_stream(stream):
</div>
<div style="padding-left: 6em;">
Sets the reference stream of the ValidatorStream.
</div>

<div style="padding-left: 4em; color: #2094F3;">
close():
</div>
<div style="padding-left: 6em;">
Closes the primary and reference streams, if they are not <code>None</code>.
</div>

<div style="padding-left: 4em; color: #2094F3;">
seek(offset):
</div>
<div style="padding-left: 6em;">
Seeks both the primary and reference streams to the given <code>offset</code>.
</div>

<div style="padding-left: 4em; color: #2094F3;">
tell():
</div>
<div style="padding-left: 6em;">
Returns the position of the primary stream, which should be synchronised with the reference stream.
</div>

<div style="padding-left: 4em; color: #2094F3;">
read(count):
</div>
<div style="padding-left: 6em;">
Reads <code>count</code> from both streams and raises a <code>ValidationError</code> if they are not equal.
</div>

<div style="padding-left: 4em; color: #2094F3;">
write(data):
</div>
<div style="padding-left: 6em;">
Raises <code>NotImplementedError</code>.
</div>
