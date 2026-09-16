NAME=main

all: clean
	pdflatex $(NAME).tex
	make bib
	pdflatex $(NAME).tex
	pdflatex $(NAME).tex
  # make clean

bib:
	if [ -e $(NAME).aux ] ; \
	then \
		echo COMPILE BIBTEX; \
		bibtex $(NAME).aux; \
	else \
		echo NO REFERENCES TO COMPILE; \
	fi;

clean:
	rm -f $(NAME).aux $(NAME).bbl $(NAME).log $(NAME).out $(NAME).toc $(NAME).blg $(NAME).dvi $(NAME).ps $(NAME).nav $(NAME).snm $(NAME).vrb $(NAME).synctex.gz
