# Makefile for compiling LaTeX documents

# Main document
MAIN = curie

# Compiler
LATEX = pdflatex
BIBTEX = bibtex

# Flags
LATEX_FLAGS = -interaction=nonstopmode

# Default target
all: $(MAIN).pdf

# Compile PDF
$(MAIN).pdf: $(MAIN).tex
	$(LATEX) $(LATEX_FLAGS) $(MAIN).tex
	$(BIBTEX) $(MAIN)
	$(LATEX) $(LATEX_FLAGS) $(MAIN).tex
	$(LATEX) $(LATEX_FLAGS) $(MAIN).tex

# Clean auxiliary files
clean:
	rm -f *.aux *.bbl *.blg *.log *.out *.toc

# Clean all generated files
cleanall: clean
	rm -f $(MAIN).pdf
