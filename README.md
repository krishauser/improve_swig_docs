# Improve SWIG Docs
## Kris Hauser 

If you've ever used SWIG to auto-generate docstrings, you'll realize that the documentation is horrendous for readers of the target language. In particular, there's a lot of cruft around the function declarations, and SWIG type hints throw IDEs and linters into a frenzy!

This script solves all of that.

## Prerequisites

This package supports C/C++ -> Python3 conversion with SWIG 4.0+ and Python 3.5+.

## Running the script

It is assumed that you have generated your file with 

```
swig -python -py3 -c++ my_module.i
```

You will need to edit the items ``settings.py`` to include any classes, special prefixes, and type hints.  See ``klampt_settings.py`` for an example from the Klampt project.

To process your module's docstrings, simply run:

```
python3 main.py my_module.py > my_module_improved.py
```

That's it!

