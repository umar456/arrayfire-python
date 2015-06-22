import inspect
from .library import *

def dim4(d0=1, d1=1, d2=1, d3=1):
    c_dim4 = c_longlong * 4
    out = c_dim4(1, 1, 1, 1)

    for i, dim in enumerate((d0, d1, d2, d3)):
        if (dim is not None): out[i] = dim

    return out

def dim4_tuple(dims):
    assert(isinstance(dims, tuple))
    out = [1]*4

    for i, dim in enumerate(dims):
        out[i] = dim

    return tuple(out)

def is_valid_scalar(a):
    return isinstance(a, float) or isinstance(a, int) or isinstance(a, complex)

def safe_call(af_error):
    if (af_error != AF_SUCCESS.value):
        c_err_str = c_char_p(0)
        c_err_len = c_longlong(0)
        clib.af_get_last_error(pointer(c_err_str), pointer(c_err_len))
        raise RuntimeError(c_err_str.value, af_error)
