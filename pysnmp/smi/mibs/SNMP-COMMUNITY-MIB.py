#
# This file is part of pysnmp software.
#
# Copyright (c) 2005-2019, Ilya Etingof <etingof@gmail.com>
# License: https://www.pysnmp.com/pysnmp/license.html
#
# PySNMP MIB module SNMP-COMMUNITY-MIB (https://www.pysnmp.com/pysnmp)
# ASN.1 source http://mibs.pysnmp.com:80/asn1/SNMP-COMMUNITY-MIB
# Produced by pysmi-0.1.3 at Mon Apr 17 13:47:39 2017
# On host grommit.local platform Darwin version 16.4.0 by user ilya
# Using Python version 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22)
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols(
    "ASN1", "OctetString", "ObjectIdentifier", "Integer"
)
(NamedValues,) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
(
    ConstraintsUnion,
    ConstraintsIntersection,
    ValueRangeConstraint,
    ValueSizeConstraint,
    SingleValueConstraint,
) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsUnion",
    "ConstraintsIntersection",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "SingleValueConstraint",
)
SnmpAdminString, SnmpEngineID = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB", "SnmpAdminString", "SnmpEngineID"
)
snmpTargetAddrEntry, SnmpTagValue = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB", "snmpTargetAddrEntry", "SnmpTagValue"
)
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols(
    "SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance"
)
(
    Unsigned32,
    MibScalar,
    MibTable,
    MibTableRow,
    MibTableColumn,
    NotificationType,
    Bits,
    ModuleIdentity,
    TimeTicks,
    Counter32,
    Gauge32,
    Integer32,
    Counter64,
    MibIdentifier,
    IpAddress,
    snmpModules,
    iso,
    ObjectIdentity,
) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Unsigned32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "Bits",
    "ModuleIdentity",
    "TimeTicks",
    "Counter32",
    "Gauge32",
    "Integer32",
    "Counter64",
    "MibIdentifier",
    "IpAddress",
    "snmpModules",
    "iso",
    "ObjectIdentity",
)
DisplayString, RowStatus, StorageType, TextualConvention = mibBuilder.importSymbols(
    "SNMPv2-TC", "DisplayString", "RowStatus", "StorageType", "TextualConvention"
)
snmpCommunityMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 18))
if mibBuilder.loadTexts:
    snmpCommunityMIB.setRevisions(
        (
            "2003-08-06 00:00",
            "2000-03-06 00:00",
        )
    )
if mibBuilder.loadTexts:
    snmpCommunityMIB.setLastUpdated("200308060000Z")
if mibBuilder.loadTexts:
    snmpCommunityMIB.setOrganization("SNMPv3 Working Group")
if mibBuilder.loadTexts:
    snmpCommunityMIB.setContactInfo(
        "WG-email: snmpv3@lists.tislabs.com Subscribe: majordomo@lists.tislabs.com In msg body: subscribe snmpv3 Co-Chair: Russ Mundy SPARTA, Inc Postal: 7075 Samuel Morse Drive Columbia, MD 21045 USA EMail: mundy@tislabs.com Phone: +1 410-872-1515 Co-Chair: David Harrington Enterasys Networks Postal: 35 Industrial Way P. O. Box 5005 Rochester, New Hampshire 03866-5005 USA EMail: dbh@enterasys.com Phone: +1 603-337-2614 Co-editor: Rob Frye Vibrant Solutions Postal: 2711 Prosperity Ave Fairfax, Virginia 22031 USA E-mail: rfrye@vibrant-1.com Phone: +1-703-270-2000 Co-editor: David B. Levi Nortel Networks Postal: 3505 Kesterwood Drive Knoxville, Tennessee 37918 E-mail: dlevi@nortelnetworks.com Phone: +1 865 686 0432 Co-editor: Shawn A. Routhier Wind River Systems, Inc. Postal: 500 Wind River Way Alameda, CA 94501 E-mail: sar@epilogue.com Phone: +1 510 749 2095 Co-editor: Bert Wijnen Lucent Technologies Postal: Schagen 33 3461 GL Linschoten Netherlands Email: bwijnen@lucent.com Phone: +31-348-407-775 "
    )
if mibBuilder.loadTexts:
    snmpCommunityMIB.setDescription(
        "This MIB module defines objects to help support coexistence between SNMPv1, SNMPv2c, and SNMPv3. Copyright (C) The Internet Society (2003) This version of this MIB module is part of RFC 3584; see the RFC itself for full legal notices."
    )
snmpCommunityMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 18, 1))
snmpCommunityMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 18, 2))
snmpCommunityTable = MibTable(
    (1, 3, 6, 1, 6, 3, 18, 1, 1),
)
if mibBuilder.loadTexts:
    snmpCommunityTable.setStatus("current")
if mibBuilder.loadTexts:
    snmpCommunityTable.setDescription(
        "The table of community strings configured in the SNMP engine's Local Configuration Datastore (LCD)."
    )
snmpCommunityEntry = MibTableRow(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1),
).setIndexNames((1, "SNMP-COMMUNITY-MIB", "snmpCommunityIndex"))
if mibBuilder.loadTexts:
    snmpCommunityEntry.setStatus("current")
if mibBuilder.loadTexts:
    snmpCommunityEntry.setDescription(
        "Information about a particular community string."
    )
snmpCommunityIndex = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 1),
    SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)),
)
if mibBuilder.loadTexts:
    snmpCommunityIndex.setStatus("current")
if mibBuilder.loadTexts:
    snmpCommunityIndex.setDescription("The unique index value of a row in this table.")
snmpCommunityName = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 2), OctetString()
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityName.setStatus("current")
if mibBuilder.loadTexts:
    snmpCommunityName.setDescription(
        "The community string for which a row in this table represents a configuration. There is no SIZE constraint specified for this object because RFC 1157 does not impose any explicit limitation on the length of community strings (their size is constrained indirectly by the SNMP message size)."
    )
snmpCommunitySecurityName = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 3),
    SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)),
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunitySecurityName.setStatus("current")
if mibBuilder.loadTexts:
    snmpCommunitySecurityName.setDescription(
        "A human readable string representing the corresponding value of snmpCommunityName in a Security Model independent format."
    )
snmpCommunityContextEngineID = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 4), SnmpEngineID()
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityContextEngineID.setStatus("current")
if mibBuilder.loadTexts:
    snmpCommunityContextEngineID.setDescription(
        "The contextEngineID indicating the location of the context in which management information is accessed when using the community string specified by the corresponding instance of snmpCommunityName. The default value is the snmpEngineID of the entity in which this object is instantiated."
    )
snmpCommunityContextName = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 5),
    SnmpAdminString()
    .subtype(subtypeSpec=ValueSizeConstraint(0, 32))
    .clone(hexValue=""),
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityContextName.setStatus("current")
if mibBuilder.loadTexts:
    snmpCommunityContextName.setDescription(
        "The context in which management information is accessed when using the community string specified by the corresponding instance of snmpCommunityName."
    )
snmpCommunityTransportTag = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 6), SnmpTagValue().clone(hexValue="")
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityTransportTag.setStatus("current")
if mibBuilder.loadTexts:
    snmpCommunityTransportTag.setDescription(
        "This object specifies a set of transport endpoints which are used in two ways: - to specify the transport endpoints from which an SNMP entity will accept management requests, and - to specify the transport endpoints to which a notification may be sent using the community string matching the corresponding instance of snmpCommunityName. In either case, if the value of this object has zero-length, transport endpoints are not checked when either authenticating messages containing this community string, nor when generating notifications. The transports identified by this object are specified in the snmpTargetAddrTable. Entries in that table whose snmpTargetAddrTagList contains this tag value are identified. If a management request containing a community string that matches the corresponding instance of snmpCommunityName is received on a transport endpoint other than the transport endpoints identified by this object the request is deemed unauthentic. When a notification is to be sent using an entry in this table, if the destination transport endpoint of the notification does not match one of the transport endpoints selected by this object, the notification is not sent."
    )
snmpCommunityStorageType = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 7), StorageType()
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityStorageType.setStatus("current")
if mibBuilder.loadTexts:
    snmpCommunityStorageType.setDescription(
        "The storage type for this conceptual row in the snmpCommunityTable. Conceptual rows having the value 'permanent' need not allow write-access to any columnar object in the row."
    )
snmpCommunityStatus = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 18, 1, 1, 1, 8), RowStatus()
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityStatus.setStatus("current")
if mibBuilder.loadTexts:
    snmpCommunityStatus.setDescription(
        "The status of this conceptual row in the snmpCommunityTable. An entry in this table is not qualified for activation until instances of all corresponding columns have been initialized, either through default values, or through Set operations. The snmpCommunityName and snmpCommunitySecurityName objects must be explicitly set. There is no restriction on setting columns in this table when the value of snmpCommunityStatus is active(1)."
    )
snmpTargetAddrExtTable = MibTable(
    (1, 3, 6, 1, 6, 3, 18, 1, 2),
)
if mibBuilder.loadTexts:
    snmpTargetAddrExtTable.setStatus("current")
if mibBuilder.loadTexts:
    snmpTargetAddrExtTable.setDescription(
        "The table of mask and maximum message size (mms) values associated with the snmpTargetAddrTable. The snmpTargetAddrExtTable augments the snmpTargetAddrTable with a transport address mask value and a maximum message size value. The transport address mask allows entries in the snmpTargetAddrTable to define a set of addresses instead of just a single address. The maximum message size value allows the maximum message size of another SNMP entity to be configured for use in SNMPv1 (and SNMPv2c) transactions, where the message format does not specify a maximum message size."
    )
snmpTargetAddrExtEntry = MibTableRow(
    (1, 3, 6, 1, 6, 3, 18, 1, 2, 1),
)
snmpTargetAddrEntry.registerAugmentions(
    ("SNMP-COMMUNITY-MIB", "snmpTargetAddrExtEntry")
)
snmpTargetAddrExtEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())
if mibBuilder.loadTexts:
    snmpTargetAddrExtEntry.setStatus("current")
if mibBuilder.loadTexts:
    snmpTargetAddrExtEntry.setDescription(
        "Information about a particular mask and mms value."
    )
snmpTargetAddrTMask = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 18, 1, 2, 1, 1),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)).clone(hexValue=""),
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetAddrTMask.setStatus("current")
if mibBuilder.loadTexts:
    snmpTargetAddrTMask.setDescription(
        "The mask value associated with an entry in the snmpTargetAddrTable. The value of this object must have the same length as the corresponding instance of snmpTargetAddrTAddress, or must have length 0. An attempt to set it to any other value will result in an inconsistentValue error. The value of this object allows an entry in the snmpTargetAddrTable to specify multiple addresses. The mask value is used to select which bits of a transport address must match bits of the corresponding instance of snmpTargetAddrTAddress, in order for the transport address to match a particular entry in the snmpTargetAddrTable. Bits which are 1 in the mask value indicate bits in the transport address which must match bits in the snmpTargetAddrTAddress value. Bits which are 0 in the mask indicate bits in the transport address which need not match. If the length of the mask is 0, the mask should be treated as if all its bits were 1 and its length were equal to the length of the corresponding value of snmpTargetAddrTable. This object may not be modified while the value of the corresponding instance of snmpTargetAddrRowStatus is active(1). An attempt to set this object in this case will result in an inconsistentValue error."
    )
snmpTargetAddrMMS = MibTableColumn(
    (1, 3, 6, 1, 6, 3, 18, 1, 2, 1, 2),
    Integer32()
    .subtype(
        subtypeSpec=ConstraintsUnion(
            ValueRangeConstraint(0, 0),
            ValueRangeConstraint(484, 2147483647),
        )
    )
    .clone(484),
).setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTargetAddrMMS.setStatus("current")
if mibBuilder.loadTexts:
    snmpTargetAddrMMS.setDescription(
        "The maximum message size value associated with an entry in the snmpTargetAddrTable. Note that a value of 0 means that the maximum message size is unknown."
    )
snmpTrapAddress = MibScalar((1, 3, 6, 1, 6, 3, 18, 1, 3), IpAddress()).setMaxAccess(
    "accessible-for-notify"
)
if mibBuilder.loadTexts:
    snmpTrapAddress.setStatus("current")
if mibBuilder.loadTexts:
    snmpTrapAddress.setDescription(
        "The value of the agent-addr field of a Trap PDU which is forwarded by a proxy forwarder application using an SNMP version other than SNMPv1. The value of this object SHOULD contain the value of the agent-addr field from the original Trap PDU as generated by an SNMPv1 agent."
    )
snmpTrapCommunity = MibScalar((1, 3, 6, 1, 6, 3, 18, 1, 4), OctetString()).setMaxAccess(
    "accessible-for-notify"
)
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("current")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setDescription(
        "The value of the community string field of an SNMPv1 message containing a Trap PDU which is forwarded by a a proxy forwarder application using an SNMP version other than SNMPv1. The value of this object SHOULD contain the value of the community string field from the original SNMPv1 message containing a Trap PDU as generated by an SNMPv1 agent. There is no SIZE constraint specified for this object because RFC 1157 does not impose any explicit limitation on the length of community strings (their size is constrained indirectly by the SNMP message size)."
    )
snmpCommunityMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 18, 2, 1))
snmpCommunityMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 18, 2, 2))
snmpCommunityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 18, 2, 1, 1)
).setObjects(("SNMP-COMMUNITY-MIB", "snmpCommunityTableGroup"))
if mibBuilder.loadTexts:
    snmpCommunityMIBCompliance.setDescription(
        "The compliance statement for SNMP engines which implement the SNMP-COMMUNITY-MIB."
    )
snmpProxyTrapForwardCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 18, 2, 1, 2)
).setObjects(("SNMP-COMMUNITY-MIB", "snmpProxyTrapForwardGroup"))
if mibBuilder.loadTexts:
    snmpProxyTrapForwardCompliance.setDescription(
        "The compliance statement for SNMP engines which contain a proxy forwarding application which is capable of forwarding SNMPv1 traps using SNMPv2c or SNMPv3."
    )
snmpCommunityMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 6, 3, 18, 2, 1, 3)
).setObjects(("SNMP-COMMUNITY-MIB", "snmpCommunityTableGroup"))
if mibBuilder.loadTexts:
    snmpCommunityMIBFullCompliance.setDescription(
        "The compliance statement for SNMP engines which implement the SNMP-COMMUNITY-MIB with full read-create access."
    )
snmpCommunityTableGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 18, 2, 2, 1)).setObjects(
    ("SNMP-COMMUNITY-MIB", "snmpCommunityName"),
    ("SNMP-COMMUNITY-MIB", "snmpCommunitySecurityName"),
    ("SNMP-COMMUNITY-MIB", "snmpCommunityContextEngineID"),
    ("SNMP-COMMUNITY-MIB", "snmpCommunityContextName"),
    ("SNMP-COMMUNITY-MIB", "snmpCommunityTransportTag"),
    ("SNMP-COMMUNITY-MIB", "snmpCommunityStorageType"),
    ("SNMP-COMMUNITY-MIB", "snmpCommunityStatus"),
    ("SNMP-COMMUNITY-MIB", "snmpTargetAddrTMask"),
    ("SNMP-COMMUNITY-MIB", "snmpTargetAddrMMS"),
)
if mibBuilder.loadTexts:
    snmpCommunityTableGroup.setDescription(
        "A collection of objects providing for configuration of community strings for SNMPv1 (and SNMPv2c) usage."
    )
snmpProxyTrapForwardGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 18, 2, 2, 3)).setObjects(
    ("SNMP-COMMUNITY-MIB", "snmpTrapAddress"),
    ("SNMP-COMMUNITY-MIB", "snmpTrapCommunity"),
)
if mibBuilder.loadTexts:
    snmpProxyTrapForwardGroup.setDescription(
        "Objects which are used by proxy forwarding applications when translating traps between SNMP versions. These are used to preserve SNMPv1-specific information when translating to SNMPv2c or SNMPv3."
    )
mibBuilder.exportSymbols(
    "SNMP-COMMUNITY-MIB",
    PYSNMP_MODULE_ID=snmpCommunityMIB,
    snmpCommunityMIBFullCompliance=snmpCommunityMIBFullCompliance,
    snmpTargetAddrTMask=snmpTargetAddrTMask,
    snmpTargetAddrExtEntry=snmpTargetAddrExtEntry,
    snmpCommunityContextName=snmpCommunityContextName,
    snmpCommunityMIBConformance=snmpCommunityMIBConformance,
    snmpCommunityTableGroup=snmpCommunityTableGroup,
    snmpCommunityIndex=snmpCommunityIndex,
    snmpTrapCommunity=snmpTrapCommunity,
    snmpCommunityContextEngineID=snmpCommunityContextEngineID,
    snmpTrapAddress=snmpTrapAddress,
    snmpCommunityMIBObjects=snmpCommunityMIBObjects,
    snmpCommunityMIBCompliances=snmpCommunityMIBCompliances,
    snmpCommunityStorageType=snmpCommunityStorageType,
    snmpCommunitySecurityName=snmpCommunitySecurityName,
    snmpCommunityTable=snmpCommunityTable,
    snmpCommunityMIBGroups=snmpCommunityMIBGroups,
    snmpCommunityEntry=snmpCommunityEntry,
    snmpTargetAddrExtTable=snmpTargetAddrExtTable,
    snmpCommunityName=snmpCommunityName,
    snmpCommunityMIBCompliance=snmpCommunityMIBCompliance,
    snmpCommunityMIB=snmpCommunityMIB,
    snmpCommunityStatus=snmpCommunityStatus,
    snmpProxyTrapForwardCompliance=snmpProxyTrapForwardCompliance,
    snmpProxyTrapForwardGroup=snmpProxyTrapForwardGroup,
    snmpTargetAddrMMS=snmpTargetAddrMMS,
    snmpCommunityTransportTag=snmpCommunityTransportTag,
)
