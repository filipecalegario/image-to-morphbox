import minecart

pdffile = open('sources/goodnotes_sample.pdf', 'rb')
doc = minecart.Document(pdffile)
page = doc.get_page(0)
# for shape in page.shapes.iter_in_bbox((0, 0, 500, 500)):
for shape in page.shapes:
    print(shape.path[0])
# im = page.images[0].as_pil()  # requires pillow
# im.show()