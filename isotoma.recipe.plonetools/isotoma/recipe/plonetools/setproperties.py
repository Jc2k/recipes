"""
This script loads a file of properties stored in JSON format and sets then on a
plone site.

JSON takes care of making sure bools are bools and lists are lists so we don't
need to be too clever about introspection.
"""

import optparse, transaction
import simplejson as json

typemap = {
    "unicode": "string",
    "int": "int",
    "bool": "boolean",
    "list": "lines",
}

parser = optparser.OptionParser()
parser.add_option("-p", "--properties", store="properties")
parser.add_option("-s", "--site-id", store="site_id")
options, args = parser.parse_args()

portal = app[options.site_id]

properties = json.loads(open(options.properties).read())
for key, value in properties:
    # What kind of thing is this? We only support those in typemap
    typename = value.__class__.__name__
    if not typename in typemap.keys():
        print "Not setting %s, it has type %s" % (key, typename)
        continue
    typename = typemap[typename]

    print "Setting %s to '%s'" % (key, value)

    # Set it
    portal[key] = value

transaction.commit()
