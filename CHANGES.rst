Revision 7.1.21, released on Jun 19, 2025
-----------------------------------------

- Fixed a bug in bulk walk command when lookupMib is set to False.

Revision 7.1.20, released on May 01, 2025
-----------------------------------------

- Implemented v1arch dispatcher timeout support.

Revision 7.1.19, released on Apr 27, 2025
-----------------------------------------

- Resolved dispatcher resource leak issue.

Revision 7.1.18, released on Apr 26, 2025
-----------------------------------------

- Upgraded pysmi dependency to 1.6.1.

Revision 7.1.17, released on Mar 19, 2025
-----------------------------------------

- Fixed an SNMPv2-SMI issue.

Revision 7.1.16, released on Jan 15, 2025
-----------------------------------------

- Fixed a few MIB related issues.

Revision 7.1.15, released on Dec 05, 2024
-----------------------------------------

- Improved shadow cloning patch.
- Fixed v1arch local address issue.

Revision 7.1.14, released on Dec 03, 2024
-----------------------------------------

- Fixed shadow cloning issue.

Revision 7.1.13, released on Nov 07, 2024
-----------------------------------------

- Fixed a resource leak issue.

Revision 7.1.12, released on Nov 06, 2024
-----------------------------------------

- Reverted some changes in named values support.

Revision 7.1.11, released on Nov 04, 2024
-----------------------------------------

- Reverted some changes in fixed length support.

Revision 7.1.10, released on Nov 04, 2024
-----------------------------------------

- Reimplemented getReference in a few MIB objects.

Revision 7.1.9, released on Nov 02, 2024
----------------------------------------

- Updated built-in MIBs to match latest PySMI compiled results.

Revision 7.1.8, released on Oct 14, 2024
----------------------------------------

- Fixed a bug in compatibility layer.

Revision 7.1.7, released on Oct 13, 2024
----------------------------------------

- Fixed two bugs in MIB related code and improved compatibility layer.

Revision 7.1.6, released on Oct 12, 2024
----------------------------------------

- Method names are revised to be PEP 8 compliant. Compatibility layer is
  added to support most of the old method names, but will be removed in the
  next major release, 8.0.
- Python 3.8 support is dropped.
- Python 3.13 support is added.

Revision 7.1.5, released on Oct 06, 2024
----------------------------------------

- The pysmi dependency is now optional.

Revision 7.1.4, released on Sep 17, 2024
----------------------------------------

- Dumped pysnmpcrypto dependency and bind to cryptography if presented.

Revision 7.1.3, released on Sep 15, 2024
----------------------------------------

- Fixed a bulkCmd IndexError bug.
- Cleaned up nextCmd/bulkCmd related code.
- Revised docs and examples accordingly.

Revision 7.1.2, released on Sep 14, 2024
----------------------------------------

- Revised v1arch hlapi and its docs/examples.
- Revised nextCmd, bulkCmd, walkCmd, and bulkWalkCmd returned collections.
- Moved Slim class to v1arch.

Revision 7.1.1, released on Sep 12, 2024
----------------------------------------

- Reimplemented walkCmd and bulkWalkCmd.

Revision 7.1.0, released on Sep 11, 2024
----------------------------------------

- Removed pyasn1.compat dependency.
- Switched to async DNS resolver.

Revision 7.0.4, released on Sep 18, 2024
----------------------------------------

- Removed pyasn1.compat dependency.

Revision 7.0.3, released on Aug 26, 2024
----------------------------------------

- The high-level API (`hlapi`) extended to cover lightweight SNMP v1arch
  in hope to ease the use of packet-level SNMP API.

  By way of introducing v1arch hlapi, the sub-packages layout changed
  so that `pysnmp.hlapi` is moved to `pysnmp.hlapi.v3arch` and the new
  v1arch layer is introduced in `pysnmp.hlapi.v1arch`. This change does
  not break backward compatibility as `pysnmp.hlapi` still defaults to
  `pysnmp.hlapi.v3arch`.

  The `pysnmp.hlapi.v1arch` is designed to be as much similar in use
  to `pysnmp.hlapi.v3arch`, but with high-performance in mind. One of
  the consequences of this higher performance focus is that various
  automation around building well-formed SNMP messages is and mediating
  differences between SNMP versions is not present in this new `v1arch`
  layer.

- The signature of the hlapi `.sendNotification()` call has changed
  to accept `*varBinds` instead of a sequence of `varBinds`. The rationale
  is to unify this method call with similar methods of CommandGenerator.
  This change should not compromise backward compatibility with pysnmp 4.

Revision 7.0.2, released on Aug 25, 2024
----------------------------------------

- Fixed a duplicate item issue in bulkWalkCmd.

Revision 7.0.1, released on Aug 24, 2024
----------------------------------------

- Many really old backward-compatibility code snippets removed.
  Most importantly, everything related to (non-standard) UNIX domain socket
  transport are gone.

- The MIB instrumentation API overhauled in backward incompatible
  way:

  * MIB instrumentation methods signatures simplified to accept
    just var-binds (as var-arg), the rest of the parameters packed
    into opaque kwargs

  * CommandResponder application passes `snmpEngine` and optionally
    user-supplied `cbCtx` object throughout the MIB instrumentation
    methods. The goal is to let MIB objects access/modify whatever
    custom Python objects they need while being called back.

- Cherry-picked many minor fixes from etingof/master branch.

Revision 7.0.0, released on Aug 22, 2024
----------------------------------------

- Applied PEP8 recommended names. This breaks backward compatibility.

Revision 6.2.6, released on Sep 11, 2024
----------------------------------------

- Removed pyasn1.compat dependency. A helper release to enable migration.

Revision 6.2.5, released on Aug 10, 2024
----------------------------------------

- Improved OrderedDict performance.
- User credentials changes are now reflected in the LCD.
- Other cleanup.

Revision 6.2.4, released on Jul 20, 2024
----------------------------------------

- Deleted more obsolete items.

Revision 6.2.3, released on Jul 17, 2024
----------------------------------------

- Removed unused dependencies.

Revision 6.2.2, released on Jul 16, 2024
----------------------------------------

- Removed package postfix. A helper release to enable migration.

Revision 6.2.1, released on Jul 14, 2024
----------------------------------------

- Cleaned up sync API leftover.

Revision 6.2.0, released on Jul 12, 2024
----------------------------------------

- Retired temporary sync API.

Revision 6.1.4, released on Sep 11, 2024
----------------------------------------

- Removed pyasn1.compat dependency. A helper release to enable migration.

Revision 6.1.3, released on Jul 16, 2024
----------------------------------------

- Removed package postfix. A helper release to enable migration.

Revision 6.1.2, released on Mar 25, 2024
----------------------------------------

- Merged changes from 4.4.13.

Revision 6.1.1, released on Mar 23, 2024
----------------------------------------

- Fixed more access descriptors.

Revision 6.1.0, released on Mar 23, 2024
----------------------------------------

- Initial work to support pysmi-lextudio 1.3.0 and above.

Revision 6.0.13, released on July 16, 2024
------------------------------------------

- Removed package postfix. A helper release to enable migration.

Revision 6.0.12, released on Mar 23, 2024
-----------------------------------------

- Restricted pysmi-lextudio version to 1.2.0 to avoid breaking changes.

Revision 6.0.11, released on Mar 14, 2024
-----------------------------------------

- Fixed walkCmd bug.

Revision 6.0.10, released on Mar 13, 2024
-----------------------------------------

- Fixed bulkWalkCmd bug.

Revision 6.0.9, released on Mar 08, 2024
----------------------------------------

- Added sync oneliner back.

Revision 6.0.8, released on Mar 07, 2024
----------------------------------------

- Fix annotations.

Revision 6.0.7, released on Mar 07, 2024
----------------------------------------

- Added walkCmd() and bulkWalkCmd() to hlapi.

Revision 6.0.6, released on Mar 04, 2024
----------------------------------------

- Improved Slim class to support IPv6.
- Added some sync API based on asyncio.

Revision 6.0.5, released on Mar 01, 2024
----------------------------------------

- Added custom socket support in openServerMode.
- Fixed various bugs in RFC3414 error handling.

Revision 6.0.4, released on Feb 28, 2024
----------------------------------------

- Reverted some changes in 6.0.2 on asyncio dispatch.

Revision 6.0.3, released on Feb 26, 2024
----------------------------------------

- Deleted asyncore related bits.

Revision 6.0.2, released on Feb 13, 2024
----------------------------------------

- Simplified asyncio dispatch.
- Added ignoreNonIncreasingOid option to nextCmd and bulkCmd.

Revision 6.0.1, released on Feb 10, 2024
----------------------------------------

- Fixed a dispatch bug related to "Slim.close".

Revision 6.0.0, released on Feb 10, 2024
----------------------------------------

- Improved asyncio "runDispatcher" method to support timeout.
- Changed internal defaults to asyncio.
- Converted asyncore samples to asyncio.

Revision 5.1.0, released on July 16, 2024
-----------------------------------------

- Removed package postfix. A helper release to enable migration.

Revision 5.0.34, released on Feb 04, 2024
-----------------------------------------

- Fixed a v3 authentication issue when wrong user name is used.

Revision 5.0.33, released on Jan 12, 2024
-----------------------------------------

- Fixed an import error with Python 3.12.

Revision 5.0.32, released on Dec 25, 2023
-----------------------------------------

- Added timeout and retries to Slim class.

Revision 5.0.31, released on Dec 09, 2023
-----------------------------------------

- Added experimental Python 3.12 support based on pyasyncore. But all
  asyncore based API is deprecated and will be removed in the next major
  release.

Revision 5.0.30, released on Nov 20, 2023
-----------------------------------------

- Added pyasn1 0.5.1 support.

Revision 5.0.29, released on Sep 12, 2023
-----------------------------------------

- Fix asyncio hlapi double awaitable returns.

Revision 5.0.28, released on May 08, 2023
-----------------------------------------

- Fixed SNMP engine ID generation on Windows.

Revision 5.0.27, released on Apr 28, 2023
-----------------------------------------

- SNMPv3 crypto operations that require external dependencies
  made dependent on the optional external
  package -- pysnmpcrypto.
- By switching to pysnmpcrypto, pysnmp effectively migrates from
  PyCryptodomex to pyca/cryptography whenever available on the
  platform.

Revision 5.0.26, released on Apr 21, 2023
-----------------------------------------

- Blocked pyasn1 new release due to its breaking changes.

Revision 5.0.25, released on Jan 26, 2023
-----------------------------------------

- Added Slim class and simplified some examples.

Revision 5.0.24, released on Jan 22, 2023
-----------------------------------------

- Fixed a #SNMP demo compatibility issue.

Revision 5.0.23, released on Jan 21, 2023
-----------------------------------------

- Fixed a #SNMP demo compatibility issue.
- Fixed passwordToKeySHA.

Revision 5.0.22, released on Jan 20, 2023
-----------------------------------------

- Enabled Python 3.11 support.

Revision 5.0.21, released on Dec 26, 2022
-----------------------------------------

- Switched to pyasn1/pyasn1 package.

Revision 5.0.20, released on Dec 01, 2022
-----------------------------------------

- Removed legacy paddings in v3 packets.

Revision 5.0.18, released on Nov 13, 2022
-----------------------------------------

- Changed web site to pysnmp.com.
- Inherited all changes made by Splunk team.

Revision 4.4.13, released on 2019-11-XX
-----------------------------------------

- Fixed `genErr` handing in Command Responder when mapping MIB instrumentation
  exception onto SNMP errors. Prior to this fix, `genErr` would never be
  reported back to SNMP manager.

Revision 4.4.12, released on Sep 24, 2019
-----------------------------------------

- Fixed broken SNMPv3 `msgFlag` initialization on authoritative SNMP
  engine ID discovery. This bug causes secure communication with peer
  SNMP engines to stall at SNMP engine ID discovery procedure.

Revision 4.4.11, released on Aug 10, 2019
-----------------------------------------

- Added SNMPv3 USM master and localized keys support to LCD configuration
- Improved initial and runtime USM debugging
- Fixed a bug in USM configuration which did not allow the same user names
  to be added under different security names

Revision 4.4.10, released on Jul 29, 2019
-----------------------------------------

- Reworked VACM access control function. Most important changes include:

  * Added subtree match negation support (vacmViewTreeFamilyType)
  * Added subtree family mask support (vacmViewTreeFamilyMask)
  * Added prefix content name matching support (vacmAccessContextMatch)
  * Added key VACM tables caching for better `isAccessAllowed` lookup
    performance

  One potential incompatibility may be caused by the `addContext()` call
  which now needs to be made explicitly during low-level VACM configuration
  rather than be a side effect of `addVacmAccess()` call.

- Rebased MIB importing code onto `importlib` because `imp` is long
  deprecated
- Received MIB objects resolution made more forgiving to errors, added
  optional `ignoreErrors` parameter to `ObjectType.resolveWithMib()` to
  control that behaviour.
- Fixed asyncore main loop to respect non-default timer resolution
- Fixed `.setTimerResolution()` behaviour of abstract main loop dispatcher
  to update call intervals of the existing periodic dispatcher jobs
- Fixed `var-bindings` initialization to prevent pyasn1 encoder failures
  with newer pyasn1 versions where `SequenceOf` type looses its default
  initializer.
- Fixed crash on uninitialized component serialization left out in
  SNMP v1 TRAP PDU to SNMPv2/3 TRAP PDU proxy translation routine.

Revision 4.4.9, released on Feb 09, 2019
-----------------------------------------

- Made MIB loader ignoring file and directory access errors
- Added missing SNMP PDU error classes and their handling in Command Responder
- Fixed crash on MIB load failure in case of directory access error
- Fixed socket transparency option (IPV6_TRANSPARENT) to make IPv6
  transparent operation functional

Revision 4.4.8, released on Dec 30, 2018
----------------------------------------

- Fixed Pythonized MIB load (in the source form) - made sure to turn
  it into a code object prior to its execution

Revision 4.4.7, released on Dec 29, 2018
----------------------------------------

- Copyright notice extended to the year 2019
- Exposed ASN.1 `Null` type through `rfc1902` module for convenience.
- Use `compile()` before `exec`'ing MIB modules to attach filename to
  the stack frames (ultimately shown in traceback/debugger)
- Fixed hlapi/v3arch transport target caching to ensure transport targets
  are different even if just timeout/retries options differ
- Fixed hlapi LCD configurator to include `contextName`. Prior to this fix
  sending SNMPv3 TRAP with non-default `contextName` would fail.
- Fixed possible duplicate key occurrence in the `OrderedDict` following
  a race condition
- Fixed undefined name references in `inet_pton`/`inet_ntop` substitute
  routines for IPv6 in `TRANSPORT-ADDRESS-MIB.py`

Revision 4.4.6, released on Sep 13, 2018
----------------------------------------

- Improved package build and dependency tracking
- Fixed missing LICENSE from the tarball distribution
- Fixed `CommandGeneratorLcdConfigurator.unconfigure()` to fully clean up
  internal caches, otherwise repetitive attempts to configure the target
  would fail.
- Fix to tolerate possible duplicate enumerations in `Bits` and `Integer`
  SMI types.
- Fix to tolerate non-initialised entries in SNMP community table. Once a
  bad entry sneaked into the SNMP community table, all the subsequent
  SNMP v1/v2c operations failed. The fix ignores incomplete SNMP community
  table entries in the course of building indices.

Revision 4.4.5, released on Aug 05, 2018
----------------------------------------

- Added PySnmpError.cause attribute holding parent exception tuple
- Fixed broken InetAddressType rendering caused by a pyasn1 regression
- Fixed typo in RFC1158 module
- Fixed possible infinite loop in GETBULK response PDU builder
- Fixed memory leak in the `config.delContext()` VACM management harness
- Fixed `Bits` class initialization when enumeration values are given
- Fixed crash caused by incoming SNMPv3 message requesting SNMPv1/v2c
  security model
- Fixed out-of-scope OIDs leaking at the end of SNMP table at hlapi
  `nextCmd` and `bulkCmd` calls when `lexicographicMode = False`

Revision 4.4.4, released on Jan 03, 2018
----------------------------------------

- Copyright notice extended to the year 2018
- Fixed short local key expansion at 3DES key localization
  implementation.

Revision 4.4.3, released on Dec 22, 2017
----------------------------------------

- Migrated references from SourceForge
- Added missing SHA2 support for Blumenthal key localization
- Fixed named bits handling at rfc1902.Bits
- Fixed missing SmiError exception class at pysnmp.proto.rfc1155
- Fixed SNMP v1->v2c PDU proxy -- error-status & error-index fields
  from v1 PDU get copied over to v2c PDU in addition to the exception
  sentinels being set

Revision 4.4.2, released on Nov 11, 2017
----------------------------------------

- The pysnmp version being used gets exposed to the MIB modules
  via the `MibBuilder` instance
- The .setObjects() method of the SMI types now accepts
  `append=False` parameter to let the caller adding more
  than 255 elements over the course of multiple calls
- Added support for some more missing fields of SMIv2 MACRO types
- Example scripts rearranged in a way that IPv6 requirement is
  clearly encoded in the script's name
- Fixed SNMPv2-SMI.NotificationType to expose .set/getReference()
  instead of .set/getRevision() which should not be there in the
  first place
- Fixed non-implied-OID encoding in SNMP table indices
- Fixed inconsistent SNMPv3 discovery and retrying algorithm

Revision 4.4.1, released on Oct 23, 2017
----------------------------------------

- HMAC-SHA-2 Authentication Protocols support added (RFC-7860)
- The pycryptodome dependency replaced with pycryptodomex as
  it is recommended by the upstream to avoid unwanted interference
  with PyCrypto package should it also be installed
- Sphinx theme changed to Alabaster in the documentation
- Minor adjustments towards pyasn1 0.4.x compatibility
- Fixed ObjectIdentifier-into-ObjectIdentity casting at
  rfc1902.ObjectType MIB resolution harness
- Fixed NetworkAddress object handling in SNMP table indices
- Fixed MIB lookup by module:object.indices MIB object with
  InetAddressIPv{4,6} objects being in the index
- Fixed non-translated PDU being retries at CommandGenerator what
  leads to wrong PDU version being sent and even a crash on
  incompatible PDU/SNMP message combination

Revision 4.3.10, released on Oct 06, 2017
-----------------------------------------

- Refactored partial SNMP message decoding to make it less dependent
  on unpublished pyasn1 API features.
- Fix to MibTableRow.setFromName() to keep the input parameter type when
  it propagates to the return value. Before this fix
  ObjectIdentity.prettyPrint() may crash when rendering malformed SNMP
  table indices.
- Fixed NotificationReceiver to include SNMPv1 TRAP Message community
  string into SNMPv2c/v3 TRAP PDU
- Fixed multiple bugs in SNMP table indices rendering, especially
  the InetAddressIPv6 type which was severely broken.
- Fixed crashing Bits.prettyPrint() implementation
- Fixed crashing Bits.clone()/subtype() implementation
- Fixed leaking exceptions bubbling up from the asyncio and Twisted adapters

Revision 4.3.9, released on Jul 26, 2017
----------------------------------------

- Deprecated UsmUserData initialization parameters removed
- Adapted to pyasn1 API changes introduced by release 0.3.1
- Fix to a crash happening on inbound SNMP message having non-initialized
  fields
- Fix to (persistent SNMP engine ID) file writing on Windows

Revision 4.3.8, released on Jun 15, 2017
----------------------------------------

- Security fix to the bug introduced in 4.3.6: msgAuthoritativeEngineTime
  stopped changing over time and was returning the same timestamp (process
  start time). This fix makes it growing as it should.

Revision 4.3.7, released on May 29, 2017
----------------------------------------

* Fixed import error in legacy NotificationOriginator implementation

Revision 4.3.6, released on May 28, 2017
----------------------------------------

- More instrumentation hooks added addressing security failures
  auditing needs.
- SNMP table indices correlation implemented within SMI framework.
  The opaque InetAddress type implemented. INET-ADDRESS-MIB included
  into the distribution.
- SNMP table indices resolution logic made more robust against
  malformed indices.
- Fixes to *lexicographicMode* option documentation to make it
  unambiguous.
- The `ErrorIndication` object is now derived from `Exception` so
  that it could be raised in exceptions.
- The `errorIndication` values produced by various parts of
  SNMP engine unified to be `ErrorIndication` instances. This fixes
  an issue with Twisted.
- Embedded MIB modules rebuilt with the latest pysmi adding previously
  missing attributes like `status`, `description` etc.
- Fixed potential SNMP engine crash on handling incoming message
  at unsupported security level

Revision 4.3.5, released on Mar 24, 2017
----------------------------------------

- The getNext() and getBulk() calls of Twisted interface.
  now support ignoreNonIncreasingOid option.
- TextualConvention is now a new-style class.
- Fix to accidentally reset error-status when building confirmed class
  SNMPv1 PDU.
- Fix to possible infinite recursion in TextualConvention.prettyIn().
- Fixed crash when attempting to report unsupported request/notification
  PDU back to sender.

Revision 4.3.4, released on Mar 01, 2017
----------------------------------------

- Fix to low-level SNMP API example to accommodate changed pyasn1
  SEQUENCE supporting iterator protocol.
- The pyasn1 version dependency bumped (0.2.3), SEQUENCE/SEQUENCE OF
  API calls adjusted to accommodate changed pyasn1 API (in part
  of .setComponentBy*() kw flags).
- Fixed crash on SNMP engine's invalid message counter increment.

Revision 4.3.3, released on Feb 04, 2017
----------------------------------------

- Switched from now unmaintained PyCrypto to PyCryptodome.
- Switched to new-style classes.
- NotificationType now allows additional var-binds specified as
  MIB objects. A side effect of this change is that additional
  var-binds can only be added prior to .resolveMibObjects() is
  run.
- Non-standard (but apparently used by many vendors) Reeder AES192/256
  key localization algorithm implemented and set as default for
  usmAesCfb192Protocol and usmAesCfb256Protocol identifiers.
  Original and more standard implementation can still be used
  with the usmAesBlumenthalCfb192Protocol and
  usmAesBlumenthalCfb192Protocol IDs respectively.
- TextualConvention.prettyOut() improved to produce prettier and
  more SMI-compliant output.
- TextualConvention.prettyIn() implemented to handle DISPLAY-HINT
  based value parsing.
- Fix to NotificationType to make additional var-binds overriding
  MIB objects implicitly included through NOTIFICATION-TYPE OBJECTS.
- Fix to SNMP engine boots counter persistence on Python 3.
- Fix to Pythonized MIBs loading when only .pyc files are
  present (e.g. py2exe/cx_freeze environments).
- Fix broken 3DES key localization and encryption procedures.
- Updated IP address for demo.snmplabs.com in examples.
- Missing index added to bundled RFC1213::atEntry MIB table.
- Twisted integration made Python3 compatible.
- Accommodated ASN.1 SEQUENCE iteration rules change in upcoming pyasn1
  version.
- Author's email changed, copyright extended to 2017.

Revision 4.3.2, released on Feb 12, 2016
----------------------------------------

- Copyright notice added to non-trivial source code files.
- SNMP table row consistency check added. This change may break
  valid SNMP SET operations on tables if RowStatus column is not
  passed at the very end of var-binds.
- All SNMP counters now incremented via '+= 1' rather than 'x = x + 1'
  to simplify their tracking by third-party code.
- Notification originator examples re-pointed to Notification Receiver
  at demo.snmplabs.com.
- Two more execution observer points added: rfc2576.processIncomingMsg
  and rfc3414.processIncomingMsg to give an insight on security modules
  internals.
- TEXTUAL-CONVENTION's DISPLAY-HINT text formatting reworked for better
  performance and encoding accuracy of 'a' and 't' formats.
- WARNING: security fix to USM - extra user entry clone removed on
  incoming message processing. It made USM accepting SNMPv3 TRAPs
  from unknown SNMP engine IDs.
- Fix to snmpInvalidMsgs and snmpUnknownSecurityModels MIB symbols
  import at SNMPv3 MP model.
- Fix to NotificationOriginator to cope with unspecified user callable.
- Fix to OctetString.prettyOut() to pretty-print Python 3 bytes without
  'b' qualifier.
- Fix to better pysmi import errors handling.
- Fix to missing next() in Python 2.5 at pysnmp.hlapi

Revision 4.3.1, released on Nov 12, 2015
----------------------------------------

- Added recursive resolution of ObjectIdentifier values at ObjectType
  by converting it to ObjectIdentity.
- A bunch of convenience shortcuts to rfc1902.ObjectIdentity added
  from rfc1902.ObjectType and rfc1902.NotificationType
  (.addAsn1MibSource(), .addMibSource(), .loadMibs())
- When pretty printing indices at rfc1902.ObjectType, quote only strings.
- SNMP overview and PySNMP hlapi tutorial added to documentation.
- Fix to __doc__ use in setup.py to make -O0 installation mode working.
- Fix to ObjectIdentity->ObjectIdentifier attributes handover
- Fixed crash at oneliner compatibility code on EOM response.
- Fixed crash in hlapi.transport module.
- Fixed OID resolution issues that roots at node 0 and 2.
- Fix to MIB builder to fail gracefully on corrupted MIB package encounter.
- Fix to docs distribution -- now the are Sphinx-buildable out-of-the-box.
- Source code re-linted

Revision 4.3.0, released on Sep 28, 2015
----------------------------------------

- Critical error fixed in key localization procedure for AES192/AES256/3DES
  cyphers. Previous versions might never worked properly in this respect.
- Initial PySMI integration. Original ASN.1 MIBs could now be parsed, stored
  at a local pysnmp MIBs repository and loaded into SNMP Engine. Relevant
  example scripts added. Obsolete libsmi-based scripts removed.
- Major rewrite of native SNMPv3 CommandGenerator and NotificationOriginator
  applications towards the following goals:

  * avoid binding to specific SNMP engine instance to promote single
    SNMP app instance using many SNMP engine instances
  * support two APIs for working with request data: one operates on the
    whole PDU object while the other on PDU contents
  * keep callback context data in stack rather than in stateful application
    cache
  * newly introduced sendVarBinds() method offers a more functional and
    logical signatures.
  * Promote the use of dedicated classes for dealing with OID-value pairs.
    Instances of those classes resemble OBJECT-IDENTITY, OBJECT-TYPE and
    NOTIFICATION-TYPE MIB structures.
  * Oneliner API reworked to become more generic: its LCD configuration
    shortcuts and and var-bindings processing code split off SNMP apps
    classes to stand-alone objects. The whole API also moved up in package
    naming hierarchy and becomes 'pysnmp.hlapi.asyncore' (hlapi is
    apparently an African fish). Old oneliner API remains fully operational
    at its original location.
  * Synchronous oneliner apps redesigned to offer Python generator-based
    API along with a more comprehensive set of accepted parameters.
  * Asyncore-based asynchronous apps reworked to become functions.
  * Twisted API moved entirely into high-level domain to be aligned with
    other high-level APIs. This WILL BREAK backward compatibility for
    those apps that use Twisted API.
  * Keep backward compatibility for all existing major/documented interfaces

- Sphinx documentation added to source code and example scripts. Library
  documentation converted from .html into RsT markup.
- Execution Observer facility implemented to give app an inside view
  of SNMP engine inner workings. This is thought to be a generic
  framework for viewing (and modifying) various internal states
  of pysnmp engine. Previously introduced non-standard APIs (like
  getting peer's transport endpoint which is not suggested in RFCs)
  will be gradually migrated to this new framework.
- Initial support for the asyncio & Trollius frameworks and
  coroutines-based SNMP Applications interfaces added. Both IPv4 and IPv6
  datagram transports are currently supported.
- Original asynsock transport and AsyncsockDispatcher renamed into
  asyncore and AsyncoreDispatcher respectively to provide better hint
  to fellow devs on the underlying transport being used. Backward
  compatibility preserved.
- The asyncore-based transport subsystem extended to support POSIX
  sendmsg()/recvmsg() based socket communication what could be used,
  among other things, in the context of a transparent SNMP proxy
  application. Technically, the following features were brought
  into pysnmp with this update:

  * Sending SNMP packets from a non-local IP address
  * Receiving IP packets for non-local IP addresses
  * Responding to SNMP requests from exactly the same IP address
    the query was sent to. This proves to be useful when listening
    on both primary and secondary IP interfaces.

- Internal oneliner apps configuration cache moved from respective
  apps objects to [a singular] snmpEngine "user context" object.
  That would allow for better cache reuse and allow for a single app
  working with many snmpEngine instances.
- Oneliner GETBULK Command Generator now strips possible excessive OIDs
  off the bottom of returned var-binds table.
- Constraints assignment shortcut added to some base rfc1902 types (Integer,
  Integer32, OctetString, Bits). That formally constitutes ASN.1 sub-typing.
- Built-in debugging is now based on Python logging module.
- Examples on a single Transport Dispatcher use with multiple SnmpEngine
  instances applications added.
- Example script on transport timeout & retries manipulation added.
- Example script explaining incoming message's communityName re-mapping added.
- Broadcast socket option can now be enabled with the .enableBroadcast()
  call for any datagram-based transport (namely, UDP and UDP6).
- AbstractTransportDispatcher's jobStarted() and jobFinished() methods
  now accept optional 'count' parameter which is a way for an app to indicate
  how many responses are expected or have been processed in bulk.
- Example script on SNMP Agents UDP broadcast-based discovery added.
- Oneliner transport object now supports setLocalAddress() method to
  force socket binding to specified local interface.
- New public DgramSocketTransport.getLocalAddress() returns local endpoint
  address underlying BSD socket is currently bound to.
- Passing request details to access control callback at CommandResponder
  reworked towards more robust and simple design with the execution observer
  facility.
- All MIBs rebuilt with pysmi.
- MIB instrumentation example improved to cover table index building facility.
- Handle the case of null writer at Debug printer.
- Do not cache snmpEngineId & snmpAdminString at CommandGenerator to let it
  be reused with many different snmpEngines.
- TRAP PDU agent address evaluation at proto.api made lazy to improve
  startup time.
- Multiple fixes to verify pyasn1 decoder.decode() return to withstand
  broken SNMP messages or its components.
- First attempt made to make some of SNMP Engine settings persistent
  across reboots.
- Make config.delTransport() returning detached transport object. Asyncio
  examples now use this facility to explicitly shutdown transport object.
- Parts of SMIv1 remnant MIBs (RFC1213-MIB, RFC1158-MIB) added to provide
  complete compatibility with SMIv1. Symbols defined in these MIBs only
  present in SMIv1 so they can't be substituted with their SMIv2 analogues.
- MibBuilder.addMibSources() convenience method added.
- The smi.MibBuilder() will now raise more specific exceptions (MibLoadError,
  MibNotFoundError) on MIB loading problems rather than more generic
  SmiError.
- The oneliner's MibVariable MIB lookup subsystem redesigned for more
  generality to mimic OBJECT-TYPE macro capabilities related to SNMP
  PDU handling. The two new classed are ObjectIdentity and ObjectType.
  The ObjectIdentity class additionally supports just a MIB module name
  initializer in which case if resolves into either first or last symbol
  in given MIB. Another option is just a MIB symbol initializer without
  specifying MIB module.
  This new subsystem is moved from the scope of oneliner to more common
  pysnmp.smi.rfc1903 scope to more naturally invoke it from whatever
  part of pysnmp requires MIB services.
- MibBuilder now prepends the contents of environment variables it
  recognizes (PYSNMP_MIB_DIR, PYSNMP_MIB_DIRS, PYSNMP_MIB_PKGS) rather
  than using them instead of its default core MIBs.
- Removed RowStatus default value as it may collide with possible subclass
  constraints.
- A few additional MIB tree management methods added to MibViewController
  to better address ordered nature of MIB tree nodes (namely, getFirst*,
  getLast* family of methods).
- Wheel distribution format now supported.
- Fix to authoritative engine side snmpEngineID discovery procedure:
  respond with notInTimeWindows rather then with unsupportedSecurityLevel
  at time synchronization phase.
- Fix to rfc1902.Bits type to make it accepting hex and binary initializers,
  cope with missing bits identifiers at prettyPrint().
- Memory leak fixed in CommandForwarder examples.
- Fix to BULK CommandGenerator to use the same nonRepeaters OIDs across
  multiple GETBULK iterations so returned table for nonRepeaters columns
  would hold the same var-bind.
- Fix to CommandGenerator to make sendRequestHandle persistent across
  multiple iterations of GETNEXT/GETBULK queries.
- Fix to sendNotification() error handling at NotificationOriginator.
- Fix to preserve possible 'fixed length' setting atrfc1902.OctetString
  on clone()'ing and subtype()'ing.
- Fix to rfc1902.OctetString & Bits to base them on OctetString class to
  make the 'fixed length' property working.
- Fix to .clone() method of rfc1902.Bits class to make its signature
  matching the rest of classes. This may broke code which used to pass
  namedValue parameter positionally rather than binding it by name.
- Fix to PDU translation service (proto.proxy.rfc2576) to make it
  initializing errorIndex & errorStatus components of the resulting PDU.
- Fix to MsgAndPduDispatcher.sendPdu() to clean up request queue on
  pysnmp-level processing failure.
- Fix to SNMPv1/v2c message processing subsystem to make it serving
  unique PDU request-id's in both outgoing and incoming confirmed
  and response PDU types. Duplicate request-id's in unrelated PDUs may
  cause cache errors otherwise.
- Fix to licensing terms of multiple twisted backend modules to make
  the whole pysnmp package licensed under BSD 2-Clause license. This
  change has been explicitly permitted by the original modules authors.
- Fix to asyncore-based transport not to use asyncore's cheap inheritance
  from socket object what caused warnings.
- Fix at NotificationOriginator to make is using MibInstrumentationController
  when expanding Notification OBJECTS into Managed Objects Instances.
- Missing wrongLength and wrongEncoding SMI errors added.
- Fix to file descriptor leak at MibBuilder.
- Fix to rfc2576.v2ToV1() to ignore impossible errorStatus.
- Fix to rfc2576.v1ToV2() to reset ErrorStatus==noSuchName on proxying.
- Fix to smi.builder to explicitly fail on any MIB file access error
  (but ENOENT) and raise IOError uniformly on any directory/egg access
  failure.
- Fix to infinite loop at config.delV3User().

Revision 4.2.5, released on Oct 02, 2013
----------------------------------------

- License updated to vanilla BSD 2-Clause to ease package use
  (http://opensource.org/licenses/BSD-2-Clause).
- A dozen of lightweight Twisted-based example scripts replaced more
  complex example implementations used previously.
- SNMP Proxy example apps separated into a larger set of more specialized
  ones.
- Most of Command Generator examples re-pointed to a live SNMP Agent
  at demo.snmplabs.com to ease experimentation and adoption.
- Multithreaded oneliner CommandGenerator example added.
- Packet-level SNMP API (pysnmp.proto.api) getErrorIndex() method can now
  be instructed to ignore portentially malformed errorIndex SNMP packet
  value what sometimes happens with buggy SNMP implementations.
- Standard SNMP Apps and built-in proxy now ignores malformed errorIndex
  value.
- Built-in logging now includes timestamps.
- Multi-lingual capabilities of all CommandGenerator & NotificationOriginator
  apps re-worked and improved. For instance it is now it's possible to run
  getBulk() against a SNMPv1 Agent invoking built-in SNMP Proxy behind the
  scene.
- The $PYSNMP_MIB_DIR & $PYSNMP_MIB_DIRS & $PYSNMP_MIB_PKGS path separator
  made platform-specific.
- Change to rfc2576.v1tov2() logic: errorStatus = noSuchName is now
  translated into rfc1905.noSuchObject exception value for *all* var-bindings
  at once. Although RFC2576 does not suggest error-status -> v2c exception
  translation, historically pysnmp used to perform it for a long time so we
  can't easily stop doing that.
- Exception re-raising improved at MibInstrumController.flipFlopFsm() and
  asynsock/twisted dispatchers so that original traceback is preserved.
- A single instance of transport dispatcher can now serve multiple
  receivers (identified by IDs) chosen by a public data routing method.
- SnmpEngine.[un]registerTransportDispatcher() methods now accept optional
  receiver ID token to be used by transport dispatcher's data router. This
  allows for multiple SNMP engines registration with a single transport
  dispatcher.
- Distribute is gone, switched to setuptools completely.
- The snmpCommunityTable row selection improved to follow RFC2576, clause
  5.2.1.
- Asyncore-based dispatcher attempts to use poll() whenever available
  on the platform. It would help handling a really large number (>1024)
  of file descriptors.
- AsynCommandGenerator.makeReadVarBinds() generalized into a new
  makeVarBinds() method which replaces somewhat redundant code at setCmd()
  and AsynNotificationOriginator.sendNotification().
- AsynCommandGenerator.uncfgCmdGen() & AsynNotificationOriginator.uncfgCmdGen()
  methods now accept optional authData parameter to remove specific entries
  from LCD. This can be useful for modifying security parameters for
  specific securityName.
- SNMP credentials management reworked to separate userName from securityName
  in snmpCommunityEntry and usmUserEntry tables. Changes made to addV1System(),
  addV3User() functions as well as to their oneliner's wrappers.
- The contextEngineId parameter of config.addV3User() and auth.UsmUserData()
  renamed into securityEngineId as it's semantically correct
- Oneliner UsmUserData() and CommunityData() classes now support clone()'ing
  to facilitate authentication data management in user applications.
- Oneliner transport target classes now support the getTransportInfo()
  method that returns network addresses used on protocol level.
- Oneliner CommandGenerator.getNext() & .getBulk() methods now support the
  maxCalls kwarg to limit the maximum number of iterations to perform.
- The config.addSocketTransport() helper renamed into config.addTransport()
  and improved by automatically instantiating compatible TransportDispatcher
  making it dispatcher-agnostic. As an additional bonus, application may not
  call registerTransportDispatcher() as it would be called by addTransport().
- The SnmpV3MessageProcessingModel.getPeerEngineInfo() method is implemented
  to communicate discovered peer SNMP engine information to SNMP apps what
  can be used for fine usmUserTable configuration.
- AsynNotificationOriginator.cfgCmdGen() does not take into account
  securityModel & securityLevel when reducing LCD access via addTrapUser().
  This improves LCD consistency on sparse add/del operations but also
  does not let you to configure different securityModels per securityname
  at VACM though the cfgCmdGen() wrapper.
- MIB builder traceback formatting and reporting improved.
- SNMP Engine object now has a snmpEngineID attribute exposed.
- Fix to inet_ntop()/inet_pton() support on Windows at TRANSPORT-ADDRESS-MIB.
- Fix to usmUserSecurityName table column implementation -- automatic value
  generation from index value removed.
- Fix and significant logic rework of snmpCommunityTable to make it working
  in both Generator and Responder modes and better follow RFC2576
  requirements on sequential entries lookup and selection. As a side effect,
  untagged snmpCommunityTable entries will *not* match tagged
  snmpTargetAddrTable entries and vice versa.
- Fix to Twisted-based NotificationOriginator to make it serving INFORMs again.
- Fix to rfc2576.v1tov2() logic: errorStatus = noSuchName is now translated
  into rfc1905.noSuchObject exception value for *all* var-bindings. Although
  this is not mentioned in RFC, it looks as a more consistent approach.
- Fix of rounding error to base I/O dispatcher's next timer call calculation.
- Explicit twisted dispatcher's timer resolution (of 1 sec) removed to make
  use of global default of 0.5 sec.
- Fix to twisted/udp non-default local endpoint binding features. Common
  socket ('host', port) notation is now supported.
- Fix to Twisted-based transport to make it closing UDP port / UNIX pipe
  on shutdown.
- Fix to Twisted-based dispatcher not to close transport on unregistration
  at dispatcher as transports can potentially be reused elsewhere.
- Fix to asyncore-based transport to work only with AsynsockDispatcher's
  socket map and not to touch default asyncore's one. The latter have caused
  dispatcher/transport restarting issues.
- The delV3User() function improved to drop all rows from USM table that
  were cloned from the target one.
- Fix to exceptions handling at MsgAndPduDispatcher.sendPdu() to avoid
  sendPduHandle miss (followed by system crash) on cache expiration run.
- Break cyclic references at CommandResponder and NotificationReceiver apps
  through close() method.
- Fix to octet string typing at 3DES codec (used to throw an exception).
- Fix to SnmpAdminString, SnmpTagList, SnmpTagValue types to make them
  supporting UTF-8 initializers.
- Fix to v1/v2c message processing module which used to refer to a
  bogus stateReference in some cases what causes SNMP engine crashes.
- Fix to IPv6 transport to zero ZoneID, FlowID and ScopeID components
  sometimes coming along with incoming packet.
- Fix to SNMPv1 MP module to pass stateReference to registered app on
  unconfirmed notifications reception (to let NotificationReceiver
  Apps browsing request details).
  (transport information at the moment) at SNMP engine.
- Asyncsock sockets now configured with SO_REUSEADDR option to fix possible
  Windows error 10048.
- Gracefully handle malformed SnmpEngineID at USM coming from SNMPv3 header.
- Typos fixed in error-status constants at CommandResponder
- Missing import added to oneliner auth module.
- Cosmetic changes to v3arch example scripts.

Revision 4.2.4, released on Jan 30, 2013
----------------------------------------

- SNMPv3 high-level and native API examples reworked and extended to cover
  many use cases.
- The missing functionality of NOTIFICATION-TYPE objects being looked up
  at local Management Instrumentation and attached to TRAP/INFORM message
  by Notification Originator is now fully implemented.
- The missing functionality of passing Response PDU contents of INFORM
  request is now implemented at Notification Originator app. The return
  value of NotificationOriginator.sendNotification is now a composite object
  that includes errorStatus, errorIndex and varBinds.
- The missing functionality of passing lookupNames & lookupValues params
  to Notification Originator is now implemented. It may make sense for
  INFORMs.
- The missing functionality of passing contextName to oneliner
  version of NotificationOriginator.sendNotification is now implemented.
- Oneliner example apps now include cases where non-default SNMP
  ContextEngineId/ContextName/SecurityEngineId is used.
- The contextName parameter of SnmpContext.getMibInstrum made optional.
- AbstractMibInstrumController class added as a base class for all possible
  kinds of Management Instrumentation controllers.
- Report package version on debugging code initialization.
- MibInstrumController.getMibBuilder() added.
- I/O sockets buffer sizes made configurable, minimum default is now
  forced to be no less than 2**17 (to fit two huge datagrams).
- Catch possible exceptions on pyasn1 encoder invocation.
- VACM modules converted from a function into an object to let it keep
  state (caches) in the future.
- Unnecessary MibSource explicit initialization calls removed at MibBuilder.
- Example configuration for Net-SNMP's snmptrapd added.
- Cast additionalVarBinds into ObjectIdentifier type at
  NotificationOriginator.sendNotification()
- Standard SNMPv3 Apps hardened to catch protocol-related exceptions and
  report them as errorIndication's.
- Catch and mute possible failure of getsockname(), that seems to happen
  on Windows only so far.
- Memory leak fixed at oneliner cache of already configured targets.
- Fixes to at AsynNotificationOriginator.sendNotification() to make
  a) the notificationType param mandatory b)t e varBinds param really
  optional
- Fixes to ContextEngineId/ContextName support at the oneliner API: now
  both items should be passed to request PDU through Cmd() request
  initiation method, the items of authData object should be used only for
  LCD configuration.
- Fix to MibVariable handling of the MIB, <empty-symbol> initializers.
- Fix to outgoing queue processing order at socket transport. Now
  it's a FIFO discipline rather than LIFO.
- Fix to NotificationOriginator's additionalVarBinds parameter - it is
  not mandatory anymore with the oneliner API. Also additionalVarBinds
  defaulted value changed from None to () meaning no var-binds.
- Attempt to convert Windows style EOL into UNIX ones in MIB source
  modules appeared to be unnecessary and even destructive to modules
  data in some cases. So the conversion code removed altogether.
- Fix to isAccessAllowed() error handling at NotificationOriginator. System
  used to crash on access denied condition.
- Fix to NotificationOriginator to make it use system uptime and trap OID
  values from SNMP engine's instrumentation rather then from SNMP context.
- Fix a couple of bugs at MibTable* logic involved for table instances
  creation.
- Fix to Management Instrumentation code to handle cases of non-initialized
  or not-compliant-to-constraints Managed Objects Instances.
- Fix to Management Instrumentation code to make table row removal through
  SNMP working again. Wrong method (instumClone) was probed at terminal
  MIB nodes values instead of the right one (setValue).

Revision 4.2.3, released on Sep 06, 2012
----------------------------------------

- SECURITY FIX: USM subsystem did not verify securityLevel of a request
  to an authoritative SNMP engine against auth/priv protocols
  configured for the user in question. That allowed unauthenticated/unciphered
  access to pysnmp-based Agent even if USM user is configured to provide one.
- Oneliner [Asyn]CommandGenerator now supports optional keyword args
  lookupNames, lookupValues that enable response OID / value looked up at
  MIB and reported as a MibVariable container object carrying relevant
  MIB info.
- Oneliner [Asyn]CommandGenerator now supports symbolic MIB object names to be
  passed within a MibVariable container object which would do a deferred
  MIB lookup for name resolution. This is a new and preferred API which
  obsoletes the tuple-based one (it is still suppored though).
- Oneliner CommandGenerator's class attributes lexicographicMode, maxRows
  and ignoreNonIncreasingOid moved to optional keyword args of nextGen()
  and bulkGen() methods.
- IPv6/UDP and Local Domain Socket transport interfaces added to the
  oneliner API.
- Mib Instrumentation subsystem re-worked to replace excessive
  MibNode's smiCreate()/smiWrite()/smiDestroy() methods with
  MibScalarInstance's getValue()/setValue()
- MibTree.readTest[Get]Next() reworked to be called uniformely so
  user could tap on these methods at any level of the MIB tree.
- MibTableColumn.getNextNodeWithValue() unpublished API method obsoleted
  and removed for clarity.
- Hex dumps of binary parts of the protocol added to ease system
  operations analysis.
- SnmpEngineId autogeneration does not call DNS resolver but uses
  local hostname not to depend upon local IP availability and performance.
- Example apps reworked, additional SNMPv3 auth/priv protocols and transports
  added.
- Package version is now available as __init__.__version__ and it is
  in-sync with distutils.
- Package meta-information updated.
- The __init__.py's made non-empty (rumors are that they may be optimized
  out by package managers).
- Multiple fixes to UNIX domain socket transport to make it fully
  operational again.
- Use sysUpTime value whenever it is included in Notification PDU, otheriwese
  resort to SNMP engine uptime reading.
- SNMPv2c Message is now defined in rfc1901.py what matches standard
  definition.
- Types defined within SNMPv1/v2c data structures (rfc1157.py/rfc1905.py)
  moved to module scope to become accessible by wrapper routines
  (v1.py/v2c.py). This is used for setting strictly typed default values
  to corresponding SNMP data structures.
- The obsolete and unpublished MibInstrumController.readVarsFast() method
  removed for API clarity.
- MibBuilder now distinguishes case of MIB modules filenames even if
  underlying OS does not.
- LCD configuration caching is implemented at pysnmp.entity.rfc3413.config
  that improves performance of repetitive calls by 10% and might hugely
  improve NotificationOriginator's performance when working on a large
  number of targets.
- A caching maps implemented at rfc2576 subsystem to speed-up communityName
  to/from securityName resolution. The also makes transport tags processing
  better compliant to the standard.
- Community and Transport tags processing changed at the oneliner interface
  to make the whole mechanism more compliant with the standard. Most
  importantly, it is now possible to tag authentication and transport
  information separately.
- The NoSuchInstanceError exception class is no more inherits from
  NoSuchObjectError to make class hierarchy closer to SNMP specification
  which states that these errors are separate and independent.
- The Next & BulkCommandGenerator's split onto single-run and iterative
  impementations. The former just process a single interaction and complete
  while the latter run as many interactions as user callback function
  indicates to.
- The pysnmp.entity.rfc3413.mibvar module is now obsolete by
  pysnmp.entity.rfc3413.oneliner.mibvar featuring basically the same
  features but within a stateful, dedicated object.
- Auth & target configuration container classes moved to their separate
  modules at oneliner API.
- The notificationType parameter of AsynNotificationOriginator.sendNotification
  made defaulted to reflect its optional nature.
- Oneliner UsmUserData, UdpTransportTarget, Udp6TransportTarget instances
  are not hashable anymore as they are intended to act more like a data
  structure than object.
- Built-in debugger now supports negating debugging categories.
- An async/getgen.py example script added.
- Fix to MIB data reading routine to make it working with possible
  Windows end-of-line's.
- Fix to CommandGenerator's SNMPv3 engine autodiscovery algorithm
  when retryCount is administratively set to 0.
- Fix to Notification Originator to make it communicating a single
  sendPduHandle to an application even when multiple INFORMs are triggered
  and processed by a single call by way of transport tagging feature.
- Fix to rfc2576:processIncomingMessage() to take SecurityModel into account
  when lookup up SecurityName by CommunityName. This allows mixed SNMPv1/v2c
  communication with the same target.
- Fix to internal MessageProcessing and SecurityModel timers so they become
  dependant on system timer resolution.
- Fix to v1.PDUAPI.setDefaults() method that used to set wrongly typed
  time-stamp component.
- Fix to IPv6 address handling to prevent system from crashing whilst
  running Python3.
- Fix to SNMPv2 exception objects translation into SNMPv1 PDU and NEXT
  OIDs calculation.
- Fix to MibTree class to properly report noSuchObject & noSuchInstance
  SNMP special values.
- Fix to libsmi2pysnmp tool to make it working again in Python < 2.7
- Fix to exception handling at decodeMessageVersion() caller to prevent
  ASN.1 parsing errors crashing the whole app.
- Fix to GenericTrap type processing at rfc2576:v1Tov2c() which used to
  crash the whole SNMP engine.
- Fix to [possibly uninizilaized] pyasn1 objects printouts at
  MibInstrumController.__indexMib()
- Fix to maxSizeResponseScopedPDU calculation at rfc3414/service.py.
- Dedicated 'withmib' example set is obsolete and removed.
- Another SNMP proxy example app added (1to3.py).
- Fix to MIB modules loading code to make it using __import__() properly.
  This also makes pysnmp working again with Python 3.3rc0.
- Typo fix to snmpInASNParseErrs MIB instance object.
- Typo fix to errind.EngineIdMismatch class and its instance.

Revision 4.2.2, released on Apr 21, 2012
----------------------------------------

- Oneliner CommandGenerator can now limit the number of SNMP table
  rows returned by nextCmd()/bulkCmd() methods.
- Oneliner CommunityData configuration object can now be initialized
  with community name only, security name will be chosen automatically.
- Oneliner LCD configuration routines reworked towards clarity. The
  side-effect of this change is that repetitive oneliner call with the same
  securityName and different configuration options will only honor
  the first settings. Previous implementation would override older settings.
- Transport dispatcher now provides its own time expressed in
  fractions of second. SNMP engine uses this notion of time for
  handling requests timeout to make packet flow time bound
  to async I/O core operations rather than to real time.
- The libsmi2pysnmp tool improved to handle incomplete SMI v1->v2
  conversion performed by smidump. The remaining core SMIv1 modules
  excluded from the core MIB set.
- The pyasn1 constraint and enumeration objects put into ASN1-*
  MIB modules what appears to be more in-line with SMI. Existing
  MIB modules as well as libsmi2pysnmp tool corrected accordingly.
- SMIv1 MIB modules (including RFC1155 and RFC1213) were moved to
  pysnmp-mibs as pysnmp is SMIv2-based.
- The MibBuilder.importSymbols() now takes optional kwargs and
  push them into MIB modules globals(). This is to facilitate
  passing user infomation, such as DB connection handler, to MIB
  module namespace so it could be used by ManagedObjects implementations.
- When running on Python3, SMI will re-raise exceptions with the original
  traceback for easier diagnostics.
- Out of PYTHONPATH MIB paths now supported.
- Added pyasn1 decoder failures diagnistics in debug mode.
- Fix to non-MT-safe class attributes at SNMPv3 MP & SEC modules.
- Fix to ContextName handling in bytes form whilst running Python3. Data
  mismatch error would return otherwise.
- Fix to SNMPv3 MP peer engine ID discovery not to learn and use
  user-specified ContextEngineId.
- Fix to socket.error processing at Py3 on Windows.
- Fix to oneliner GETNEXT/GETBULK implementation to properly support
  ignoreNonIncreasingOIDs option.
- Fix to setEndOfMibError()/setNoSuchInstanceError() at v1 PDU not to
  loose errorIndex.
- Fix to api.v2c.getVarBindTable() to ignore possible non-rectangular GETBULK
  response tables.
- Fix to oneliner getnext/getbulk response table rectangulation procedure
  to gracefully handle an empty column condition.
- Fix to legacy MibBuilder.getMibPath() to prevent it from missing
  .egg-based components in path.
- Fix to oneliner configuration routine that used to implicitly
  tag SNMPv1/v2c auth and transport LCD rows what resulted in
  huge delays when processing incoming messages with large number
  of peers configured.
- Fix to UDP6 transport handling at rfc2576 security module.
- Fix to SnmpEngineID value autogeneration (used to fail on Mac).
- SNMPv2-SMI.ObjectType.__repr__() fixed to do a repr() on its components.
- All SNMPv2-SMI.MibNode-based objects, once exported to a mibBuilder, will
  carry an embedded label symbol.
- Exlicit repr() calls replaced with '%r'
- Fix to error processing at GETNEXT & GETBULK apps response handlers.
- Fix to libsmi2pysnmp to make it supporting long (256+) list of function
  params.
- Fix to libsmi2pysnmp to support inheritance of MIB types.

Revision 4.2.1, released on Nov 07, 2011
----------------------------------------

- Support string OIDs at one-liner API.
- Code quality of libsmi2pysnmp tool improved, MIBs re-built.
- SNMP-PROXY-MIB & SNMP-USER-BASED-SM-3DES-MIB added
- v1arch bulkgen.py example added
- Major overhawl for Python 2.4 -- 3.2 compatibility:

  + get rid of old-style types
  + drop string module usage
  + switch to rich comparation
  + drop explicit long integer type use
  + map()/filter() replaced with list comprehension
  + apply() replaced with var-args
  + dictionary operations made 2K/3K compatible
  + division operator made 2K/3K compatible
  + sorting function now operates on key
  + iterators returned by some funcs in py3k converted to lists
  + exception syntax made 2K/3K compatible
  + tuple function arguments resolved to scalars to become py3k compatible
  + BER octetstream is now of type bytes (Py3k) or still string (Py2k)

Revision 4.1.16d, released on Sep 22, 2011
------------------------------------------

- Fix to SNMPv1 Trap PDU agentAddress setter shortcut method.

Revision 4.1.16c, released on Aug 14, 2011
------------------------------------------

- Missing module import fixed in privacy subsystem

Revision 4.1.16b, released on Aug 13, 2011
------------------------------------------

- Oneliner CommandGenerator can now optionally ignore non-increasing OIDs.
- Default CommandResponder now skips non-compliant (Counter64) values
  when responding to a v1 Manager.
- Fix to state information handling at CommandResponder app.
- Fix to Twisted reactor shutdown condition.
- Fix to distutils dependencies syntax.

Revision 4.1.16a, released on Mar 17, 2011
------------------------------------------

- Extended Security Options (3DESEDE, AES192, AES256) privacy
  protocols implemented.
- The error-indication codes moved from literals to objects for reliability
  and clarity
- Fix to v1.TrapPDUAPI.getVarBinds() to address PDU component at the right
  position.
- Fix to rfc1902.Bits initialization from named bits sequence.
- Fix to MIB builder by-extension module filtering code to cope with .pyw
  files.
- Internal caches structure improved.
- Sync versions of oneliner apps split off async implementation for clarity.
- Randomize initial in various numeric sequences.
- MsgAndPduDsp expectResponse parameters passing reworked.
- GetNext/GetBulk response processing logic moved to getNextVarBinds()
- Changes towards performance improvement:

  + all dict.has_key() & dict.get() invocations replaced with modern syntax
    (this breaks compatibility with Python 2.1 and older).
  + introduce the MibInstrumControlle.readVarsFast() method (which skips
    the "testing" phase of MIB value readin) for dealing with internal
    configuration (LCD).
  + default debug.logger is now just a zero value instead of an object
    what saves big on frequent calls
  + SNMPv2-SMI columnar indices <-> index values conversion code optimized.
  + pre-compute and re-use some of ASN.1 structures.
  + avoid setting PDU defaults to save on unnecessary initialization.
  + skip ASN.1 types verification where possible.
  + at oneliner Command Generator, avoid looking up pure OID arguments
    at MIB as it's pointless but takes time.
  + cache MIB columnar objects instance ID <-> symbolic index representation
    mapping

Revision 4.1.15a, released on Dec 13, 2010
------------------------------------------

- SNMP Proxy example added.
- End-of-MIB condition detection reworked what caused backward
  incompatibility at v1arch GETNEXT API. Previous pysnmp versions
  used value = None in var-binds as returned by getVarBindTable()
  API method. This version uses rfc1905 exception values (v2c/v3)
  or pyasn1 Null (v1).
  Built-in GETNEXT/GETBULK apps now do not require user to track
  end-of-mib conditions anymore -- this is now done automatically.
- CommandResponder API now supports async mode of operation.
- SNMP exception values now exported from rfc1905 module, and made
  pretty printable.
- Lexicographic walking mode is now supported at oneliner CommandGenerator.
- ContextEngineId&ContextName parameters passing implemented at
  v3arch oneliner API.
- Multiple instances of the same transport domain now supported.
- Initial snmpEngineId value generation improved not to accidentally
  collide within an administrative domain.
- MibTableColumn instances now build value-to-column-instance map
  to speedup by-value search.
- SNMPv2-CONF::AgentCapabilities macro implemented.
- The libsmi2pysnmp tool handles some more MACROs.
- Void access control module implemented to let apps disabling [default] VACM.
- Allow standard SNMP apps to choose access control method to use.
- Twisted-based CommandResponder example added.
- Fix/rework of Twisted GETNEXT/BULK CommandGenerator callback API to
  make it simpler and uniform with other CommandGenerators
- Fix to SNMPv3 security module to store peer SNMP engine timeline
  only if taken from an authenticated message. Prior to this fix
  SNMP engine was not been protected from spoofing.
- Fix to $SMIPATH initialization at build-pysnmp-mib.
- Fix to maxSizeResponseScopedPDU calculation.
- Fix to Next/Bulk CommandGenerators to catch a non-increasing OID
  error condition (what prevents looping).
- Fix to Opaque value tagging at rfc1155.Opaque type.
- Fix to handle (fail gracefully) zero-length user password.
- Fix to SNMP error propagation at Twisted driver (SF tracker ID #3054505).
- Fix to Agent-role snmpEngineId discovery procedure that allows
  authenticated ReportPDU generation.
- Fix to SNMPv1 PDU handling at CommandResponder & NotificationReceiver
  apps.
- Fix to CommandResponder app to skip Counter64 SMI values when responding
  to SNMPv1 Manager.
- Fix to protocol translator code (rfc2576) to handle Counter64 type
  in v2c-to-v1 PDU translation.
- Fix to non-response var-binds translation in rfc2576.v2ToV1().
- Fix to wrong exceptions used in pysnmp/entity modules.
- Fix to noauth/nopriv security module so that it would not crash SNMP
  engine if called accidentally.
- Fix to CommandResponder not to return out-of-range errorIndex along
  with genErr
- Fix to GETBULK CommandResponder to do a by-column MIB walk, not by-raw.
- Fix to getVarBindTable() API function logic.
- Fix to example Manager scripts to use errorIndex when available.
- Fix to dummy encryptData()/decryptData() API
- Fix to oneliner GETBULK table collection code to make it stripping
  uneven rows off table tail.

Revision 4.1.14a, released on Jul 15, 2010
------------------------------------------

- Fix to maxSizeResponseScopedPDU calculation at USM security module: now
  more precise and robust against screwed values on input.
- Fix to MIB loading logic that used to load same-name modules at
  disticts search paths on each loadModules() call.
- Fix to AsynsockDispatcher.runDispatcher() to make use of optional
  non-default select() timeout value.
- AbstractTransportDispatcher now allows user application registering
  multiple timer callbacks each with dedicated call period.
- Asynsock mainloop default idle period reduced to 0.5 sec for better
  timer resolution.
- Fix to SNMPv1->SNMPv2c error status handling at proxy module. This
  defect may have caused an infinite loop on a multiple var-bind
  SNMPv1 GetNext operation.
- Fix to contextName processing at config.addV1System -- typo rendered
  passed contextName not committed into LCD.
- Fix to unknown ContextName exception handling at CommandResponder App.
- config.addVacmUser() now accepts an optional contextName what makes
  it usable for configuring multiple contextName-bound bases of Managed
  Objects to SnmpEngine.
- MP pending states cache management re-worked so that SNMP engine will
  now handle an unlimited number of pending request/responses.
- Fix to SNMP discovery procedure: include ContentName in SNMP discovery
  messaging.
- Many fixes to AES crypto code that makes it actually working.
- Fix to SNMPv2-SMI createUndo operations.
- Fix to INFORM sending error handling at oneliner.
- Fix to mismatched response PDU handling at CommandGenerator application.
- Debug category 'app' (for Application) added to facilitate
  Standard SNMP Applications debugging.
- The retryCount semantic of CommandGenerator application changed to include
  sole retries and do not include initial request. Thus, retryCount=1 will
  now send up to two packets, not just one as it used to be.
- Debugging printout now escapes non-printable characters.

Revision 4.1.13a, released on Feb 09, 2010
------------------------------------------

- UDP over IPv6 transport implemented.
- Fix to MIB tree walking code that used to fail on table columns where
  indices have identical leading parts.
- SNMPv1/v2c snmpCommunityTransportTag-based imcoming message filtering
  implemented (rfc2576).

Revision 4.1.12a, released on Dec 03, 2009
------------------------------------------

- API versioning retired (pysnmp.v4 -> pysnmp).
- MIB loading mechanics re-designed to allow ZIP import.
- MIB loader supports code objects (py[co])
- Installer now uses setuptools for package management whenever available.
- The libsmi2pysnmp tool improved to build constraints of more than
  256 items (Python has a limit on the number of function params).
- Missing SNMPTrap PDU API implemented at proto.api.v2c, RFC2576 proxy
  code reworked.
- Fix to sysUpTime OID at SNMPv2 TRAP PDU.

Revision 4.1.11a, released on Aug 21, 2009
------------------------------------------

- Twisted integration implemented.
- Attempt to use hashlib whenever available.
- Fix to oneliner Manager code on < Python 2.4.
- Let NotificationReceiver and CommandResponder Apps browsing request details
  (transport information at the moment) at SNMP engine.
- Fix to config.addV1System() to allow multiple systems to co-exist in LCD.
- Fix to wrongly succeeding user-parameters-by-community-name searching code
  in rfc2576 processIncomingMsg() method.
- Do sanity checking on PYSNMP_MODULE_ID, Groups and Notifications in
  libsmi2pysnmp (SF bug #2122489).
- Fix to oneliner Notification Originator that sometimes used to send multiple
  requests at once.
- Oneliners LCD names generation code reworked to avoid accidental clashes.
- Fix and re-work of sysUpTime value management in LCD.
- Fix to pending inform request data caching in mpmod/rfc2576.py -- previous
  code led to cache data corruption on multple outstanding requests.
- In SMI configuration wrapper functions, catch access to non-configured
  entries and raise an exception.
- Allow multuple callback timer functions in all transport dispatchers.
- Fix to libsmi2pysnmp code to preserve more underscored object names and
  to guess the right type between indistinguishable ObjectGroup &
  NotificationGroup
- Fix to MibScalarInstance value setting logic - previous code failed
  when modifying the same OID multiple times within a single SET operation.
- Minor usability improvements to tools/build-pysnmp-mib.
- Made MIB objects unexport feature operational.

Revision 4.1.10a, released on May 25, 2008
------------------------------------------

- Internal MIB indexing method __indexMib() unmangled to facilitate
  setting up mutex there for sharing MIB stuff between threads.
- Fixed broken IpAddress value handling in SET operation.
- Broken MibBuilder.unloadModules() method now works.
- Use getLabel() SMI object method when building MIB tree (in builder.py)
  in addition to direct attribute access for clearer object protocol.
- The MIB building tools updated to match significantly improved
  smidump tool (libsmi version > 0.4.5).
- Made libsmi2pysnmp tool optionally building MIB text fields into pysnmp
  MIB code (enabled by default) and MibBuilder conditionally loading them
  up (disabled by default).
- SnmpEngine and MsgAndPduDispatcher constructors now optionally
  take msgAndPduDspr and mibInstrumController class instances
  respectively to facilitate these objects sharing within a process.
- Unique integers, for various parts of the system, are now generated
  by a nextid.py module. This fixes possible issues with duplicate
  request IDs and handlers.
- Built-in MIBs re-generated to include text fields.

Revision 4.1.9a, released on Nov 28, 2007
-----------------------------------------

- UNSTABLE ALPHA RELEASE.
- At onliner CommandGenerator, close transport on destruction to
  prevent socket leak. Implicit async transports registration at
  default asyncore's socket map has been disabled to avoid side
  effects.
- Fix to rfc2576.v1ToV2c() PDU converter to perform noSuchName error code
  translation.
- Fixes to Notification PDU conversion code at rfc2576 in part of
  snmpTrapOID handling.
- Fix to nonRepeaters object use as sequence slicer (must be int) at
  cmdrsp.CommandResponderApplication
- Make AsynsockDispatcher using its own socket map by default for
  threading safety. This will break asyncore apps that rely on pysnmp
  sharing the same socket map with them. A solution would  be to either
  set asyncore map to pysnmp (AsynsockDispatcher.setSocketMap()) or pass
  pysnmp map (AsynsockDispatcher.getSocketMap()) to asyncore.
- Fix to response timeout roundup bug at CommandGenerator and
  NotificationOriginator code.
- Oneline configuration classes made hashable to prevent memory leaks
  when committing them into CommandGenerator/NotificationOriginator
  internal repository.
- Security information is now released properly in all MP modules.
  This might fix a significant memory leak.
- Typo fix to rfc3411 confirmed class PDU members.

Revision 4.1.8a, released on Aug 14, 2007
-----------------------------------------

- UNSTABLE ALPHA RELEASE.
- SMI/dispatcher timeout conversion multiplier is actually 100 (1/100 sec)
  rather than 1/1000. This fix affects timeouts specified through SMI.
- __repr__() implemented for UdpTransportTarget, CommunityData, UsmUserData
  in oneliner module.
- Automatically initialize table index values on table management
  operations (SF bug ID #1671989).
- Fix to carrier code: ignore BADFD socket error as it may happen upon
  FD closure on n-1 select() event.
- Fix to MibBuilder.setMibPath() to preserve previously loaded modules
  intact. Otherwise loadModules() called after setMibPath() might fail
  with 'MIB file not found in search path' exception.
- Fix to oneliner classes that now invoke unconfiguration methods on
  destruction. This might have caused memory leaks.
- Automatically initialize SNMP-USER-BASED-SM-MIB::UsmUserSecurityName
  columnar object instance on creation, as stated in DESCRIPTION (SF
  tracker ID #1620392).
- Fix to USM timeframe arithmetics (SF bug #1649032).
- VACM shortcuts merged into universal add/delVacmUser() to let notifications
  and requests to co-exist for the same user.
- At oneliners, build LCD tables keys from a hashed mix of input parameters
  to make sure these automatic entries won't interfere or exceed constraints
  on keys values.
- Made use of notificationType parameter of the sendNotification method
  in NotificationOriginator applications. This parameter used to be
  ignored in the past. Note, that previously used (and ignored) syntax
  has been changed in an incompatible way.
- Allow plain Python values in setCmd() and sendNotification()
  methods in CommandGenerator and NotificationOriginator applications
  respectively.
- Multi-target oneliner API-based example script added.
- Ignore more socket errors in datagram-type async socket code.
- AES cipher now supported (rfc3826).
- Fix to messed up tagIDs of noSuchInstance and noSuchObject types.
- SET Command Responder fixed to obscure access to non-existing variables
  by returning notWritable error (SF bug #1764839).
- AsynsockDispatcher.setSocketMap() method added to facilitate pysnmp
  transport integration into third-party asyncore-based applications.
- Fix to errorIndex generation at CommandResponder application, the value
  should be a one-based.

Revision 4.1.7a, released on Feb 19, 2007
-----------------------------------------

- UNSTABLE ALPHA RELEASE.
- Low-level debugging facility implemented.
- Support UdpTransportTarget timeout and retries parameters in oneliner API.
- Fix to snmpTrapOID construction at ...proxy.rfc2576.v1ToV2()
  function.
- Fix to MibViewController.getNodeName() to take MIB module name
  into account (SF bug #1505847).
- Do explicit check for Counter32,Unsigned32,TimeTicks,Counter64 value types
  in MibTableRow index conversion and in TextualConvention.prettyPrint()
  methods (SF bug #1506341). Handle Bits in indices as RFC2578 suggests.
- Apply read-create column status to libsmi2pysnmp-generated code
  whenever MIB text specifies that (SF bug #1508955).
- Honor and apply DISPLAY-HINT specification when building TextualConvention
  class at libsmi2pysnmp.
- Managed Objects Instances files (smi/mibs/instances/) are now
  double-underscore prefixed to make them imported explicitly by these
  prefixed names. They used to be imported as a side-effect of
  Managed Objects files import what is way too hackerish.
- The libsmi2pysnmp now supports future libsmi bugfix that would generate
  "ranges" subtree along with the legacy and ambiguous "range" one.
- SMI support for fixed-length string indices implemented (SF bug #1584799,
  #1653908).
- Managed Object Instances may now have smiRead, smiWrite, smiCreate methods
  to support specific value mangling. These methods, if present, would be
  invoked from SNMP [Agent] core instead of conventional clone() method.
  The reason is to separate trivial value duplication from specific
  Instance value mangling that may have Agent-specific side effects
  (such as RowStatus).
- MIB table row destruction now works (SF bug #1555010).
- LCD unconfiguration functions for oneliners implemented (SF bug #1635270).
- unloadModules() and unexportSymbols() implemented at MibBuilder
- Notification type PDU proxy code fixed to produce symmetrical
  conversion.
- Various SNMP engine-internal caches expiration implemented.
- SMI-level access control now takes effect only if AC object is
  passed to MIB instrumentation API.
- LCD management code now uses generic MIB instrumentation features.
- Fix to oneliner manager code to have individual UdpSocketTransport
  instance per each SnmpEngine. Multithreaded apps might fail otherwise.
  (SF bug ID #1586420).
- Exclude the PYSNMP_MODULE_ID symbol from MIB view index, as it may get
  resolved into OID label instead of actual MIB object name.
- Memory leak fixed in indices.OidOrderedDict implementation.
- Fix to VACM shortcuts to let notifications and requests to co-exist
  for the same user otherwise.
- Fix to ...oneliner.cmdgen.UsmUserData to support non-default ciphers.
- USM now uses local notion of snmpEngineBoots/Time when authoritative
  and cached estimate otherwise. Also, a security fix applied to to USM
  time-window verification (SF bug #1649032).
- Fix to notification objects resolution code at
  NotificationOriginator.sendNotification()
- Do not raise securityLevel for USM error reports that lacks user
  information, as these reports could never be ciphered (SF bug #1624720).
- Non-default BULK PDU params now actually applied.
- SnmpEngineID default value generation algorithmic function changed
  to allow multiple SNMP engines running on the same host.
- Documentation updated.
- A handful of minor fixes applied (SourceForge tracker IDs #1537592,
  #1537600, #1537659, #1548208, #1560939, #1563715, #1575697, #1599220,
  #1615077, #1615365, #1616579).

Revision 4.1.6a, released on May 25, 2006
-----------------------------------------

- UNSTABLE ALPHA RELEASE.
- pysnmpUsmSecretAuthKey and pysnmpUsmSecretPrivKey length increased
  up to 256 octets. There seems no limit on this in RFC, though.
- A workaround for probably broken Agents: SNMPv3 Manager code defaults
  ContextEngineId to SecurityEngineId whenever ContextEngineId is not
  reported by authoritative SNMP engine on discovery.
- Use empty PDU in engine-discovery report at mpmod/rfc3412.py.
- MibBuilder.loadModules() now fails on missing MIB files.
- MibBuilder.exportSymbols() now accepts unnamed objects (likely Managed
  Objects Instances)
- SNMPv2-SMI.MibScalarInstance objects now support create*/destroy*
  Management Instrumentation methods to pass Columnar Object creation and
  removal events. MibTableColumn class invoke these methods accordingly.
- Fix to AsynNotificationOriginator.asyncSendNotification() callback
  formal parameters
- Initial VACM configuration implemented according to rfc3415 Appendix 1
- tools/buildmibs.sh split-up and re-implemented as tools/build-pysnmp-mib
  and pysnmp-mibs/tools/rebuild-pysnmp-mibs for better usability. These
  and libsmi2pysnmp scripts made installable.
- Types/Notifications/Groups exportSymbols() call chunking implemented
  in tools/libsmi2pysnmp
- Initial values specified to pyasn1 types to comply with latest pyasn1 API.
- Documentation improved
- Minor fixes towards Python 1.5 compatibility

Revision 4.1.5a, released on Nov 04, 2005
-----------------------------------------

- UNSTABLE ALPHA RELEASE.
- Multi-lingual SNMP Trap/Inform Applications completed; examples added
- SMI model re-designed to make a clear separation between
  Managed Objects and their specification (AKA Agent and Manager side)
- SNMP SET Application support completed
- Minor, though backward incompatible, changes to one-liner API
- Many bugfixes

Revision 4.1.4a, released on Aug 16, 2005
-----------------------------------------

- UNSTABLE ALPHA RELEASE.
- SHA-based authentication fixed and privacy implemented
- ...oneliner.cmdgen.UsmUserData constructor now takes
  authProtocol and privProtocol parameters in a backward incompatible
  manner.

Revision 4.1.3a, released on Jul 28, 2005
-----------------------------------------

- UNSTABLE ALPHA RELEASE.
- rfc3413 applications API changes (related to callback function
  behaviour).
- TransportDispatcher now provides "jobs" interface to clients
  for better control of dispatcher's execution.
- Many minor fixes.

Revision 4.1.2a, released on Jul 12, 2005
-----------------------------------------

- UNSTABLE ALPHA RELEASE.
- Top-level application classes renamed into longer, self descripting names
  for clarity.
- CommandResponder & NotificationOriginator applications now uses
  stand-alone SnmpContext for application registration.
- Many minor fixes (inspired by testing on WinXP)

Revision 4.1.1a, released on Jun 29, 2005
-----------------------------------------

- UNSTABLE ALPHA RELEASE.
- SNMPv3 code first published
- SNMP engine and applications implemented on library level
- Major re-design towards SNMPv3-style API.

Revision 4.0.2a, released on Mar 01, 2005
-----------------------------------------

- Adopted to slightly changed asyncore API (as shipped with python 2,4)

Revision 4.0.1a, released on Nov 18, 2004
-----------------------------------------

- Minor bug/typo fixes, mostly in example/ scripts.

Revision 4.0.0a, released on Nov 15, 2004
-----------------------------------------

- UNSTABLE EARLY ALPHA RELEASE.
- Major re-design and re-implementation.
- Rudimental API versioning implemented to let incompatible package
  branches to co-exist within the same Python installation.
- SMI framework designed and implemented. This framework provides
  1) various access to MIB data 2) a way to implement custom MIB
  instrumentation objects. There's also a tool for building SMI classes
  from libsmi(3) output (smidump -f python).
- ASN.1 subtyping machinery implemented. Now dynamic ASN.1 instances
  subtyping and quering becomes available. Previously, this has been done
  through Python classes inheritance what proved to be a wrong concept.
- ASN.1 codecs framework re-designed and re-implemented aimed at a more
  consistent design and better performance. Highlights include abstract
  codec interface and serialized data caching (at encoder).
- Asn1Item constraints machinery re-implemented based on Mike C. Fletcher's
  design and code. Now various constrains are implemented as stand-alone
  objects serving interested Asn1Object derivatives through some abstract
  protocol (that's probably the Decorator design pattern).
- ASN.1 tagging facility re-implemented along the client-server design
  pattern. Besides this seems to be a more appropriate design, it allows
  an easier way for dynamic subtyping.
