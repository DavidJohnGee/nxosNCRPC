'''
Author:       David Gee, copyright (C) 2014, ipengineer.net
Date:         17th of November 2014
Version:      0.1
Site:         http://ipengineer.net

This class generates Cisco Nexus hello, close and RPC NETCONF messages for wrapping CLI commands.

Try this code out by copying and pasting the output into an NX-OS box like so off a bash command line:

    ssh user@x.x.x.x -s xmlagent
    
See the example main() boiler plate code at the end of the this page.

'''

from lxml import etree

class nxosNCRPC(object):
    """Create the root object which will be later used for the etree"""
    _root = ""
    
    """Create the message-id object which uniquely identifies an RPC call"""
    _id = ""
    
    """Namespace map. XML namespaces are painful. Be warned.
    In order to include namespaces, you need to define them here. This information was pulled from
    much messing about with Cisco Nexus output and Cisco documentation. 
    This information is also spat out as 'capabilities' when opening up the NETCONF channel."""
    _NSMAP = {"nxos" : "http://www.cisco.com/nxos:1.0", "nc" : "urn:ietf:params:xml:ns:netconf:base:1.0"}
    
    """RPC call exec-command wrapper within the NETCONF call"""
    _rpc_call = ""
    
    """return string containing the NETCONF wrapper"""
    _send_str = ""
    
    """NETCONF hello message"""
    _hello = """<?xml version="1.0" encoding="ISO-8859-1"?>
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <capabilities>
    <capability>urn:ietf:params:xml:ns:netconf:base:1.0</capability>
    <capability>urn:ietf:params:netconf:base:1.0</capability>
  </capabilities>
</hello>
]]>]]>\n"""
    
    """NETCONF close message"""
    _close = """<?xml version="1.0"?>
<nc:rpc message-id="101" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="http://www.cisco.com/nxos:1.0">
  <nc:close-session/>
</nc:rpc>
]]>]]>"""
    
    def __init__(self, _id):
        #Set the message id
        self._id = _id
        
        #Create the root element and attach the namespace map.
        self._root = etree.Element('{urn:ietf:params:xml:ns:netconf:base:1.0}rpc', nsmap=self._NSMAP)
        
        #Add in the root.attribute of 'message-id'
        self._root.attrib['message-id']=self._id
        
        #Geneate the rpc_call wrapper of 'nxos:exec-command'
        self._rpc_call = etree.SubElement(self._root,'{http://www.cisco.com/nxos:1.0}exec-command')
        
    def add_command(self, command):
        #Geneate the sub element of 'nxos:cmd'
        etree.SubElement(self._rpc_call, '{http://www.cisco.com/nxos:1.0}cmd').text = command
    
    def message(self):
        #Now print it out all pretty like.
        self._send_str = etree.tostring(self._root, pretty_print=True, encoding="ISO-8859-1")
        self._send_str += "]]>]]>\n"
        return self._send_str

    def hello(self):
        return self._hello
    
    def close(self):
        return self._close
    
    def __str__(self):
        #Now print it out all pretty like.
        self._send_str = etree.tostring(self._root, pretty_print=True, encoding="ISO-8859-1")
        self._send_str += "]]>]]>"
        return self._send_str

"""
---------------------------------------------------------------------------------
Let's try the code out. Create a class, create a command and print the wrapper
---------------------------------------------------------------------------------
"""
if __name__ == '__main__':
    call1 = nxosNCRPC("42")
    call1.add_command("conf t")
    call1.add_command("int eth2/1")
    call1.add_command("shut")
    # Some built in helper functions to provide the NETCONF hello, the actual RPC message and the NETCONF close messages
    print call1.hello()
    print call1.message()
    print call1.close()