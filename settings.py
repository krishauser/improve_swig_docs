#all of the classes defined in the package that you'd like to cross-reference
classes = {'MyClass1',
           'MyClass2' 
}

#default prefix for class cross-references
default_class_prefix = 'my_module'

#other prefixes for class cross-references
class_prefix = {
    'MyClass2':'my_module.sub_module'
}

basic_types = {'int','float','str','bytes','bool'}

#location to inject typing string. Usually don't need to change this
typing_inject_location = 'import __builtin__'
typing_header = """
from typing import List,Tuple,Sequence,Iterator,Dict
"""

#conversions from SWIG docstrings to RST docstrings
to_python_types = {
    'char *':'str',
    'char':'str',
    'std::string':'str',
    'double':'float',
    'PyObject': "object",
    'PyObject *': "object"
}

to_python_type_hints = {
    'void' : 'None',
    'bool' : 'bool',
    'int' : 'int',
    'float' : 'float',
    'double' : 'float',
    'size_t' : 'int',
    'ptrdiff_t' : 'int',
    'SwigPyIterator': 'Iterator',
    'swig::SwigPyIterator': 'Iterator',
    'swig::SwigPyIterator *': 'Iterator',
    "std::vector< int >::value_type" : "int",
    "std::vector< float >::value_type" : "float",
    "std::vector< double >::value_type" : "float",
    "std::vector< std::string >::value_type" : "str",
    "std::map< std::string,int >::key_type" : 'str',
    "std::map< std::string,int >::mapped_type" : 'int',
    "std::map< std::string,float >::key_type" : 'str',
    "std::map< std::string,float >::mapped_type" : 'float',
    "std::map< std::string,double >::key_type" : 'str',
    "std::map< std::string,double >::mapped_type" : 'double',
    "std::map< std::string,std::string >::key_type" : 'str',
    "std::map< std::string,std::string >::mapped_type" : 'str',
}

"""SWIG's bindings of STL has a bunch of garbage"""
stl_to_python_type_hints = {
    "::size_type" : 'int',
    "::difference_type" : 'int',
    "::iterator" : "Iterator",
    "::reverse_iterator" : "Iterator",
    "::allocator_type" : None,
}

to_python_defaults = {'NULL':"None"}
