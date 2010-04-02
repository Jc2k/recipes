# Copyright 2010 Isotoma Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

class Portmap(object):

    def __init__(self, buildout, name, options):
        self.buildout = buildout
        self.name = name
        self.options = options
        base = int(self.options['base'])
        self.pm = dict([(x, int(y)) for x, y in [
                    x.split() for x in 
                        self.options['map'].strip().split("\n")]])
        for k, v in self.pm.items():
            self.options.setdefault(k, str(base + v))

    def install(self):
        outputdir = os.path.join(self.buildout['buildout']['parts-directory'], self.name)
        if not os.path.exists(outputdir):
            os.mkdir(outputdir)
        out = open(os.path.join(outputdir, "portmap.txt"), 'w')
        print >>out, "[portmap]"
        for k in self.pm.keys():
            print >>out, "%s = %s" % (k, self.options[k])
        out.close()
        return outputdir
        
    def update(self): pass

