#!/usr/bin/env python3

import fontforge

import glob

f = fontforge.font()

for ps in sorted(glob.glob("ps/*.ps")):
    g = f.createChar(-1, ps[ps.index("/")+1:])
    g.importOutlines(ps, simplify=False)

f.ascent = 2000
f.descent = 500

for g in f.glyphs():
    l = fontforge.layer()
    for c in g.layers["Fore"]:
        c.closed = True
        l += c
    g.layers["Fore"] = l

f.selection.all()
f.autoWidth(250)
f.save("desalph.sfd")
