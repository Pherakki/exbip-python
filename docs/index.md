# Index

## What is exbip-python?

`exbip-python` is a pure Python library of **EX**tensible **BI**nary **P**arsers that aims to make data serialization fast and easy. The main features of `exbip` are:

- Serialization is (currently, see Future Development) performed verbosely with a single function that acts as a "schema", capable of handling deserialization, serialization, automatic data offset calculations, data validation, or other user-defined tasks, depending on an external object used to parse the data structure.
- It provides a simple interface to extend the library functionality with "descriptors" for binary data patterns not covered in the `exbip-python` "standard library".

In addition, the library has been written with the goal of minimizing abstraction overhead in CPython. Some abstraction overhead is incurred by necessity in CPython, which has been partially mitigated by inlining function calls (by hand or by runtime monkey-patching), and optimizing out unnecessary attribute accesses.

Further optimization and benchmarking work is always highly welcome.

Note that `exbip` is a work-in-progress. There are likely areas that the API either does not fit as well as it could do, or is missing functionality that is useful for a large number of workflows. Issues to discuss this (followed by pull requests to fix them) are very much appecriated.
However, `exbip` has been used successfully in several projects before its standalone release and is capable of building useable and validatable serialization logic.

## Documentation Contents

In the documentation you will find:

1. [Getting Started](02-gettingstarted.md): A gentle introduction to using `exbip` which covers the major features.

2. [Standard Library](03-standardlibrary.md): An exhaustive list of every function and class in the exbip standard library that is exposed to the user.

3. [Framework](04-framework.md): An exhaustive list of the framework functions and classes exposed to the user, which are used for creating extensions for `exbip`.

4. [Future Development](05-futuredevelopment.md): A list of topics under consideration for future development of the library.
