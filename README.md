Python - nxosNCRPC Library 0.1
====================================
<pre>
Author:       David Gee, copyright (C) 2014, ipengineer.net
Date:         17th of November 2014
Version:      0.1
Site:         http://ipengineer.net
Notes:		  Absolutely no error handling exists. Wrap usage with try:/except: to catch problems!
</pre>

This class generates Cisco Nexus hello, close and RPC NETCONF messages for wrapping CLI commands.

Use this code to test:

```
from nxosNCRPC install *

# Create a call1 object with message-id of '42'
call1 = nxosNCRPC("42")
call1.add_command("conf t")
call1.add_command("int eth2/1")
call1.add_command("shut")
# Some built in helper functions to provide the NETCONF hello, the actual RPC message and the NETCONF close messages
print call1.hello()
print call1.message()
print call1.close()
```

The output this code generates can be copy and pasted in to an SSH session to test. From the bash, to connect 
to a Cisco Nexus NETCONF subsystem try the below.

```ssh user@x.x.x.x -s netconf```

Once you're logged in, copy and paste output generated like below. Once you're happy the code is functioning, you can
then use something like Paramiko to programmatically send/receive data to and from NETCONF server.

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <capabilities>
    <capability>urn:ietf:params:xml:ns:netconf:base:1.0</capability>
    <capability>urn:ietf:params:netconf:base:1.0</capability>
  </capabilities>
</hello>
]]>]]>

<?xml version='1.0' encoding='ISO-8859-1'?>
<nc:rpc xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nxos="http://www.cisco.com/nxos:1.0" message-id="42">
  <nxos:exec-command>
    <nxos:cmd>conf t</nxos:cmd>
    <nxos:cmd>int eth2/1</nxos:cmd>
    <nxos:cmd>shut</nxos:cmd>
  </nxos:exec-command>
</nc:rpc>
]]>]]>

<?xml version="1.0"?>
<nc:rpc message-id="101" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="http://www.cisco.com/nxos:1.0">
  <nc:close-session/>
</nc:rpc>
]]>]]>
```