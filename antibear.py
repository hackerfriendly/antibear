#!/usr/bin/python
import subprocess
import sys

letters = sys.argv[1]
pattern = "^[" + letters + "]{1," + str(len(letters)) + "}$"

counts = {}
for l in letters:
	if l in counts:
		counts[l] = counts[l] + 1
	else:
		counts[l] = 1

pat = "egrep '{0}' /usr/share/dict/words".format(pattern)

ap = []
for l in counts:
	ap.append("(" + l + (".*" + l) * counts[l] + ")")

antipat = "| egrep -v '" + '|'.join(ap) + "'"

awk = """| awk '{ print length(), $0 | "sort -n" }'"""

subprocess.call(pat + antipat + awk, shell=True)
