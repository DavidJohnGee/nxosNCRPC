# Copyright 2014 David Gee (@davidjohngee)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages
from distutils.command.install import install as _install

import sys

if not sys.version_info[0] == 2:
    print "Sorry, Python 3 is not supported (yet)"
    exit()

if sys.version_info[0] == 2 and sys.version_info[1] < 6:
    print "Sorry, Python < 2.6 is not supported"
    exit()


setup(name='nxosNCRPC',
      version='0.1',
      description="Python library to generate Cisco Nexus NETCONF RPC messages, hello and close messages",
      long_description = "Python library to generate Cisco Nexus NETCONF RPC messages, hello and close messages",
      author="David Gee",
      author_email="david.gee@ipengineer.net",
      url="https://github.com/DavidJohnGee/nxosNCRPC",
      packages=find_packages('.'),
      #install_requires=install_reqs,
      license="Apache License 2.0",
      platforms=["Posix; OS X; Windows"],
      keywords=('NETCONF', 'NETCONF Python client', 'Juniper Optimization', 'Cisco NXOS Optimization'),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Topic :: System :: Networking',
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ]
      )