
LISTING_COLOR = "#FFA000"
VFUNC_COLOR   = "#2094F3"

class GenericOp:
    def __init__(self, name, sig, summary, deserialize, serialize, count, offset_calc=None):
        self.name        = name
        self.sig         = sig
        self.summary     = summary
        self.deserialize = deserialize
        self.serialize   = serialize
        self.count       = count
        self.offset_calc = offset_calc
    
    def to_string(self):
        return f"<a name=\"{self.name}\"></a>\n"\
        f"<code style=\"display: block; color: {LISTING_COLOR};\">\n"\
        f"<span>{self.name}({self.sig}): <a href=\"#{self.name}\">#</a>"\
        "</code>\n"\
        "\n"\
        "<div style=\"padding-left: 2em;\">\n"\
        f"{self.summary}.\n"\
        "</div>"\
        + ("<div style=\"padding-top: 1em\"></div>\n"
        if any(p is not None for p in [self.deserialize, self.serialize, self.count, self.offset_calc])
        else "")\
        +\
        (
        f"<div style=\"padding-left: 2em; color: {VFUNC_COLOR};\">\n"\
        "deserialize:\n"\
        "</div>\n"\
        "<div style=\"padding-left: 4em;\">\n"\
        f"{self.deserialize}.\n"\
        "</div>\n"\
        if self.deserialize is not None
        else ''
        )\
        +\
        (
        f"<div style=\"padding-left: 2em; color: {VFUNC_COLOR};\">\n"\
        "serialize:\n"\
        "</div>\n"\
        "<div style=\"padding-left: 4em;\">\n"\
        f"{self.serialize}.\n"\
        "</div>\n"\
        if self.serialize is not None
        else ''
        )\
        +\
        (
        f"<div style=\"padding-left: 2em; color: {VFUNC_COLOR};\">\n"\
        "count:\n"\
        "</div>\n"\
        "<div style=\"padding-left: 4em;\">\n"\
        f"{self.count}.\n"\
        "</div>\n"\
        if self.count is not None
        else ''
        )\
        +\
        (
        f"<div style=\"padding-left: 2em; color: {VFUNC_COLOR};\">\n"\
        "calculate_offsets:\n"\
        "</div>\n"\
        "<div style=\"padding-left: 4em;\">\n"\
        f"{self.offset_calc}.\n"\
        "</div>\n"\
        if self.offset_calc is not None
        else ''
        )


class PrimitiveOp:
    def __init__(self, name, typestring, size):
        self.name       = name
        self.typestring = typestring
        self.size       = size
    
    def to_string(self):
        return GenericOp(
            self.name, 
            "value", 
            f"Operates on {self.typestring} with context-sensitive endianness", 
            f"Returns {self.typestring} unpacked from the stream", 
            f"Packs <code>value</code> to {self.size} byte{'s' if self.size != 1 else ''} and writes it to the stream. Returns <code>value</code>",
            f"Increments the stream offset by {self.size}. Returns <code>value</code>"
        ).to_string()\
        +\
        "<div style=\"padding-top: 1em\"></div>\n"\
        "<div style=\"padding-left: 2em;\">\n"\
        "Variants:\n"\
        "</div>\n"\
        "\n"\
        "<div style=\"padding-left: 4em;\">\n"\
        f"<code style=\"color: {LISTING_COLOR};\">{self.name + '_le'}(value)</code>\n"\
        "\n"\
        "Forced little-endian mode.\n"\
        "</div>\n"\
        "\n"\
        "<div style=\"padding-left: 4em;\">\n"\
        f"<code style=\"color: {LISTING_COLOR};\">{self.name + '_be'}(value)</code>\n"\
        "\n"\
        "Forced big-endian mode.\n"\
        "</div>\n"\
        "\n"\
        "<div style=\"padding-left: 4em;\">\n"\
        f"<code style=\"color: {LISTING_COLOR};\">{self.name + '_e'}(value, endianness)</code>\n"\
        "\n"\
        "Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.\n"\
        "</div>\n"\

class PrimitiveArrayOp:
    def __init__(self, name, typestring, size):
        self.name       = name
        self.typestring = typestring
        self.size       = size
    
    def to_string(self):
        return GenericOp(
            self.name, 
            "value, shape", 
            f"Operates on an array of {self.typestring} with context-sensitive endianness", 
            f"Returns an array of {self.typestring} unpacked from the stream, row-major reshaped to the dimensions given by <code>shape</code>", 
            "Packs <code>value</code> in row-major order and writes it to the stream. Returns <code>value</code>",
            "Increments the stream offset by the binary size of <code>value</code>. Returns <code>value</code>"
        ).to_string()\
        +\
        "<div style=\"padding-top: 1em\"></div>\n"\
        "<div style=\"padding-left: 2em;\">\n"\
        "Variants:\n"\
        "</div>\n"\
        "\n"\
        "<div style=\"padding-left: 4em;\">\n"\
        f"<code style=\"color: {LISTING_COLOR};\">{self.name + '_le'}(value, shape)</code>\n"\
        "\n"\
        "Forced little-endian mode.\n"\
        "</div>\n"\
        "\n"\
        "<div style=\"padding-left: 4em;\">\n"\
        f"<code style=\"color: {LISTING_COLOR};\">{self.name + '_be'}(value, shape)</code>\n"\
        "\n"\
        "Forced big-endian mode.\n"\
        "</div>\n"\
        "\n"\
        "<div style=\"padding-left: 4em;\">\n"\
        f"<code style=\"color: {LISTING_COLOR};\">{self.name + '_e'}(value, shape, endianness)</code>\n"\
        "\n"\
        "Runtime endianness. Pass <code>'<'</code> or <code>'>'</code> for little- or big-endianness respectively.\n"\
        "</div>\n"\




class GenericListing:
    def __init__(self, name, sig, summary,):
        self.name        = name
        self.sig         = sig
        self.summary     = summary
    
    def to_string(self):
        return f"<a name=\"{self.name}\"></a>\n"\
        f"<code style=\"display: block; color: {LISTING_COLOR};\">\n"\
        f"<span>{self.name}({self.sig}): <a href=\"#{self.name}\">#</a>"\
        "</code>\n"\
        "\n"\
        "<div style=\"padding-left: 2em;\">\n"\
        f"{self.summary}.\n"\
        "</div>"

class ParserListing:
    def __init__(self, name, summary, rw_method, aliases, extra_methods):
        self.name          = name
        self.summary       = summary
        self.rw_method     = rw_method
        self.aliases       = aliases
        self.extra_methods = extra_methods
    
    def to_string(self):
        return f"<a name=\"{self.name}\"></a>\n"\
        f"<code style=\"display: block; color: {LISTING_COLOR};\">\n"\
        f"<span>{self.name} <a href=\"#{self.name}\">#</a>"\
        "</code>\n"\
        "\n"\
        "<div style=\"padding-left: 2em;\">\n"\
        f"{self.summary}.\n"\
        "</div>"\
        f"<span style=\"padding-left: 2em; color: {VFUNC_COLOR};\">\n"\
        "Descriptor Method:"\
        "</span> "\
        f"<span>{self.rw_method}</span>"\
        + ("<div style=\"padding-left: 2em;\">\n"\
           "Operator Aliases:\n"\
           "</div>\n"\
           + "\n".join(
               f"<span style=\"padding-left: 4em; color: {VFUNC_COLOR};\">\n"\
               f"{f1}"\
               "</span>"\
               "<span>"\
               f" -> "\
               "</span>"
               f"<span style=\"color: {VFUNC_COLOR};\">"\
               f"{f2}"\
               "</span>\n"
                f""
                for f1, f2 in self.aliases
            )
            if len(self.aliases)
            else ""
        )\
        + ("<div style=\"padding-left: 2em;\">\n"\
           "Additional Functions:\n"\
           "</div>\n"\
           + "\n".join(
               f"<div style=\"padding-left: 4em; color: {VFUNC_COLOR};\">\n"\
               f"{func_name}({func_sig}):\n"\
               "</div>\n"\
               "<div style=\"padding-left: 6em;\">\n"\
               f"{func_summary}.\n"\
               "</div>\n"
                f""
                for func_name, func_sig, func_summary in self.extra_methods
            )
            if len(self.extra_methods)
            else ""
        )
        
class ClassListing:
    def __init__(self, name, summary, funcs):
        self.name    = name
        self.summary = summary
        self.funcs   = funcs
    
    def to_string(self):
        return f"<a name=\"{self.name}\"></a>\n"\
        f"<code style=\"display: block; color: {LISTING_COLOR};\">\n"\
        f"<span>{self.name} <a href=\"#{self.name}\">#</a>"\
        "</code>\n"\
        "\n"\
        "<div style=\"padding-left: 2em;\">\n"\
        f"{self.summary}.\n"\
        "</div>"\
        +\
        "<div style=\"padding-top: 1em\"></div>\n"\
        "<div style=\"padding-left: 2em;\">\n"\
        "Functions:\n"\
        "</div>\n"\
        "\n"\
        + "\n".join(
            f"<div style=\"padding-left: 4em; color: {VFUNC_COLOR};\">\n"\
            f"{func_name}({func_sig}):\n"\
            "</div>\n"\
            "<div style=\"padding-left: 6em;\">\n"\
            f"{func_summary}.\n"\
            "</div>\n"\
            for func_name, func_sig, func_summary in self.funcs
        )

class TraitListing:
    def __init__(self, name, sig, summary, funcs):
        self.name    = name
        self.sig     = sig
        self.summary = summary
        self.funcs   = funcs
    
    def to_string(self):
        return GenericListing(
            self.name, 
            self.sig, 
            self.summary
        ).to_string()\
        +\
        "<div style=\"padding-top: 1em\"></div>\n"\
        "<div style=\"padding-left: 2em;\">\n"\
        "Functions:\n"\
        "</div>\n"\
        "\n"\
        + "\n".join(
            f"<div style=\"padding-left: 4em; color: {VFUNC_COLOR};\">\n"\
            f"{func_name}({func_sig}):\n"\
            "</div>\n"\
            "<div style=\"padding-left: 6em;\">\n"\
            f"{func_summary}.\n"\
            "</div>\n"\
            for func_name, func_sig, func_summary in self.funcs
        )


primitive_ops = [
    PrimitiveOp("rw_int8", "a signed 8-bit integer", 1),
    PrimitiveOp("rw_int16", "a signed 16-bit integer", 2),
    PrimitiveOp("rw_int32", "a signed 32-bit integer", 4),
    PrimitiveOp("rw_int64", "a signed 64-bit integer", 8),
    PrimitiveOp("rw_uint8", "an unsigned 8-bit integer", 1),
    PrimitiveOp("rw_uint16", "an unsigned 16-bit integer", 2),
    PrimitiveOp("rw_uint32", "an unsigned 32-bit integer", 4),
    PrimitiveOp("rw_uint64", "an unsigned 64-bit integer", 8),
    PrimitiveOp("rw_float16", "an IEEE 16-bit float", 2),
    PrimitiveOp("rw_float32", "an IEEE 32-bit float", 4),
    PrimitiveOp("rw_float64", "an IEEE 64-bit float", 8),
]


primitive_array_ops = [
    PrimitiveArrayOp("rw_int8s",  "signed 8-bit integers", 1),
    PrimitiveArrayOp("rw_int16s", "signed 16-bit integers", 2),
    PrimitiveArrayOp("rw_int32s", "signed 32-bit integers", 4),
    PrimitiveArrayOp("rw_int64s", "signed 64-bit integers", 8),
    PrimitiveArrayOp("rw_uint8s",  "unsigned 8-bit integers", 1),
    PrimitiveArrayOp("rw_uint16s", "unsigned 16-bit integers", 2),
    PrimitiveArrayOp("rw_uint32s", "unsigned 32-bit integers", 4),
    PrimitiveArrayOp("rw_uint64s", "unsigned 64-bit integers", 8),
    PrimitiveArrayOp("rw_float16s", "IEEE 16-bit floats", 2),
    PrimitiveArrayOp("rw_float32s", "IEEE 32-bit floats", 4),
    PrimitiveArrayOp("rw_float64s", "IEEE 64-bit floats", 8),
]

bstring_op = GenericOp("rw_bytestring", 
                       "value, length", 
                       "Operates on a fixed-size bytestring", 
                       "Reads <code>length</code> chars from the stream. Returns a <code>bytes</code> object", 
                       "Writes <code>value</code> to the stream. Expects <code>value</code> to be a <code>bytes</code>-like object. Returns <code>value</code>", 
                       "Increments the stream offset by the length of <code>value</code>. Expects <code>value</code> to be a <code>bytes</code> object. Returns <code>value</code>")

bstrings_op = GenericOp("rw_bytestrings", 
                       "value, lengths", 
                       "Operates on a list of fixed-size bytestrings", 
                       "Reads <code>length</code> chars from the stream. Returns a <code>List[bytes]</code> object", 
                       "Writes each element in <code>value</code> to the stream. Expects <code>value</code> to be an iterable of <code>bytes</code>-like objects. Returns <code>value</code>", 
                       "Increments the stream offset by the sum of all lengths in <code>value</code>. Expects <code>value</code> to be an iterable of <code>bytes</code>-like objects. Returns <code>value</code>")

cbstring_op = GenericOp("rw_cbytestring", 
                       "value[, chunksize=0x40, terminator=b'\\x00']", 
                       "Operates on a terminated bytestring", 
                       "Reads chars from the stream in blocks of <code>chunksize</code> until the <code>terminator</code> pattern is identified in one of those blocks. Returns a <code>bytes</code> object without the terminator", 
                       "Writes <code>value</code> to the stream, and then writes the <code>terminator</code>. Expects <code>value</code> to be a <code>bytes</code>-like object. Returns <code>value</code>", 
                       "Increments the stream offset by the length of <code>value</code> plus the length of the <code>terminator</code>. Expects <code>value</code> to be an iterable of <code>bytes</code>-like objects. Returns <code>value</code>")

cbstrings_op = GenericOp("rw_cbytestrings", 
                       "value, count[, chunksize=0x40, terminator=b'\\x00']", 
                       "Operates on a list of terminated bytestrings", 
                       "Reads chars from the stream in blocks of <code>chunksize</code> until the <code>terminator</code> pattern is identified in one of those blocks, <code>count</code> times. Returns a <code>List[bytes]</code> object", 
                       "Writes each element (followed by the <code>terminator</code>) in <code>value</code> to the stream. Expects <code>value</code> to be an iterable of <code>bytes</code>-like objects. Returns <code>value</code>", 
                       "Increments the stream offset by the sum of all lengths in <code>value</code> (plus the requisite <code>terminator</code> lengths). Expects <code>value</code> to be an iterable of <code>bytes</code>-like objects. Returns <code>value</code>")

descriptor_op = GenericOp("rw_descriptor",
    "descriptor, \*args, \*\*kwargs",
    "Looks for and executes the descriptor method required by the parser",
    "Invokes the 'deserialize' method of the descriptor",
    "Invokes the 'serialize' method of the descriptor",
    "Invokes the 'count' method of the descriptor",
)

object_op = GenericOp("rw_obj",
    "value, \*args, \*\*kwargs",
    "Executes the <code>exbip_rw</code> function on <code>value</code>",
    "Calls <code>exbip_rw</code> on <code>value</code>",
    "Calls <code>exbip_rw</code> on <code>value</code>",
    "Calls <code>exbip_rw</code> on <code>value</code>",
)

dynamic_object_op = GenericOp("rw_dynamic_obj",
    "value, constructor, \*args, \*\*kwargs",
    "Executes the <code>exbip_rw</code> function on <code>value</code> if not deserializing, otherwise constructs it first",
    "Calls <code>constructor</code> to build a new object, then calls <code>exbip_rw</code> on it",
    "Calls <code>exbip_rw</code> on <code>value</code>",
    "Calls <code>exbip_rw</code> on <code>value</code>",
)

dynamic_objects_op = GenericOp("rw_dynamic_objs",
    "values, constructor, count, \*args, \*\*kwargs",
    "Executes the <code>exbip_rw</code> function on <code>value</code> if not deserializing, otherwise constructs to object array first from a count",
    "Calls <code>constructor</code> to build a new object, then calls <code>exbip_rw</code> on it, <code>count</code> times",
    "Calls <code>exbip_rw</code> on each element in <code>values</code>",
    "Calls <code>exbip_rw</code> on each element in <code>values</code>",
)

dynamic_objects_while_op = GenericOp("rw_dynamic_objs_while",
    "values, constructor, condition, \*args, \*\*kwargs",
    "Executes the <code>exbip_rw</code> function on <code>value</code> if not deserializing, otherwise constructs to object array first from a boolean condition",
    "Calls <code>constructor</code> to build a new object, then calls <code>exbip_rw</code> on it, until calling <code>condition</code> returns False. <code>condition</code> must be a function (or functor) that takes the parser as its only argument",
    "Calls <code>exbip_rw</code> on each element in <code>values</code>",
    "Calls <code>exbip_rw</code> on each element in <code>values</code>",
)

iterator_for_op = GenericOp("array_iterator",
    "array, constructor, count",
    "Returns an iterable object that will construct <code>count</code> array elements if deserializing, and iterate through an array if not. Example:\n"\
    "</div>\n\n"\
    "```python\n"\
    "for i, obj in enumerate(rw.array_iterator(arr, MyObject, my_count)):\n"\
    "    rw.check_stream_offset(obj_offsets[i], \"Object {i}\", HEX32_FORMATTER)\n"\
    "    rw.rw_obj(obj)\n"\
    "```\n"\
    "\n"\
    "<div style=\"padding-left: 2em\">This can be used for more advanced looping behavior than <i>e.g.</i> <code>rw_dynamic_objs</code>",
    "Returns an iterable object that clears the given array, and then appends a newly-constructed object to the array at the start of each iteration",
    "Returns an iterable object that iterates through the elements of <code>array</code>",
    "Returns an iterable object that iterates through the elements of <code>array</code>",
)

iterator_while_op = GenericOp("array_while_iterator",
    "array, constructor, stop_condition",
    "Returns an iterable object that will construct array elements until <code>condition</code> is False if deserializing, and iterate through an array if not. Example:\n"\
    "</div>\n\n"\
    "```python\n"\
    "class Cond:\n"\
    "    def __init__(self, offset):\n"\
    "        self.offset = offset\n"\
    "\n"\
    "    def __call__(self, rw):\n"\
    "        return rw.tell() < self.offset\n"\
    "\n"\
    "offset_list = []\n"\
    "for obj in rw.array_while_iterator(arr, MyObject, Cond(offset)):\n"\
    "    offset_list.append(rw.tell())\n"\
    "    rw.rw_obj(obj)\n"\
    "```\n"\
    "\n"\
    "<div style=\"padding-left: 2em\">This can be used for more advanced looping behavior than <i>e.g.</i> <code>rw_dynamic_objs_while</code>",
    "Returns an iterable object that clears the given array, and then appends a newly-constructed object to the array at the start of each iteration",
    "Returns an iterable object that iterates through the elements of <code>array</code>",
    "Returns an iterable object that iterates through the elements of <code>array</code>",
)
    
section_exists_op = GenericOp("section_exists",
    "offset, count",
    "Returns a bool that states whether a data section defined by a non-zero offset and/or count exists or not",
    "Returns True if <code>offset</code> is greater than 0",
    "Returns True if <code>count</code> is greater than 0",
    "Returns True if <code>count</code> is greater than 0",
)
    
stream_eof_op = GenericOp("assert_eof",
    "",
    "Raises an exception if the stream pointer is not at the end of the stream, if the parsing mode defines an end-of-stream",
    "Raises a <code>NotAtEOFError</code> if the stream pointer is not at the end of the stream",
    "Does nothing",
    "Does nothing",
)
    
align_op = GenericOp("align",
    "offset, alignment(, pad_value=b'\\x00'",
    "Rounds up <code>offset</code> to the next multiple of <code>alignment</code>, and performs an operation on the section of the stream corresponding to the skipped bytes",
    "Reads enough bytes to perform the alignment, and validates that they are an array of <code>pad_value</code>s. Raises <code>ValueError</code> if the number of bytes required for the alignment is not divisible by the length of <code>pad_value</code>",
    "Writes enough <code>pad_value</code>s to the stream to perform the alignment. Raises <code>ValueError</code> if the number of bytes required for the alignment is not divisible by the length of <code>pad_value</code>",
    "Advances the stream offset to the next multiple of <code>alignment</code>. Raises <code>ValueError</code> if the number of bytes required for the alignment is not divisible by the length of <code>pad_value</code>",
) 

fill_op = GenericOp("fill",
    "offset, alignment(, fill_value=b'\\x00'",
    "Rounds up <code>offset</code> to the next multiple of <code>alignment</code>, and performs an operation on the section of the stream corresponding to the skipped bytes",
    "Reads enough bytes to perform the alignment. Does not perform any validation",
    "Writes enough <code>pad_value</code>s to the stream to perform the alignment. Raises <code>ValueError</code> if the number of bytes required for the alignment is not divisible by the length of <code>pad_value</code>",
    "Advances the stream offset to the next multiple of <code>alignment</code>. Raises <code>ValueError</code> if the number of bytes required for the alignment is not divisible by the length of <code>pad_value</code>",
)

enforce_offset_op = GenericOp("verify_stream_offset",
    "offset, message[, formatter=lambda x: x, notifier=None]",
    "Seeks to <code>offset</code>, throws an error if the stream offset is not at <code>offset</code>, or calls <code>notifier</code> with the current stream offset",
    "Seeks to <code>offset</code>",
    "Throws a <code>UnexpectedOffsetError</code> if the stream offset is not at <code>offset</code>",
    "Does nothing",
    "Calls <code>notifier.notify()</code> if <code>notifier</code> is not None. Commonly, <code>notifier</code> is an <code>OffsetMarker</code> object"
)


navigate_offset_op = GenericOp("navigate_stream_offset",
    "offset, message[, formatter=lambda x: x, notifier=None]",
    "Seeks to <code>offset</code>, throws an error if the stream offset is not at <code>offset</code>, or calls <code>notifier</code> with the current stream offset",
    "Seeks to <code>offset</code>",
    "Does nothing",
    "Does nothing",
    "Calls <code>notifier.notify()</code> if <code>notifier</code> is not None. Commonly, <code>notifier</code> is an <code>OffsetMarker</code> object"
)

verify_offset_op = GenericOp("verify_stream_offset",
    "offset, message[, formatter=lambda x: x, notifier=None]",
    "Throws an error if the stream offset is not at <code>offset</code>, or calls <code>notifier</code> with the current stream offset",
    "Throws a <code>UnexpectedOffsetError</code> if the stream offset is not at <code>offset</code>",
    "Throws a <code>UnexpectedOffsetError</code> if the stream offset is not at <code>offset</code>",
    "Does nothing",
    "Calls <code>notifier.notify()</code> if <code>notifier</code> is not None. Commonly, <code>notifier</code> is an <code>OffsetMarker</code> object"
)

check_as_verify_op = GenericOp("check_stream_offset",
    "offset, message[, formatter=lambda x: x, notifier=None]",
    "An alias for <code>verify_stream_offset</code>. Used by all standard parsers except <code>NonContiguousReader</code>",
    None, None, None
)

check_as_enforce_op = GenericOp("check_stream_offset",
    "offset, message[, formatter=lambda x: x, notifier=None]",
    "An alias for <code>enforce_stream_offset</code>. Used by <code>NonContiguousReader</code>",
    None, None, None
)

padding_op = GenericOp("rw_padding",
    "count[, pad_value=b'\\x00', validate=True]",
    "Operates on an anonymous bytestring of length <code>count</code>",
    "Reads <code>count*len(pad_value)</code> bytes from the stream. If <code>validate</code> is True, the bytes are checked to ensure they are an array of <code>pad_value</code>. If they are not, an <code>UnexpectedPaddingError</code> is raised",
    "Writes <code>count</code> <code>pad_value</code>s to the stream",
    "Advances the stream by <code>count*len(pad_value)</code>",
)


dispatch_marker_op = GenericOp("dispatch_marker",
    "marker",
    "Operates on an object with a single-argument <code>notify</code> method, expected to be an <code>OffsetMarker</code> object",
    "Does nothing",
    "Does nothing",
    "Does nothing",
    "Calls <code>marker.notify()</code>"
)

def wbreak(FILE):
    FILE.write("\n\n\n<div><br></div>\n\n\n")

with open("03-standardlibrary.md", 'w') as FILE:
    FILE.write(
        "# Standard Library\n")
    FILE.write("Namespace: `exbip`\n")
    
    FILE.write(
        "\n\n\n## Parsers\n"
        "\n")
    FILE.write(ParserListing("Reader", "Inherits from <code>ReaderBase</code>. Implements the standard library descriptors. A parser for deserializing bytes to Python objects. Designed for contiguous parsing", "<code>deserialize</code>", 
                             [("check_stream_offset", "verify_stream_offset")],
                             []).to_string())
    wbreak(FILE)
    FILE.write(ParserListing("NonContiguousReader", "Inherits from <code>ReaderBase</code>. Implements the standard library descriptors. A parser for deserializing bytes to Python objects. Designed for non-contiguous parsing", "<code>deserialize</code>", 
                             [("check_stream_offset", "enforce_stream_offset")],
                             []).to_string())
    wbreak(FILE)
    FILE.write(ParserListing("Validator", "Inherits from <code>ValidatorBase</code>. Implements the standard library descriptors. A parser to verify whether two bytestreams deserialize to identical Python objects, and if not, to raise an error that originates at the first pair of read calls that deserialize to different values. Designed for contiguous parsing", "<code>deserialize</code>", 
                             [("check_stream_offset", "verify_stream_offset")],
                             []).to_string())
    wbreak(FILE)
    FILE.write(ParserListing("Writer", "Inherits from <code>WriterBase</code>. Implements the standard library descriptors. A parser for serializing Python objects to bytes. Designed for contiguous parsing", "<code>serialize</code>", 
                             [("check_stream_offset", "verify_stream_offset")],
                             []).to_string())
    wbreak(FILE)
    FILE.write(ParserListing("Counter", "Inherits from <code>CounterBase</code>. Implements the standard library descriptors. A parser for counting how many bytes a stream pointer will advance for each operator call. Designed for contiguous parsing", "<code>count</code>", 
                             [("check_stream_offset", "verify_stream_offset")],
                             []).to_string())
    wbreak(FILE)
    FILE.write(ParserListing("OffsetCalculator", "Inherits from <code>OffsetCalculatorBase</code>. Implements the standard library descriptors. A parser for counting how many bytes a stream pointer will advance for each operator call, and using this to calculate the value of stream-offset variables within a structure", "<code>calculate_offsets</code> if it exists. Else, <code>count</code>", 
                             [("check_stream_offset", "verify_stream_offset")],
                             []).to_string())
    
    FILE.write(
        "\n\n\n## Traits\n"\
        "\n"\
        + "\n".join([l.to_string() for l in [
            TraitListing("ReadableTrait", "Reader", "A trait that adds deserialization methods to a structure",
                         (
                             ("read", "filepath, \*args, \*\*kwargs", "Passes <code>filepath</code> to the <code>FileIO()</code> method of <code>Reader</code>"),
                             ("frombytes", "byte_data, \*args, \*\*kwargs", "Passes <code>byte_data</code> to the <code>BytestreamIO()</code> method of <code>Reader</code>")
                        )),
            TraitListing("WriteableTrait", "Writer", "A trait that adds serialization methods to a structure",
                         (
                             ("write", "filepath, \*args, \*\*kwargs", "Passes <code>filepath</code> to the <code>FileIO()</code> method of <code>Writer</code>"),
                             ("tobytes", "\*args, \*\*kwargs", "Returns the bytes written to the stream initialized by the <code>BytestreamIO()</code> method of <code>Writer</code>")
                        )),
            TraitListing("ValidatableTrait", "Validator", "A trait that adds validation methods to a structure",
                         (
                             ("validate_file_against_file",   "primary_filepath, reference_filepath, \*args, \*\*kwargs", "Validates the data in <code>primary_filepath</code> against the data in <code>reference_filepath</code>"),
                             ("validate_file_against_bytes",  "primary_filepath, reference_bytes,    \*args, \*\*kwargs", "Validates the data in <code>primary_filepath</code> against the bytes in <code>reference_bytes</code>"),
                             ("validate_bytes_against_file",  "primary_bytes,    reference_filepath, \*args, \*\*kwargs", "Validates the bytes in <code>primary_bytes</code> against the data in <code>reference_filepath</code>"),
                             ("validate_bytes_against_bytes", "primary_bytes,    reference_bytes,    \*args, \*\*kwargs", "Validates the bytes in <code>primary_bytes</code> against the bytes in <code>reference_bytes</code>"),
                        )),
            TraitListing("OffsetsCalculableTrait", "OffsetCalculator", "A trait that adds offset calculation methods to a structure",
                         (
                             ("calculate_offsets", "obj, \*args, \*\*kwargs", "Calls <code>OffsetCalculator.rw_obj(obj, \*args, \*\*kwargs)</code> on an instance of <code>OffsetCalculator</code>. This is intended to be used to automatically calculate the values of file offsets"),
                        )),
        ]]
    ))
    
    FILE.write("\n\n\n## Operations\n")
    
    FILE.write("\n\n\n### Primitives\n")
    FILE.write("\n\n\n<div><br></div>\n\n\n".join([o.to_string() for o in primitive_ops]))
    
    FILE.write("\n\n\n### Primitive Arrays\n")
    FILE.write("\n\n\n<div><br></div>\n\n\n".join([o.to_string() for o in primitive_array_ops]))
    
    FILE.write("\n\n\n### Strings\n")
    FILE.write(bstring_op.to_string())
    wbreak(FILE)
    FILE.write(bstrings_op.to_string())
    wbreak(FILE)
    FILE.write(cbstring_op.to_string())
    wbreak(FILE)
    FILE.write(cbstrings_op.to_string())
    
    FILE.write("\n\n\n### Descriptors\n")
    FILE.write(descriptor_op.to_string())
    
    FILE.write("\n\n\n### Objects\n")
    FILE.write(object_op.to_string())
    wbreak(FILE)
    FILE.write(dynamic_object_op.to_string())
    wbreak(FILE)
    FILE.write(dynamic_objects_op.to_string())
    wbreak(FILE)
    FILE.write(dynamic_objects_while_op.to_string())
    
    FILE.write("\n\n\n### Iterators\n")
    FILE.write(iterator_for_op.to_string())
    wbreak(FILE)
    FILE.write(iterator_while_op.to_string())
    
    FILE.write("\n\n\n### Sections\n")
    FILE.write(section_exists_op.to_string())
    
    FILE.write("\n\n\n### Stream End-of-file\n")
    FILE.write(stream_eof_op.to_string())
    
    FILE.write("\n\n\n### Stream Alignment\n")
    FILE.write(align_op.to_string())
    wbreak(FILE)
    FILE.write(fill_op.to_string())
    
    FILE.write("\n\n\n### Stream Offsets\n")
    FILE.write(enforce_offset_op.to_string())
    wbreak(FILE)
    FILE.write(navigate_offset_op.to_string())
    wbreak(FILE)
    FILE.write(verify_offset_op.to_string())
    wbreak(FILE)
    FILE.write(check_as_verify_op.to_string())
    wbreak(FILE)
    FILE.write(check_as_enforce_op.to_string())
    
    FILE.write("\n\n\n### Stream Padding\n")
    FILE.write(padding_op.to_string())
    
    FILE.write("\n\n\n### Offset Markers\n")
    FILE.write(dispatch_marker_op.to_string())
    
    FILE.write(
        "\n"\
        "## Formatters\n"\
        "\n"\
        + "\n".join(l.to_string() for l in [
            GenericListing("safe_formatter", "formatter", "Returns a <code>safe_formatter</code> object that calls <code>formatter</code>, which is a format method like <i>e.g.</i> <code>'0b{0:0>8b}'.format</code>, and returns the call return value if it does not throw an exception. On throwing a <code>ValueError</code> or <code>TypeError</code>, the original value is returned. Other exceptions are uncaught"),
            GenericListing("bin8_formatter", "value", "A <code>safe_formatter</code> that formats <code>value</code> as an 8-bit binary string"),
            GenericListing("bin16_formatter", "value", "A <code>safe_formatter</code> that formats <code>value</code> as a 16-bit binary string"),
            GenericListing("bin32_formatter", "value", "A <code>safe_formatter</code> that formats <code>value</code> as a 32-bit binary string"),
            GenericListing("bin64_formatter", "value", "A <code>safe_formatter</code> that formats <code>value</code> as a 64-bit binary string"),
            GenericListing("hex8_formatter", "value", "A <code>safe_formatter</code> that formats <code>value</code> as an 8-bit lower-case hex string"),
            GenericListing("hex16_formatter", "value", "A <code>safe_formatter</code> that formats <code>value</code> as a 16-bit lower-case hex string"),
            GenericListing("hex32_formatter", "value", "A <code>safe_formatter</code> that formats <code>value</code> as a 32-bit lower-case hex string"),
            GenericListing("hex64_formatter", "value", "A <code>safe_formatter</code> that formats <code>value</code> as a 64-bit lower-case hex string"),
            GenericListing("HEX8_formatter", "value", "A <code>safe_formatter</code> that formats <code>value</code> as an 8-bit upper-case hex string"),
            GenericListing("HEX16_formatter", "value", "A <code>safe_formatter</code> that formats <code>value</code> as a 16-bit upper-case hex string"),
            GenericListing("HEX32_formatter", "value", "A <code>safe_formatter</code> that formats <code>value</code> as a 32-bit upper-case hex string"),
            GenericListing("HEX64_formatter", "value", "A <code>safe_formatter</code> that formats <code>value</code> as a 64-bit upper-case hex string"),
        ])
    )
        
    FILE.write("\n\n\n## Structures")
    FILE.write(ClassListing("OffsetMarker", "A class that holds a list of single-argument callbacks. When <code>notify</code> is called, the offset passed to <code>notify</code> is used to call each of these callbacks, each of which is intended to give a particular variable the value of that offset",
        (
            ("clear", "", "Clears the subscriber list"),
            ("subscribe", "obj, attr", "Adds a callback <code>lambda offset: setattr(obj, attr, offset)</code> to the <code>OffsetMarker</code>'s callbacks list. Returns <code>self</code> so that multiple subscriptions can be chained with the constructor"),
            ("subscribe_callback", "callback", "Adds the single-argument function <code>callback</code> to the <code>OffsetMarker</code>'s callbacks list. Returns <code>self</code> so that multiple subscriptions can be chained with the constructor"),
            ("notify", "offset", "Iterates through the list of subscribers and calls each one with <code>offset</code>"),
        )
    ).to_string())
