import sys
import os

script, filename = sys.argv

print "filename is %r."  % filename

open(filename, 'w').close()
lines = open (filename, 'ab')
lines.truncate()

line1 = raw_input(">")
line2 = raw_input(">")

lines.write(line1)
lines.write("\n")
lines.write(line2)
lines.write("\n")

#line.read()
lines.close()