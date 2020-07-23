## Package One

This package includes a module, `p2`, which is used locally but can be released
as its own package. The code for `p2` is in `p2_code`, and `p2` is symlinked to
`p2_code/p2` so that in both places (whether imported from `p1`, or installed
with `pip` and then imported as a package) the normal import will work:
```python
import p2.goodbye
```
