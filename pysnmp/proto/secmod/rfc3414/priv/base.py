#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2020, Ilya Etingof <etingof@gmail.com>
# License: https://www.pysnmp.com/pysnmp/license.html
#
from pysnmp.proto import error


class AbstractEncryptionService:
    SERVICE_ID = None
    KEY_SIZE = 0

    def hashPassphrase(self, authProtocol, privKey):
        raise error.ProtocolError("no encryption")

    def localizeKey(self, authProtocol, privKey, snmpEngineID):
        raise error.ProtocolError("no encryption")

    def encryptData(self, encryptKey, privParameters, dataToEncrypt):
        raise error.ProtocolError("no encryption")

    def decryptData(self, decryptKey, privParameters, encryptedData):
        raise error.ProtocolError("no encryption")
