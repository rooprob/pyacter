# Copyright (c) 2012, Robert Fielding <rf@tamasi.org> 
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
#  * Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.  
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.  
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import re
import sys
import unittest

sys.path.append("../")
from pyacter.facter import Facter


class PyacterFactSequenceFunctions(unittest.TestCase):

    def test_fetch_all(self):

        f = Facter()
        facts = f.facts()

        self.assertTrue(isinstance(facts, dict))
        self.assertTrue(facts.has_key('architecture'))
        self.assertTrue(facts.has_key('ipaddress'))
        self.assertTrue(facts.has_key('fqdn'))

    def test_fetch_filter(self):

        f = Facter()

        key_filter = [
            re.compile(r"arch"),
            re.compile(r"fqdn"),
            re.compile(r"ip"),
        ]
        filtered = f.facts(key_filter=key_filter)

        self.assertTrue(isinstance(filtered, dict))
        self.assertTrue(filtered.has_key('architecture'))
        self.assertTrue(filtered.has_key('ipaddress'))
        self.assertTrue(filtered.has_key('fqdn'))

if __name__ == '__main__':
    unittest.main()
