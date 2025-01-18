
LISTING_COLOR = "#FFA000"
VFUNC_COLOR   = "#2094F3"


def wbreak(FILE):
    FILE.write("\n\n\n<div><br></div>\n\n\n")


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

class BaseParserListing:
    def __init__(self, name, summary, rw_method, extra_methods):
        self.name          = name
        self.summary       = summary
        self.rw_method     = rw_method
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
        

with open("04-framework.md", 'w') as FILE:
    FILE.write("# Framework")
    FILE.write("\nNamespace: `exbip.framework`")
    FILE.write("\n\n\n## Descriptors")
    FILE.write(ClassListing("EndianPairDescriptor",
                            "Instantiate this class to create an endian-aware descriptor",
                            (
                                ("__init__", 
                                 "name, little_endian, big_endian",
                                 "When installed on a parser, this will create an operation called <code>name</code> that is set to the operation with name <code>little_endian</code> in little-endian mode and with name <code>big_endian</code> when in big-endian mode"),
                            )
                ).to_string() + "\n"
    )
    
    FILE.write("\n\n\n## Parsers")
    
    FILE.write(BaseParserListing("IBinaryParser", "A base class for <code>exbip</code> parsers", "<i>undefined</i>", 
                             [
                                 ("_get_rw_method", "descriptor", "Pure virtual method. Must be implemented by an inheriting class. Intended to return a function on <code>descriptor</code> matching the theme of the parser"),
                                 ("global_seek", "position", "Pure virtual method. Must be implemented by an inheriting class. Intended to set the stream offset to the given offset"),
                                 ("global_tell", "", "Pure virtual method. Must be implemented by an inheriting class. Intended to return the stream offset"),
                                 ("[classmethod] extended_with", "descriptors, endian_inlined", "Returns a class derived from the current class that has the operators defined in <code>descriptors</code> defined on it, using the <code>rw_method</code> for that class. Also installs the endian-aware descriptors in <code>endian_inlined</code>"),
                                 ("execute_descriptor", "descriptor, \*args, \*\*kwargs", "Fetches the required method from <code>descriptor</code> for this parser and executes it"),
                                 ("__call__", "descriptor, \*args, \*\*kwargs", "Equal to <code>execute_descriptor</code>"),
                                 ("[staticmethod] bytes_to_alignment", "position, alignment", "Calculates how many bytes are required to round <code>position</code> up to the nearest multiple of <code>alignmente</code>"),
                                 ("is_unaligned", "alignment", "Returns True if the current stream position is not a multiple of <code>alignment</code>, else, False"),
                                 ("relative_global_seek", "offset, base_position", "Seeks to <code>offset + base_position</code> relative to the stream origin"),
                                 ("seek", "offset", "Seeks to <code>offset</code> relative to the context origin"),
                                 ("relative_seek", "offset, base_position", "Seeks to <code>offset + base_position</code> relative to the context origin"),
                                 ("relative_global_tell", "base_position", "Returns <code>global_tell() - base_position</code>"),
                                 ("tell", "", "Returns <code>global_tell()</code> relative to the context origin"),
                                 ("relative_tell", "base_position", "Returns <code>global_tell() - base_position</code> relative to the context origin"),
                                 ("local_to_global_offset", "offset", "Transforms <code>offset</code> from a local (context) offset to a global (stream) offset"),
                                 ("global_to_local_offset", "offset", "Transforms <code>offset</code> from a global (stream) offset to a local (context) offset"),
                                 ("current_origin", "", "Returns the current stream position corresponding to the context origin"),
                                 ("push_origin", "offset", "Sets <code>offset</code> as the current context origin"),
                                 ("pop_origin", "", "Restores the context origin to the previous context's origin"),
                                 ("new_origin", "", "Returns a context manager that will call <code>push_origin</code> when entered, and <code>pop_origin</code> when exited"),
                                 ("[property] endianness", "", "Returns the current context's endianness"),
                                 ("set_endianness", "endianness", "Sets the current context's endianness. Valid values are <code>'<'</code> and <code>'>'</code>"),
                                 ("as_littleendian", "", "Returns a context manager that sets the context endianness to little endian for the scope of the context"),
                                 ("as_bigendian", "", "Returns a context manager that sets the context endianness to big endian for the scope of the context"),
                                 ("as_endian", "endianness", "Returns a context manager that sets the context endianness to the provided endianness for the scope of the context. Valid values are <code>'<'</code>, <code>'>'</code>, <code>'little'</code>, and <code>'big'</code>"),
                                 ("assert_equal", "input_value, reference_value[, value_name=None, formatter=None]", "Throws an exception if <code>input_value</code> does not equal <code>reference_value</code>. The <code>name</code> of the value is included in the exception if it is not <code>None</code>, and <code>formatter</code> is used to format the values if it is not <code>None</code>")
                            ]).to_string())
    wbreak(FILE)
    
    FILE.write(BaseParserListing("ReaderBase", "Inherits from <code>IBinaryParser</code>\n. A base class for a parser that deserializes bytes to Python objects", "<code>deserialize</code>", 
                             [
                                 ("FileIO", "filepath", "Constructs the Reader with an <code>io.BufferedReader</code> stream context. Sets <code>read_bytes</code> to the <code>read</code> method of the stream"),
                                 ("BytestreamIO", "initializer", "Constructs the Reader with an <code>io.BytesIO</code> stream context. Sets <code>read_bytes</code> to the <code>read</code> method of the stream"),
                                 ("_default_read_bytes", "length", "The default function assigned to <code>read_bytes</code> when not in a stream context"),
                                 ("read_bytes", "length", "A label that which the bytes-reading method of the stream is intended to be monkey-patched onto to avoid an extra attribute lookup and provide a unified API over different streams, <i>i.e.</i> <code>rw.read_bytes</code> vs. <code>rw._bytestream.read</code>"),
                                 ("peek_bytestring", "length", "Reads up to <code>length</code> bytes from the stream without advancing the stream offset"),
                            ]).to_string())
    wbreak(FILE)
    FILE.write(BaseParserListing("ValidatorBase", "Inherits from <code>IBinaryParser</code>\n. A base class for a parser that verifies whether two bytestreams deserialize to identical Python objects, and if not, to raises an error that originates at the first pair of read calls that deserialize to different values", "<code>deserialize</code>", 
                             [
                                 ("PrimaryFileIO", "filepath", "Constructs the Validator's primary stream with an <code>io.BufferedReader</code> stream context"),
                                 ("PrimaryBytestreamIO", "initializer", "Constructs the Validator's primary stream with an <code>io.BytesIO</code> stream context"),
                                 ("ReferenceFileIO", "filepath", "Constructs the Validator's reference stream with an <code>io.BufferedReader</code> stream context"),
                                 ("ReferenceBytestreamIO", "initializer", "Constructs the Validator's reference stream with an <code>io.BytesIO</code> stream context"),
                                 ("_default_read_bytes", "length", "The default function assigned to <code>read_bytes</code> when not in a stream context"),
                                 ("read_bytes", "length", "A label that which the bytes-reading method of the stream is intended to be monkey-patched onto to avoid an extra attribute lookup and provide a unified API over different streams, <i>i.e.</i> <code>rw.read_bytes</code> vs. <code>rw._bytestream.read</code>"),
                                 ("peek_bytestring", "length", "Reads up to <code>length</code> bytes from the stream without advancing the stream offset"),
                            ]).to_string())
    wbreak(FILE)
    FILE.write(BaseParserListing("WriterBase", "Inherits from <code>IBinaryParser</code>\n. A base class for a parser that serializes Python objects to bytes", "<code>serialize</code>", 
                             [
                                 ("FileIO", "filepath", "Constructs the Writer with an <code>io.BufferedReader</code> stream context"),
                                 ("BytestreamIO", "initializer", "Constructs the Writer with an <code>io.BytesIO</code> stream context"),
                                 ("write_bytes", "length", "A label that which the bytes-reading method of the stream is intended to be monkey-patched onto to avoid an extra attribute lookup and provide a unified API over different streams, <i>i.e.</i> <code>rw.write_bytes</code> vs. <code>rw._bytestream.write</code>"),
                            ]).to_string())
    wbreak(FILE)
    FILE.write(BaseParserListing("CounterBase", "Inherits from <code>IBinaryParser</code>\n. A base class for a parser that counts how many bytes a stream pointer will advance for each operator call", "<code>count</code>", 
                             [
                                 ("advance_offset", "value", "Increments the stream offset by <code>value</code>")    
                             ]).to_string())
    wbreak(FILE)
    FILE.write(BaseParserListing("OffsetCalculatorBase", "Inherits from <code>CounterBase</code>\n. A base class for a parser that counts how many bytes a stream pointer will advance for each operator call, and using this calculates the value of stream-offset variables within a structure", "<code>calculate_offsets</code> if it exists. Else, <code>count</code>", 
                             [
                             ]).to_string())
    
    FILE.write("\n\n\n## Streams")
    FILE.write(
        ClassListing("ValidatorStream",
            "A stream used by ValidatorBase",
            (
                ("set_primary_stream", "stream", "Sets the primary stream of the ValidatorStream"),
                ("set_reference_stream", "stream", "Sets the reference stream of the ValidatorStream"),
                ("close", "", "Closes the primary and reference streams, if they are not <code>None</code>"),
                ("seek", "offset", "Seeks both the primary and reference streams to the given <code>offset</code>"),
                ("tell", "", "Returns the position of the primary stream, which should be synchronised with the reference stream"),
                ("read", "count", "Reads <code>count</code> from both streams and raises a <code>ValidationError</code> if they are not equal"),
                ("write", "data", "Raises <code>NotImplementedError</code>")
            )
        ).to_string()
    )
    