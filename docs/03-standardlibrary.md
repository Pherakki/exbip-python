# Standard Library
Namespace: `exbip`



## Parsers

<a name="Reader"></a>
<code style="display: block; color: #FFA000;">
<span>Reader <a href="#Reader">#</a></code>

<div style="padding-left: 2em;">
Inherits from <code>ReaderBase</code>. Implements the standard library descriptors. A parser for deserializing bytes to Python objects. Designed for contiguous parsing.
</div><span style="padding-left: 2em; color: #2094F3;">
Descriptor Method:</span> <span><code>deserialize</code></span><div style="padding-left: 2em;">
Operator Aliases:
</div>
<span style="padding-left: 4em; color: #2094F3;">
check_stream_offset</span><span> -> </span><span style="color: #2094F3;">verify_stream_offset</span>



<div><br></div>


<a name="NonContiguousReader"></a>
<code style="display: block; color: #FFA000;">
<span>NonContiguousReader <a href="#NonContiguousReader">#</a></code>

<div style="padding-left: 2em;">
Inherits from <code>ReaderBase</code>. Implements the standard library descriptors. A parser for deserializing bytes to Python objects. Designed for non-contiguous parsing.
</div><span style="padding-left: 2em; color: #2094F3;">
Descriptor Method:</span> <span><code>deserialize</code></span><div style="padding-left: 2em;">
Operator Aliases:
</div>
<span style="padding-left: 4em; color: #2094F3;">
check_stream_offset</span><span> -> </span><span style="color: #2094F3;">enforce_stream_offset</span>



<div><br></div>


<a name="Validator"></a>
<code style="display: block; color: #FFA000;">
<span>Validator <a href="#Validator">#</a></code>

<div style="padding-left: 2em;">
Inherits from <code>ValidatorBase</code>. Implements the standard library descriptors. A parser to verify whether two bytestreams deserialize to identical Python objects, and if not, to raise an error that originates at the first pair of read calls that deserialize to different values. Designed for contiguous parsing.
</div><span style="padding-left: 2em; color: #2094F3;">
Descriptor Method:</span> <span><code>deserialize</code></span><div style="padding-left: 2em;">
Operator Aliases:
</div>
<span style="padding-left: 4em; color: #2094F3;">
check_stream_offset</span><span> -> </span><span style="color: #2094F3;">verify_stream_offset</span>



<div><br></div>


<a name="Writer"></a>
<code style="display: block; color: #FFA000;">
<span>Writer <a href="#Writer">#</a></code>

<div style="padding-left: 2em;">
Inherits from <code>WriterBase</code>. Implements the standard library descriptors. A parser for serializing Python objects to bytes. Designed for contiguous parsing.
</div><span style="padding-left: 2em; color: #2094F3;">
Descriptor Method:</span> <span><code>serialize</code></span><div style="padding-left: 2em;">
Operator Aliases:
</div>
<span style="padding-left: 4em; color: #2094F3;">
check_stream_offset</span><span> -> </span><span style="color: #2094F3;">verify_stream_offset</span>



<div><br></div>


<a name="Counter"></a>
<code style="display: block; color: #FFA000;">
<span>Counter <a href="#Counter">#</a></code>

<div style="padding-left: 2em;">
Inherits from <code>CounterBase</code>. Implements the standard library descriptors. A parser for counting how many bytes a stream pointer will advance for each operator call. Designed for contiguous parsing.
</div><span style="padding-left: 2em; color: #2094F3;">
Descriptor Method:</span> <span><code>count</code></span><div style="padding-left: 2em;">
Operator Aliases:
</div>
<span style="padding-left: 4em; color: #2094F3;">
check_stream_offset</span><span> -> </span><span style="color: #2094F3;">verify_stream_offset</span>



<div><br></div>


<a name="OffsetCalculator"></a>
<code style="display: block; color: #FFA000;">
<span>OffsetCalculator <a href="#OffsetCalculator">#</a></code>

<div style="padding-left: 2em;">
Inherits from <code>OffsetCalculatorBase</code>. Implements the standard library descriptors. A parser for counting how many bytes a stream pointer will advance for each operator call, and using this to calculate the value of stream-offset variables within a structure.
</div><span style="padding-left: 2em; color: #2094F3;">
Descriptor Method:</span> <span><code>calculate_offsets</code> if it exists. Else, <code>count</code></span><div style="padding-left: 2em;">
Operator Aliases:
</div>
<span style="padding-left: 4em; color: #2094F3;">
check_stream_offset</span><span> -> </span><span style="color: #2094F3;">verify_stream_offset</span>



## Traits

<a name="ReadableTrait"></a>
<code style="display: block; color: #FFA000;">
<span>ReadableTrait(Reader): <a href="#ReadableTrait">#</a></code>

<div style="padding-left: 2em;">
A trait that adds deserialization methods to a structure.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Functions:
</div>

<div style="padding-left: 4em; color: #2094F3;">
read(filepath, \*args, \*\*kwargs):
</div>
<div style="padding-left: 6em;">
Passes <code>filepath</code> to the <code>FileIO()</code> method of <code>Reader</code>.
</div>

<div style="padding-left: 4em; color: #2094F3;">
frombytes(byte_data, \*args, \*\*kwargs):
</div>
<div style="padding-left: 6em;">
Passes <code>byte_data</code> to the <code>BytestreamIO()</code> method of <code>Reader</code>.
</div>

<a name="WriteableTrait"></a>
<code style="display: block; color: #FFA000;">
<span>WriteableTrait(Writer): <a href="#WriteableTrait">#</a></code>

<div style="padding-left: 2em;">
A trait that adds serialization methods to a structure.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Functions:
</div>

<div style="padding-left: 4em; color: #2094F3;">
write(filepath, \*args, \*\*kwargs):
</div>
<div style="padding-left: 6em;">
Passes <code>filepath</code> to the <code>FileIO()</code> method of <code>Writer</code>.
</div>

<div style="padding-left: 4em; color: #2094F3;">
tobytes(\*args, \*\*kwargs):
</div>
<div style="padding-left: 6em;">
Returns the bytes written to the stream initialized by the <code>BytestreamIO()</code> method of <code>Writer</code>.
</div>

<a name="ValidatableTrait"></a>
<code style="display: block; color: #FFA000;">
<span>ValidatableTrait(Validator): <a href="#ValidatableTrait">#</a></code>

<div style="padding-left: 2em;">
A trait that adds validation methods to a structure.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Functions:
</div>

<div style="padding-left: 4em; color: #2094F3;">
validate_file_against_file(primary_filepath, reference_filepath, \*args, \*\*kwargs):
</div>
<div style="padding-left: 6em;">
Validates the data in <code>primary_filepath</code> against the data in <code>reference_filepath</code>.
</div>

<div style="padding-left: 4em; color: #2094F3;">
validate_file_against_bytes(primary_filepath, reference_bytes,    \*args, \*\*kwargs):
</div>
<div style="padding-left: 6em;">
Validates the data in <code>primary_filepath</code> against the bytes in <code>reference_bytes</code>.
</div>

<div style="padding-left: 4em; color: #2094F3;">
validate_bytes_against_file(primary_bytes,    reference_filepath, \*args, \*\*kwargs):
</div>
<div style="padding-left: 6em;">
Validates the bytes in <code>primary_bytes</code> against the data in <code>reference_filepath</code>.
</div>

<div style="padding-left: 4em; color: #2094F3;">
validate_bytes_against_bytes(primary_bytes,    reference_bytes,    \*args, \*\*kwargs):
</div>
<div style="padding-left: 6em;">
Validates the bytes in <code>primary_bytes</code> against the bytes in <code>reference_bytes</code>.
</div>

<a name="OffsetsCalculableTrait"></a>
<code style="display: block; color: #FFA000;">
<span>OffsetsCalculableTrait(OffsetCalculator): <a href="#OffsetsCalculableTrait">#</a></code>

<div style="padding-left: 2em;">
A trait that adds offset calculation methods to a structure.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Functions:
</div>

<div style="padding-left: 4em; color: #2094F3;">
calculate_offsets(obj, \*args, \*\*kwargs):
</div>
<div style="padding-left: 6em;">
Calls <code>OffsetCalculator.rw_obj(obj, \*args, \*\*kwargs)</code> on an instance of <code>OffsetCalculator</code>. This is intended to be used to automatically calculate the values of file offsets.
</div>



## Operations



### Primitives
<a name="rw_int8"></a>
<code style="display: block; color: #FFA000;">
<span>rw_int8(value): <a href="#rw_int8">#</a></code>

<div style="padding-left: 2em;">
Operates on a signed 8-bit integer with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns a signed 8-bit integer unpacked from the stream.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> to 1 byte and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by 1. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int8_le(value)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int8_be(value)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int8_e(value, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_int16"></a>
<code style="display: block; color: #FFA000;">
<span>rw_int16(value): <a href="#rw_int16">#</a></code>

<div style="padding-left: 2em;">
Operates on a signed 16-bit integer with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns a signed 16-bit integer unpacked from the stream.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> to 2 bytes and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by 2. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int16_le(value)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int16_be(value)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int16_e(value, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_int32"></a>
<code style="display: block; color: #FFA000;">
<span>rw_int32(value): <a href="#rw_int32">#</a></code>

<div style="padding-left: 2em;">
Operates on a signed 32-bit integer with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns a signed 32-bit integer unpacked from the stream.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> to 4 bytes and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by 4. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int32_le(value)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int32_be(value)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int32_e(value, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_int64"></a>
<code style="display: block; color: #FFA000;">
<span>rw_int64(value): <a href="#rw_int64">#</a></code>

<div style="padding-left: 2em;">
Operates on a signed 64-bit integer with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns a signed 64-bit integer unpacked from the stream.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> to 8 bytes and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by 8. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int64_le(value)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int64_be(value)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int64_e(value, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_uint8"></a>
<code style="display: block; color: #FFA000;">
<span>rw_uint8(value): <a href="#rw_uint8">#</a></code>

<div style="padding-left: 2em;">
Operates on an unsigned 8-bit integer with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an unsigned 8-bit integer unpacked from the stream.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> to 1 byte and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by 1. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint8_le(value)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint8_be(value)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint8_e(value, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_uint16"></a>
<code style="display: block; color: #FFA000;">
<span>rw_uint16(value): <a href="#rw_uint16">#</a></code>

<div style="padding-left: 2em;">
Operates on an unsigned 16-bit integer with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an unsigned 16-bit integer unpacked from the stream.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> to 2 bytes and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by 2. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint16_le(value)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint16_be(value)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint16_e(value, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_uint32"></a>
<code style="display: block; color: #FFA000;">
<span>rw_uint32(value): <a href="#rw_uint32">#</a></code>

<div style="padding-left: 2em;">
Operates on an unsigned 32-bit integer with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an unsigned 32-bit integer unpacked from the stream.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> to 4 bytes and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by 4. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint32_le(value)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint32_be(value)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint32_e(value, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_uint64"></a>
<code style="display: block; color: #FFA000;">
<span>rw_uint64(value): <a href="#rw_uint64">#</a></code>

<div style="padding-left: 2em;">
Operates on an unsigned 64-bit integer with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an unsigned 64-bit integer unpacked from the stream.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> to 8 bytes and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by 8. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint64_le(value)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint64_be(value)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint64_e(value, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_float16"></a>
<code style="display: block; color: #FFA000;">
<span>rw_float16(value): <a href="#rw_float16">#</a></code>

<div style="padding-left: 2em;">
Operates on an IEEE 16-bit float with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an IEEE 16-bit float unpacked from the stream.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> to 2 bytes and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by 2. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float16_le(value)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float16_be(value)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float16_e(value, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_float32"></a>
<code style="display: block; color: #FFA000;">
<span>rw_float32(value): <a href="#rw_float32">#</a></code>

<div style="padding-left: 2em;">
Operates on an IEEE 32-bit float with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an IEEE 32-bit float unpacked from the stream.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> to 4 bytes and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by 4. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float32_le(value)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float32_be(value)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float32_e(value, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_float64"></a>
<code style="display: block; color: #FFA000;">
<span>rw_float64(value): <a href="#rw_float64">#</a></code>

<div style="padding-left: 2em;">
Operates on an IEEE 64-bit float with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an IEEE 64-bit float unpacked from the stream.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> to 8 bytes and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by 8. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float64_le(value)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float64_be(value)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float64_e(value, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



### Primitive Arrays
<a name="rw_int8s"></a>
<code style="display: block; color: #FFA000;">
<span>rw_int8s(value, shape): <a href="#rw_int8s">#</a></code>

<div style="padding-left: 2em;">
Operates on an array of signed 8-bit integers with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an array of signed 8-bit integers unpacked from the stream, row-major reshaped to the dimensions given by <code>shape</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> in row-major order and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by the binary size of <code>value</code>. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int8s_le(value, shape)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int8s_be(value, shape)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int8s_e(value, shape, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_int16s"></a>
<code style="display: block; color: #FFA000;">
<span>rw_int16s(value, shape): <a href="#rw_int16s">#</a></code>

<div style="padding-left: 2em;">
Operates on an array of signed 16-bit integers with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an array of signed 16-bit integers unpacked from the stream, row-major reshaped to the dimensions given by <code>shape</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> in row-major order and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by the binary size of <code>value</code>. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int16s_le(value, shape)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int16s_be(value, shape)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int16s_e(value, shape, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_int32s"></a>
<code style="display: block; color: #FFA000;">
<span>rw_int32s(value, shape): <a href="#rw_int32s">#</a></code>

<div style="padding-left: 2em;">
Operates on an array of signed 32-bit integers with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an array of signed 32-bit integers unpacked from the stream, row-major reshaped to the dimensions given by <code>shape</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> in row-major order and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by the binary size of <code>value</code>. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int32s_le(value, shape)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int32s_be(value, shape)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int32s_e(value, shape, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_int64s"></a>
<code style="display: block; color: #FFA000;">
<span>rw_int64s(value, shape): <a href="#rw_int64s">#</a></code>

<div style="padding-left: 2em;">
Operates on an array of signed 64-bit integers with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an array of signed 64-bit integers unpacked from the stream, row-major reshaped to the dimensions given by <code>shape</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> in row-major order and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by the binary size of <code>value</code>. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int64s_le(value, shape)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int64s_be(value, shape)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_int64s_e(value, shape, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_uint8s"></a>
<code style="display: block; color: #FFA000;">
<span>rw_uint8s(value, shape): <a href="#rw_uint8s">#</a></code>

<div style="padding-left: 2em;">
Operates on an array of unsigned 8-bit integers with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an array of unsigned 8-bit integers unpacked from the stream, row-major reshaped to the dimensions given by <code>shape</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> in row-major order and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by the binary size of <code>value</code>. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint8s_le(value, shape)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint8s_be(value, shape)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint8s_e(value, shape, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_uint16s"></a>
<code style="display: block; color: #FFA000;">
<span>rw_uint16s(value, shape): <a href="#rw_uint16s">#</a></code>

<div style="padding-left: 2em;">
Operates on an array of unsigned 16-bit integers with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an array of unsigned 16-bit integers unpacked from the stream, row-major reshaped to the dimensions given by <code>shape</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> in row-major order and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by the binary size of <code>value</code>. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint16s_le(value, shape)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint16s_be(value, shape)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint16s_e(value, shape, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_uint32s"></a>
<code style="display: block; color: #FFA000;">
<span>rw_uint32s(value, shape): <a href="#rw_uint32s">#</a></code>

<div style="padding-left: 2em;">
Operates on an array of unsigned 32-bit integers with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an array of unsigned 32-bit integers unpacked from the stream, row-major reshaped to the dimensions given by <code>shape</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> in row-major order and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by the binary size of <code>value</code>. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint32s_le(value, shape)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint32s_be(value, shape)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint32s_e(value, shape, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_uint64s"></a>
<code style="display: block; color: #FFA000;">
<span>rw_uint64s(value, shape): <a href="#rw_uint64s">#</a></code>

<div style="padding-left: 2em;">
Operates on an array of unsigned 64-bit integers with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an array of unsigned 64-bit integers unpacked from the stream, row-major reshaped to the dimensions given by <code>shape</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> in row-major order and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by the binary size of <code>value</code>. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint64s_le(value, shape)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint64s_be(value, shape)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_uint64s_e(value, shape, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_float16s"></a>
<code style="display: block; color: #FFA000;">
<span>rw_float16s(value, shape): <a href="#rw_float16s">#</a></code>

<div style="padding-left: 2em;">
Operates on an array of IEEE 16-bit floats with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an array of IEEE 16-bit floats unpacked from the stream, row-major reshaped to the dimensions given by <code>shape</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> in row-major order and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by the binary size of <code>value</code>. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float16s_le(value, shape)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float16s_be(value, shape)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float16s_e(value, shape, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_float32s"></a>
<code style="display: block; color: #FFA000;">
<span>rw_float32s(value, shape): <a href="#rw_float32s">#</a></code>

<div style="padding-left: 2em;">
Operates on an array of IEEE 32-bit floats with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an array of IEEE 32-bit floats unpacked from the stream, row-major reshaped to the dimensions given by <code>shape</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> in row-major order and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by the binary size of <code>value</code>. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float32s_le(value, shape)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float32s_be(value, shape)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float32s_e(value, shape, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



<div><br></div>


<a name="rw_float64s"></a>
<code style="display: block; color: #FFA000;">
<span>rw_float64s(value, shape): <a href="#rw_float64s">#</a></code>

<div style="padding-left: 2em;">
Operates on an array of IEEE 64-bit floats with context-sensitive endianness.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an array of IEEE 64-bit floats unpacked from the stream, row-major reshaped to the dimensions given by <code>shape</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Packs <code>value</code> in row-major order and writes it to the stream. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by the binary size of <code>value</code>. Returns <code>value</code>.
</div>
<div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Variants:
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float64s_le(value, shape)</code>

Forced little-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float64s_be(value, shape)</code>

Forced big-endian mode.
</div>

<div style="padding-left: 4em;">
<code style="color: #FFA000;">rw_float64s_e(value, shape, endianness)</code>

Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.
</div>



### Strings
<a name="rw_bytestring"></a>
<code style="display: block; color: #FFA000;">
<span>rw_bytestring(value, length): <a href="#rw_bytestring">#</a></code>

<div style="padding-left: 2em;">
Operates on a fixed-size bytestring.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Reads <code>length</code> chars from the stream. Returns a <code>bytes</code> object.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Writes <code>value</code> to the stream. Expects <code>value</code> to be a <code>bytes</code>-like object. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by the length of <code>value</code>. Expects <code>value</code> to be a <code>bytes</code> object. Returns <code>value</code>.
</div>



<div><br></div>


<a name="rw_bytestrings"></a>
<code style="display: block; color: #FFA000;">
<span>rw_bytestrings(value, lengths): <a href="#rw_bytestrings">#</a></code>

<div style="padding-left: 2em;">
Operates on a list of fixed-size bytestrings.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Reads <code>length</code> chars from the stream. Returns a <code>List[bytes]</code> object.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Writes each element in <code>value</code> to the stream. Expects <code>value</code> to be an iterable of <code>bytes</code>-like objects. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by the sum of all lengths in <code>value</code>. Expects <code>value</code> to be an iterable of <code>bytes</code>-like objects. Returns <code>value</code>.
</div>



<div><br></div>


<a name="rw_cbytestring"></a>
<code style="display: block; color: #FFA000;">
<span>rw_cbytestring(value[, chunksize=0x40, terminator=b'\x00']): <a href="#rw_cbytestring">#</a></code>

<div style="padding-left: 2em;">
Operates on a terminated bytestring.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Reads chars from the stream in blocks of <code>chunksize</code> until the <code>terminator</code> pattern is identified in one of those blocks. Returns a <code>bytes</code> object without the terminator.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Writes <code>value</code> to the stream, and then writes the <code>terminator</code>. Expects <code>value</code> to be a <code>bytes</code>-like object. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by the length of <code>value</code> plus the length of the <code>terminator</code>. Expects <code>value</code> to be an iterable of <code>bytes</code>-like objects. Returns <code>value</code>.
</div>



<div><br></div>


<a name="rw_cbytestrings"></a>
<code style="display: block; color: #FFA000;">
<span>rw_cbytestrings(value, count[, chunksize=0x40, terminator=b'\x00']): <a href="#rw_cbytestrings">#</a></code>

<div style="padding-left: 2em;">
Operates on a list of terminated bytestrings.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Reads chars from the stream in blocks of <code>chunksize</code> until the <code>terminator</code> pattern is identified in one of those blocks, <code>count</code> times. Returns a <code>List[bytes]</code> object.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Writes each element (followed by the <code>terminator</code>) in <code>value</code> to the stream. Expects <code>value</code> to be an iterable of <code>bytes</code>-like objects. Returns <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Increments the stream offset by the sum of all lengths in <code>value</code> (plus the requisite <code>terminator</code> lengths). Expects <code>value</code> to be an iterable of <code>bytes</code>-like objects. Returns <code>value</code>.
</div>



### Descriptors
<a name="rw_descriptor"></a>
<code style="display: block; color: #FFA000;">
<span>rw_descriptor(descriptor, \*args, \*\*kwargs): <a href="#rw_descriptor">#</a></code>

<div style="padding-left: 2em;">
Looks for and executes the descriptor method required by the parser.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Invokes the 'deserialize' method of the descriptor.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Invokes the 'serialize' method of the descriptor.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Invokes the 'count' method of the descriptor.
</div>



### Objects
<a name="rw_obj"></a>
<code style="display: block; color: #FFA000;">
<span>rw_obj(value, \*args, \*\*kwargs): <a href="#rw_obj">#</a></code>

<div style="padding-left: 2em;">
Executes the <code>exbip_rw</code> function on <code>value</code>.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Calls <code>exbip_rw</code> on <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Calls <code>exbip_rw</code> on <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Calls <code>exbip_rw</code> on <code>value</code>.
</div>



<div><br></div>


<a name="rw_dynamic_obj"></a>
<code style="display: block; color: #FFA000;">
<span>rw_dynamic_obj(value, constructor, \*args, \*\*kwargs): <a href="#rw_dynamic_obj">#</a></code>

<div style="padding-left: 2em;">
Executes the <code>exbip_rw</code> function on <code>value</code> if not deserializing, otherwise constructs it first.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Calls <code>constructor</code> to build a new object, then calls <code>exbip_rw</code> on it.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Calls <code>exbip_rw</code> on <code>value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Calls <code>exbip_rw</code> on <code>value</code>.
</div>



<div><br></div>


<a name="rw_dynamic_objs"></a>
<code style="display: block; color: #FFA000;">
<span>rw_dynamic_objs(values, constructor, count, \*args, \*\*kwargs): <a href="#rw_dynamic_objs">#</a></code>

<div style="padding-left: 2em;">
Executes the <code>exbip_rw</code> function on <code>value</code> if not deserializing, otherwise constructs to object array first from a count.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Calls <code>constructor</code> to build a new object, then calls <code>exbip_rw</code> on it, <code>count</code> times.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Calls <code>exbip_rw</code> on each element in <code>values</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Calls <code>exbip_rw</code> on each element in <code>values</code>.
</div>



<div><br></div>


<a name="rw_dynamic_objs_while"></a>
<code style="display: block; color: #FFA000;">
<span>rw_dynamic_objs_while(values, constructor, condition, \*args, \*\*kwargs): <a href="#rw_dynamic_objs_while">#</a></code>

<div style="padding-left: 2em;">
Executes the <code>exbip_rw</code> function on <code>value</code> if not deserializing, otherwise constructs to object array first from a boolean condition.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Calls <code>constructor</code> to build a new object, then calls <code>exbip_rw</code> on it, until calling <code>condition</code> returns False. <code>condition</code> must be a function (or functor) that takes the parser as its only argument.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Calls <code>exbip_rw</code> on each element in <code>values</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Calls <code>exbip_rw</code> on each element in <code>values</code>.
</div>



### Iterators
<a name="array_iterator"></a>
<code style="display: block; color: #FFA000;">
<span>array_iterator(array, constructor, count): <a href="#array_iterator">#</a></code>

<div style="padding-left: 2em;">
Returns an iterable object that will construct <code>count</code> array elements if deserializing, and iterate through an array if not. Example:
</div>

```python
for i, obj in enumerate(rw.array_iterator(arr, MyObject, my_count)):
    rw.check_stream_offset(obj_offsets[i], "Object {i}", HEX32_FORMATTER)
    rw.rw_obj(obj)
```

<div style="padding-left: 2em">This can be used for more advanced looping behavior than <i>e.g.</i> <code>rw_dynamic_objs</code>.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an iterable object that clears the given array, and then appends a newly-constructed object to the array at the start of each iteration.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Returns an iterable object that iterates through the elements of <code>array</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Returns an iterable object that iterates through the elements of <code>array</code>.
</div>



<div><br></div>


<a name="array_while_iterator"></a>
<code style="display: block; color: #FFA000;">
<span>array_while_iterator(array, constructor, stop_condition): <a href="#array_while_iterator">#</a></code>

<div style="padding-left: 2em;">
Returns an iterable object that will construct array elements until <code>condition</code> is False if deserializing, and iterate through an array if not. Example:
</div>

```python
class Cond:
    def __init__(self, offset):
        self.offset = offset

    def __call__(self, rw):
        return rw.tell() < self.offset

offset_list = []
for obj in rw.array_while_iterator(arr, MyObject, Cond(offset)):
    offset_list.append(rw.tell())
    rw.rw_obj(obj)
```

<div style="padding-left: 2em">This can be used for more advanced looping behavior than <i>e.g.</i> <code>rw_dynamic_objs_while</code>.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns an iterable object that clears the given array, and then appends a newly-constructed object to the array at the start of each iteration.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Returns an iterable object that iterates through the elements of <code>array</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Returns an iterable object that iterates through the elements of <code>array</code>.
</div>



### Sections
<a name="section_exists"></a>
<code style="display: block; color: #FFA000;">
<span>section_exists(offset, count): <a href="#section_exists">#</a></code>

<div style="padding-left: 2em;">
Returns a bool that states whether a data section defined by a non-zero offset and/or count exists or not.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Returns True if <code>offset</code> is greater than 0.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Returns True if <code>count</code> is greater than 0.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Returns True if <code>count</code> is greater than 0.
</div>



### Stream End-of-file
<a name="assert_eof"></a>
<code style="display: block; color: #FFA000;">
<span>assert_eof(): <a href="#assert_eof">#</a></code>

<div style="padding-left: 2em;">
Raises an exception if the stream pointer is not at the end of the stream, if the parsing mode defines an end-of-stream.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Raises a <code>NotAtEOFError</code> if the stream pointer is not at the end of the stream.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Does nothing.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Does nothing.
</div>



### Stream Alignment
<a name="align"></a>
<code style="display: block; color: #FFA000;">
<span>align(offset, alignment(, pad_value=b'\x00'): <a href="#align">#</a></code>

<div style="padding-left: 2em;">
Rounds up <code>offset</code> to the next multiple of <code>alignment</code>, and performs an operation on the section of the stream corresponding to the skipped bytes.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Reads enough bytes to perform the alignment, and validates that they are an array of <code>pad_value</code>s. Raises <code>ValueError</code> if the number of bytes required for the alignment is not divisible by the length of <code>pad_value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Writes enough <code>pad_value</code>s to the stream to perform the alignment. Raises <code>ValueError</code> if the number of bytes required for the alignment is not divisible by the length of <code>pad_value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Advances the stream offset to the next multiple of <code>alignment</code>. Raises <code>ValueError</code> if the number of bytes required for the alignment is not divisible by the length of <code>pad_value</code>.
</div>



<div><br></div>


<a name="fill"></a>
<code style="display: block; color: #FFA000;">
<span>fill(offset, alignment(, fill_value=b'\x00'): <a href="#fill">#</a></code>

<div style="padding-left: 2em;">
Rounds up <code>offset</code> to the next multiple of <code>alignment</code>, and performs an operation on the section of the stream corresponding to the skipped bytes.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Reads enough bytes to perform the alignment. Does not perform any validation.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Writes enough <code>pad_value</code>s to the stream to perform the alignment. Raises <code>ValueError</code> if the number of bytes required for the alignment is not divisible by the length of <code>pad_value</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Advances the stream offset to the next multiple of <code>alignment</code>. Raises <code>ValueError</code> if the number of bytes required for the alignment is not divisible by the length of <code>pad_value</code>.
</div>



### Stream Offsets
<a name="verify_stream_offset"></a>
<code style="display: block; color: #FFA000;">
<span>verify_stream_offset(offset, message[, formatter=lambda x: x, notifier=None]): <a href="#verify_stream_offset">#</a></code>

<div style="padding-left: 2em;">
Seeks to <code>offset</code>, throws an error if the stream offset is not at <code>offset</code>, or calls <code>notifier</code> with the current stream offset.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Seeks to <code>offset</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Throws a <code>UnexpectedOffsetError</code> if the stream offset is not at <code>offset</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Does nothing.
</div>
<div style="padding-left: 2em; color: #2094F3;">
calculate_offsets:
</div>
<div style="padding-left: 4em;">
Calls <code>notifier.notify()</code> if <code>notifier</code> is not None. Commonly, <code>notifier</code> is an <code>OffsetMarker</code> object.
</div>



<div><br></div>


<a name="navigate_stream_offset"></a>
<code style="display: block; color: #FFA000;">
<span>navigate_stream_offset(offset, message[, formatter=lambda x: x, notifier=None]): <a href="#navigate_stream_offset">#</a></code>

<div style="padding-left: 2em;">
Seeks to <code>offset</code>, throws an error if the stream offset is not at <code>offset</code>, or calls <code>notifier</code> with the current stream offset.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Seeks to <code>offset</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Does nothing.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Does nothing.
</div>
<div style="padding-left: 2em; color: #2094F3;">
calculate_offsets:
</div>
<div style="padding-left: 4em;">
Calls <code>notifier.notify()</code> if <code>notifier</code> is not None. Commonly, <code>notifier</code> is an <code>OffsetMarker</code> object.
</div>



<div><br></div>


<a name="verify_stream_offset"></a>
<code style="display: block; color: #FFA000;">
<span>verify_stream_offset(offset, message[, formatter=lambda x: x, notifier=None]): <a href="#verify_stream_offset">#</a></code>

<div style="padding-left: 2em;">
Throws an error if the stream offset is not at <code>offset</code>, or calls <code>notifier</code> with the current stream offset.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Throws a <code>UnexpectedOffsetError</code> if the stream offset is not at <code>offset</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Throws a <code>UnexpectedOffsetError</code> if the stream offset is not at <code>offset</code>.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Does nothing.
</div>
<div style="padding-left: 2em; color: #2094F3;">
calculate_offsets:
</div>
<div style="padding-left: 4em;">
Calls <code>notifier.notify()</code> if <code>notifier</code> is not None. Commonly, <code>notifier</code> is an <code>OffsetMarker</code> object.
</div>



<div><br></div>


<a name="check_stream_offset"></a>
<code style="display: block; color: #FFA000;">
<span>check_stream_offset(offset, message[, formatter=lambda x: x, notifier=None]): <a href="#check_stream_offset">#</a></code>

<div style="padding-left: 2em;">
An alias for <code>verify_stream_offset</code>. Used by all standard parsers except <code>NonContiguousReader</code>.
</div>


<div><br></div>


<a name="check_stream_offset"></a>
<code style="display: block; color: #FFA000;">
<span>check_stream_offset(offset, message[, formatter=lambda x: x, notifier=None]): <a href="#check_stream_offset">#</a></code>

<div style="padding-left: 2em;">
An alias for <code>enforce_stream_offset</code>. Used by <code>NonContiguousReader</code>.
</div>


### Stream Padding
<a name="rw_padding"></a>
<code style="display: block; color: #FFA000;">
<span>rw_padding(count[, pad_value=b'\x00', validate=True]): <a href="#rw_padding">#</a></code>

<div style="padding-left: 2em;">
Operates on an anonymous bytestring of length <code>count</code>.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Reads <code>count*len(pad_value)</code> bytes from the stream. If <code>validate</code> is True, the bytes are checked to ensure they are an array of <code>pad_value</code>. If they are not, an <code>UnexpectedPaddingError</code> is raised.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Writes <code>count</code> <code>pad_value</code>s to the stream.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Advances the stream by <code>count*len(pad_value)</code>.
</div>



### Offset Markers
<a name="dispatch_marker"></a>
<code style="display: block; color: #FFA000;">
<span>dispatch_marker(marker): <a href="#dispatch_marker">#</a></code>

<div style="padding-left: 2em;">
Operates on an object with a single-argument <code>notify</code> method, expected to be an <code>OffsetMarker</code> object.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em; color: #2094F3;">
deserialize:
</div>
<div style="padding-left: 4em;">
Does nothing.
</div>
<div style="padding-left: 2em; color: #2094F3;">
serialize:
</div>
<div style="padding-left: 4em;">
Does nothing.
</div>
<div style="padding-left: 2em; color: #2094F3;">
count:
</div>
<div style="padding-left: 4em;">
Does nothing.
</div>
<div style="padding-left: 2em; color: #2094F3;">
calculate_offsets:
</div>
<div style="padding-left: 4em;">
Calls <code>marker.notify()</code>.
</div>

## Formatters

<a name="safe_formatter"></a>
<code style="display: block; color: #FFA000;">
<span>safe_formatter(formatter): <a href="#safe_formatter">#</a></code>

<div style="padding-left: 2em;">
Returns a <code>safe_formatter</code> object that calls <code>formatter</code>, which is a format method like <i>e.g.</i> <code>'0b{0:0>8b}'.format</code>, and returns the call return value if it does not throw an exception. On throwing a <code>ValueError</code> or <code>TypeError</code>, the original value is returned. Other exceptions are uncaught.
</div>
<a name="bin8_formatter"></a>
<code style="display: block; color: #FFA000;">
<span>bin8_formatter(value): <a href="#bin8_formatter">#</a></code>

<div style="padding-left: 2em;">
A <code>safe_formatter</code> that formats <code>value</code> as an 8-bit binary string.
</div>
<a name="bin16_formatter"></a>
<code style="display: block; color: #FFA000;">
<span>bin16_formatter(value): <a href="#bin16_formatter">#</a></code>

<div style="padding-left: 2em;">
A <code>safe_formatter</code> that formats <code>value</code> as a 16-bit binary string.
</div>
<a name="bin32_formatter"></a>
<code style="display: block; color: #FFA000;">
<span>bin32_formatter(value): <a href="#bin32_formatter">#</a></code>

<div style="padding-left: 2em;">
A <code>safe_formatter</code> that formats <code>value</code> as a 32-bit binary string.
</div>
<a name="bin64_formatter"></a>
<code style="display: block; color: #FFA000;">
<span>bin64_formatter(value): <a href="#bin64_formatter">#</a></code>

<div style="padding-left: 2em;">
A <code>safe_formatter</code> that formats <code>value</code> as a 64-bit binary string.
</div>
<a name="hex8_formatter"></a>
<code style="display: block; color: #FFA000;">
<span>hex8_formatter(value): <a href="#hex8_formatter">#</a></code>

<div style="padding-left: 2em;">
A <code>safe_formatter</code> that formats <code>value</code> as an 8-bit lower-case hex string.
</div>
<a name="hex16_formatter"></a>
<code style="display: block; color: #FFA000;">
<span>hex16_formatter(value): <a href="#hex16_formatter">#</a></code>

<div style="padding-left: 2em;">
A <code>safe_formatter</code> that formats <code>value</code> as a 16-bit lower-case hex string.
</div>
<a name="hex32_formatter"></a>
<code style="display: block; color: #FFA000;">
<span>hex32_formatter(value): <a href="#hex32_formatter">#</a></code>

<div style="padding-left: 2em;">
A <code>safe_formatter</code> that formats <code>value</code> as a 32-bit lower-case hex string.
</div>
<a name="hex64_formatter"></a>
<code style="display: block; color: #FFA000;">
<span>hex64_formatter(value): <a href="#hex64_formatter">#</a></code>

<div style="padding-left: 2em;">
A <code>safe_formatter</code> that formats <code>value</code> as a 64-bit lower-case hex string.
</div>
<a name="HEX8_formatter"></a>
<code style="display: block; color: #FFA000;">
<span>HEX8_formatter(value): <a href="#HEX8_formatter">#</a></code>

<div style="padding-left: 2em;">
A <code>safe_formatter</code> that formats <code>value</code> as an 8-bit upper-case hex string.
</div>
<a name="HEX16_formatter"></a>
<code style="display: block; color: #FFA000;">
<span>HEX16_formatter(value): <a href="#HEX16_formatter">#</a></code>

<div style="padding-left: 2em;">
A <code>safe_formatter</code> that formats <code>value</code> as a 16-bit upper-case hex string.
</div>
<a name="HEX32_formatter"></a>
<code style="display: block; color: #FFA000;">
<span>HEX32_formatter(value): <a href="#HEX32_formatter">#</a></code>

<div style="padding-left: 2em;">
A <code>safe_formatter</code> that formats <code>value</code> as a 32-bit upper-case hex string.
</div>
<a name="HEX64_formatter"></a>
<code style="display: block; color: #FFA000;">
<span>HEX64_formatter(value): <a href="#HEX64_formatter">#</a></code>

<div style="padding-left: 2em;">
A <code>safe_formatter</code> that formats <code>value</code> as a 64-bit upper-case hex string.
</div>


## Structures<a name="OffsetMarker"></a>
<code style="display: block; color: #FFA000;">
<span>OffsetMarker <a href="#OffsetMarker">#</a></code>

<div style="padding-left: 2em;">
A class that holds a list of single-argument callbacks. When <code>notify</code> is called, the offset passed to <code>notify</code> is used to call each of these callbacks, each of which is intended to give a particular variable the value of that offset.
</div><div style="padding-top: 1em"></div>
<div style="padding-left: 2em;">
Functions:
</div>

<div style="padding-left: 4em; color: #2094F3;">
clear():
</div>
<div style="padding-left: 6em;">
Clears the subscriber list.
</div>

<div style="padding-left: 4em; color: #2094F3;">
subscribe(obj, attr):
</div>
<div style="padding-left: 6em;">
Adds a callback <code>lambda offset: setattr(obj, attr, offset)</code> to the <code>OffsetMarker</code>'s callbacks list. Returns <code>self</code> so that multiple subscriptions can be chained with the constructor.
</div>

<div style="padding-left: 4em; color: #2094F3;">
subscribe_callback(callback):
</div>
<div style="padding-left: 6em;">
Adds the single-argument function <code>callback</code> to the <code>OffsetMarker</code>'s callbacks list. Returns <code>self</code> so that multiple subscriptions can be chained with the constructor.
</div>

<div style="padding-left: 4em; color: #2094F3;">
notify(offset):
</div>
<div style="padding-left: 6em;">
Iterates through the list of subscribers and calls each one with <code>offset</code>.
</div>
