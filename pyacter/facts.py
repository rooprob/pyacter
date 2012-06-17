
import os
import subprocess
import pprint

class Facts(object):

    facter_bin = 'facter'

    def __init__(self):
        pass

    def gather(self):

        realbin=self.which(self.facter_bin)
        if realbin is None:
          return None

        p = subprocess.Popen([realbin, '-p'], stdout=subprocess.PIPE)
        p.wait()
        self.lines = p.stdout.readlines()
        return self.expand_facts()

    def expand_facts(self):
        res = {}
        for line in self.lines:
            k, v = line.split(' => ')
            res[k] = v
        return res

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
    pprint.pprint(facts.gather())
