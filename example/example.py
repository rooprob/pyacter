from pyacter.facter import Facter
import pprint
import re

class MyFacter(Facter):
    def facts(self):
        return super(MyFacter, self).facts(key_filter=self.my_filter)

class ThingFacts(MyFacter):
    my_filter=[
            re.compile(r"^kernel"),
            re.compile(r"^inter"),
            ]   


if __name__ == "__main__":

    thing_facter = ThingFacts()

    pprint.pprint(thing_facter.facts())


