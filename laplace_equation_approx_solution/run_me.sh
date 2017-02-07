ipython assign2.py

pdflatex report.tex
pdflatex report.tex

rm *.png
rm *.log
rm *.aux

evince report.pdf
