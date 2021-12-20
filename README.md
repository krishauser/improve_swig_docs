# Improve SWIG Docs
## Kris Hauser 

If you've ever used SWIG to auto-generate docstrings, you'll realize that the documentation is horrendous for readers of the target language. In particular, there's a lot of cruft around the function declarations, and SWIG type hints throw Sphinx, IDEs, and linters into a frenzy!

This script solves all of that, outputting nicely formatted docstrings that can be processed via Sphinx, read by VSCode, etc.

## Prerequisites

This package supports C/C++ extension module -> Python3 conversion with SWIG 4.0+ and Python 3.5+.

## Running the script

It is assumed that you have generated your file with 

```
swig -python -py3 -c++ my_module.i
```

You will need to edit the items ``settings.py`` to include any classes, special prefixes, and type hints.  The default supports most basic datatypes, and some STL classes.

See ``klampt_settings.py`` for an example from the Klampt project, which is a relatively complex project involving array types, vector types, and Numpy support.

To process your module's docstrings, simply run:

```
python3 main.py path/to/my_module.py > temp.py
cp temp.py path/to/my_module.py
```

That's it!

