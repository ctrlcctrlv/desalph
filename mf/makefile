quick: clean desalph.ps
	gv desalph24.ps

desalph.ps: desalph24.dvi
	dvips -o desalph24.ps desalph24.dvi

desalph24.dvi: desalph24.2602gf
	gftodvi desalph24.2602gf

desalph24.2602gf: desalph24.mf desalph.mf dadrawmacros.mf
	mfw desalph24

gv:
	gv desalph24.ps

clean:
	rm -f *.ps *.dvi *gf *.log
