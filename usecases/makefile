SRC     = *.tex
BIBS    = 
YEAR    = 2016
LATEX   = pdflatex
BIBTEX  = bibtex
DOC     = usecases

$(DOC).pdf: $(SRC)
	$(LATEX) $(DOC).tex
	rm -f *.aux *.bbl *.blg *.dvi *.log *.out *.toc *.swp

clean:
	rm -f *.aux *.bbl *.blg *.dvi *.log *.out *.toc *.swp *.pdf

view:
	open $(DOC).pdf
