#!/usr/bin/python
# ================================
# (C)2023 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# EMAG
# search and replace user channel names for selected item


import modo
import modo.constants as c
import lx
import sys

sys.path.append('{}\\scripts'.format(lx.eval('query platformservice alias ? {kit_h3d_utilites:}')))
import h3d_utils as h3du
from h3d_debug import H3dDebug
from h3d_exceptions import H3dExitException


def main():
    items = modo.Scene().selected

    SEARCH_STR = ''
    REPLACE_STR = ''

    for item in items:
        item.select(replace=True)
        print(item.name)
        for channel in item.channels():
            lx.eval("select.drop channel")
            lx.eval("select.channel {{{}:{}@lmb=x}} add".format(item.id, channel.name))
            newname = '{}'.format(channel.name).replace(SEARCH_STR, REPLACE_STR)
            lx.eval('channel.username username:"{}"'.format(newname))


if __name__ == '__main__':
    try:
        main()
    except H3dExitException as e:
        print(e.message)
