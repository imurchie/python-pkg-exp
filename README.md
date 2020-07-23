## python-pkg-exp

A simple Python project with a nested package (i.e., a package that is releasable,
that exists as a sub-module of another package, also releasable), in order to
see if there is any way to normalize the importation.

To use, go into `src` and run `python index.py` to see the outer package
successfully importing sub-modules. Then go into `p2_code` and run `python index.py`
to see the inner package successfully importing modules in itself.
