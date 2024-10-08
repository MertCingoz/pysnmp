#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2020, Ilya Etingof <etingof@gmail.com>
# License: https://www.pysnmp.com/pysnmp/license.html
#
from typing import Any, Dict


from pysnmp import nextid
from pysnmp.proto import error


class Cache:
    __stateReference = nextid.Integer(0xFFFFFF)
    __cacheEntries: Dict[int, Any]

    def __init__(self):
        self.__cacheEntries = {}

    def push(self, **securityData):
        stateReference = self.__stateReference()
        self.__cacheEntries[stateReference] = securityData
        return stateReference

    def pop(self, stateReference):
        if stateReference in self.__cacheEntries:
            securityData = self.__cacheEntries[stateReference]
        else:
            raise error.ProtocolError(
                f"Cache miss for stateReference={stateReference} at {self}"
            )
        del self.__cacheEntries[stateReference]
        return securityData

    def isEmpty(self):
        return not bool(self.__cacheEntries)
