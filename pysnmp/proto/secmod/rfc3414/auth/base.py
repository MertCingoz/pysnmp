#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2020, Ilya Etingof <etingof@gmail.com>
# License: https://www.pysnmp.com/pysnmp/license.html
#
from pysnmp.proto import errind, error


class AbstractAuthenticationService:
    SERVICE_ID = None

    def hashPassphrase(self, authKey):
        raise error.ProtocolError(errind.noAuthentication)

    def localizeKey(self, authKey, snmpEngineID):
        raise error.ProtocolError(errind.noAuthentication)

    @property
    def digestLength(self):
        raise error.ProtocolError(errind.noAuthentication)

    # 7.2.4.1
    def authenticateOutgoingMsg(self, authKey, wholeMsg):
        raise error.ProtocolError(errind.noAuthentication)

    # 7.2.4.2
    def authenticateIncomingMsg(self, authKey, authParameters, wholeMsg):
        raise error.ProtocolError(errind.noAuthentication)
