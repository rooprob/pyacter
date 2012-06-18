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

import os
import subprocess
import pprint

class Facts(object):

    facts = {}
    lines = None

    def __init__(self, facter='facter'):
        self.real_facter = facter

    def refresh(self):

        realbin=self.which(self.real_facter)
        if realbin is None:
          return {}

        p = subprocess.Popen([realbin, '-p'], stdout=subprocess.PIPE)
        p.wait()
        self.lines = p.stdout.readlines()
        self.expand_facts()
        return self.facts 

    def expand_facts(self):
        for line in self.lines:
            k, v = line.split(' => ')
            self.facts[k] = v
        return self.facts

    def filter_facts(self, key_filter=None):
        """ Create a new array by filtering the keys. 

            key_filter  an array of compiled regex
        """
        filtered = {}
        for k, v in self.facts.iteritems():
            if key_filter is None \
                    or self.key_filter(k, key_filter):
                filtered[k] = v
        return filtered

    def key_filter(self, key, key_filter):
        for regex in key_filter:
            if regex.search(key):
                return True
        return False
    
    def which(self, program):
        def is_exe(fpath):
            return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

        fpath, fname = os.path.split(program)
        if fpath:
            if is_exe(program):
                return program
        else:
            for path in os.environ["PATH"].split(os.pathsep):
                exe_file = os.path.join(path, program)
                if is_exe(exe_file):
                    return exe_file

        return None

if __name__ == "__main__":
    facts = Facts()

    pprint.pprint(facts.refresh())
