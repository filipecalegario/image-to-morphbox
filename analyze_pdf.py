from pdfrw import PdfReader

x = PdfReader('sources/after_illustrator_sample.pdf')

# print(x.pages[0].Contents.stream)

root_dict = x['/Root']

for some in x:
    print(some, x[some])