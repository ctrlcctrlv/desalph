f = fontforge.activeFont()

caps = range(0x10400, 0x10427+1)

minis = range(0x10428, 0x1044F+1)

for g, uni in enumerate(list(caps)+list(minis)):
  f[g].unicode = uni
  # f[g].comment = f[g].glyphname
  f[g].glyphname = "uni{:04X}".format(uni)