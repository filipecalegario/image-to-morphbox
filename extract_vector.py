import sys
import os

from pdfrw import PdfReader, PdfWriter
from pdfrw.findobjs import page_per_xobj

inpfn = 'sources/after_illustrator_sample.pdf'#sys.argv[1:]
outfn = 'extract.' + os.path.basename(inpfn)
pages = list(page_per_xobj(PdfReader(inpfn).pages, margin=0.5*72))
if not pages:
    raise IndexError("No XObjects found")
writer = PdfWriter(outfn)
writer.addpages(pages)
writer.write()