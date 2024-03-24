#
# PySNMP MIB module SNMP-USM-HMAC-SHA2-MIB (https://www.pysnmp.com/pysnmp)
# ASN.1 source http://mibs.pysnmp.com:80/asn1/SNMP-USM-HMAC-SHA2-MIB
# Produced by pysmi-0.1.4 at Thu Aug  3 02:14:32 2017
# On host grommit.local platform Darwin version 16.4.0 by user ilya
# Using Python version 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22)
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols(
    "ASN1", "OctetString", "Integer", "ObjectIdentifier"
)
(NamedValues,) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
(
    ValueSizeConstraint,
    SingleValueConstraint,
    ConstraintsUnion,
    ConstraintsIntersection,
    ValueRangeConstraint,
) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ValueSizeConstraint",
    "SingleValueConstraint",
    "ConstraintsUnion",
    "ConstraintsIntersection",
    "ValueRangeConstraint",
)
(snmpAuthProtocols,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB", "snmpAuthProtocols"
)
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols(
    "SNMPv2-CONF", "NotificationGroup", "ModuleCompliance"
)
(
    Counter32,
    Bits,
    MibScalar,
    MibTable,
    MibTableRow,
    MibTableColumn,
    Counter64,
    ObjectIdentity,
    TimeTicks,
    Gauge32,
    Unsigned32,
    MibIdentifier,
    mib_2,
    iso,
    ModuleIdentity,
    NotificationType,
    IpAddress,
    Integer32,
) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Counter32",
    "Bits",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Counter64",
    "ObjectIdentity",
    "TimeTicks",
    "Gauge32",
    "Unsigned32",
    "MibIdentifier",
    "mib-2",
    "iso",
    "ModuleIdentity",
    "NotificationType",
    "IpAddress",
    "Integer32",
)
TextualConvention, DisplayString = mibBuilder.importSymbols(
    "SNMPv2-TC", "TextualConvention", "DisplayString"
)
snmpUsmHmacSha2MIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 235))
if mibBuilder.loadTexts:
    snmpUsmHmacSha2MIB.setRevisions(
        (
            "2016-04-18 00:00",
            "2015-10-14 00:00",
        )
    )
if mibBuilder.loadTexts:
    snmpUsmHmacSha2MIB.setLastUpdated("201604180000Z")
if mibBuilder.loadTexts:
    snmpUsmHmacSha2MIB.setOrganization("SNMPv3 Working Group")
if mibBuilder.loadTexts:
    snmpUsmHmacSha2MIB.setContactInfo(
        "WG email: OPSAWG@ietf.org Subscribe: https://www.ietf.org/mailman/listinfo/opsawg Editor: Johannes Merkle secunet Security Networks Postal: Mergenthaler Allee 77 D-65760 Eschborn Germany Phone: +49 20154543091 Email: johannes.merkle@secunet.com Co-Editor: Manfred Lochter Bundesamt fuer Sicherheit in der Informationstechnik (BSI) Postal: Postfach 200363 D-53133 Bonn Germany Phone: +49 228 9582 5643 Email: manfred.lochter@bsi.bund.de"
    )
if mibBuilder.loadTexts:
    snmpUsmHmacSha2MIB.setDescription(
        "Definitions of Object Identities needed for the use of HMAC-SHA2 Authentication Protocols by SNMP's User-based Security Model. Copyright (c) 2016 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info)."
    )
usmHMAC128SHA224AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 4))
if mibBuilder.loadTexts:
    usmHMAC128SHA224AuthProtocol.setStatus("current")
if mibBuilder.loadTexts:
    usmHMAC128SHA224AuthProtocol.setDescription(
        "The Authentication Protocol usmHMAC128SHA224AuthProtocol uses HMAC-SHA-224 and truncates output to 128 bits."
    )
if mibBuilder.loadTexts:
    usmHMAC128SHA224AuthProtocol.setReference(
        "- Krawczyk, H., Bellare, M., and R. Canetti, HMAC: Keyed-Hashing for Message Authentication, RFC 2104. - National Institute of Standards and Technology, Secure Hash Standard (SHS), FIPS PUB 180-4, 2012."
    )
usmHMAC192SHA256AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 5))
if mibBuilder.loadTexts:
    usmHMAC192SHA256AuthProtocol.setStatus("current")
if mibBuilder.loadTexts:
    usmHMAC192SHA256AuthProtocol.setDescription(
        "The Authentication Protocol usmHMAC192SHA256AuthProtocol uses HMAC-SHA-256 and truncates output to 192 bits."
    )
if mibBuilder.loadTexts:
    usmHMAC192SHA256AuthProtocol.setReference(
        "- Krawczyk, H., Bellare, M., and R. Canetti, HMAC: Keyed-Hashing for Message Authentication, RFC 2104. - National Institute of Standards and Technology, Secure Hash Standard (SHS), FIPS PUB 180-4, 2012."
    )
usmHMAC256SHA384AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 6))
if mibBuilder.loadTexts:
    usmHMAC256SHA384AuthProtocol.setStatus("current")
if mibBuilder.loadTexts:
    usmHMAC256SHA384AuthProtocol.setDescription(
        "The Authentication Protocol usmHMAC256SHA384AuthProtocol uses HMAC-SHA-384 and truncates output to 256 bits."
    )
if mibBuilder.loadTexts:
    usmHMAC256SHA384AuthProtocol.setReference(
        "- Krawczyk, H., Bellare, M., and R. Canetti, HMAC: Keyed-Hashing for Message Authentication, RFC 2104. - National Institute of Standards and Technology, Secure Hash Standard (SHS), FIPS PUB 180-4, 2012."
    )
usmHMAC384SHA512AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 7))
if mibBuilder.loadTexts:
    usmHMAC384SHA512AuthProtocol.setStatus("current")
if mibBuilder.loadTexts:
    usmHMAC384SHA512AuthProtocol.setDescription(
        "The Authentication Protocol usmHMAC384SHA512AuthProtocol uses HMAC-SHA-512 and truncates output to 384 bits."
    )
if mibBuilder.loadTexts:
    usmHMAC384SHA512AuthProtocol.setReference(
        "- Krawczyk, H., Bellare, M., and R. Canetti, HMAC: Keyed-Hashing for Message Authentication, RFC 2104. - National Institute of Standards and Technology, Secure Hash Standard (SHS), FIPS PUB 180-4, 2012."
    )
mibBuilder.exportSymbols(
    "SNMP-USM-HMAC-SHA2-MIB",
    usmHMAC256SHA384AuthProtocol=usmHMAC256SHA384AuthProtocol,
    usmHMAC192SHA256AuthProtocol=usmHMAC192SHA256AuthProtocol,
    usmHMAC384SHA512AuthProtocol=usmHMAC384SHA512AuthProtocol,
    PYSNMP_MODULE_ID=snmpUsmHmacSha2MIB,
    snmpUsmHmacSha2MIB=snmpUsmHmacSha2MIB,
    usmHMAC128SHA224AuthProtocol=usmHMAC128SHA224AuthProtocol,
)
