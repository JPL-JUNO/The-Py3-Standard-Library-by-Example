"""
Created time: 2025-12-27 15:08:27
Author(s)   : Stephen CUI
File        : functools_update_wrapper.py
Email       : cuixuanstephen@gmail.com
Description : acquiring function properties

the partial object does not have __name__ or __doc__ attributes by default
使用 update_wrapper() 可以从原函数将属性复制或增加到 partial object
"""

import functools


def myfunc(a, b=2):
    "Docstring for myfunc()"
    print("  called myfunc with:", (a, b))


def show_details(name, f):
    "Show details of a callable object."
    print("{}:".format(name))
    print("  object:", f)
    print("  __name__:", end=" ")
    try:
        print(f.__name__)
    except AttributeError:
        print("(no __name__)")
    print("  __doc__", repr(f.__doc__))
    print()


show_details("myfunc", myfunc)

p1 = functools.partial(myfunc, b=4)
# 这里的 __doc__ 是 partial 的 __doc__，而不是 myfunc 的 __doc__
show_details("raw wrapper", p1)

print("Updating wrapper:")
# WRAPPER_ASSIGNMENTS 定义了增加到包装器的属性
print("  assign:", functools.WRAPPER_ASSIGNMENTS)
# WRAPPER_UPDATES 列出了要修改的值
print("  update:", functools.WRAPPER_UPDATES)
print()

functools.update_wrapper(p1, myfunc)  # 原函数属性复制到 partial object
show_details("updated wrapper", p1)
