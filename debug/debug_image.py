from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape

c = canvas.Canvas("debug/debug.pdf", bottomup=0, pagesize=landscape(A4))

c.saveState()
c.translate(100, 100)
c.scale(1,-1)
# c.drawImage(img_path, 0, 0, width=-width, height=-height, mask='auto')
c.drawImage(f'processed/clip0.jpg', x=0, y=0, width=100, height=100, preserveAspectRatio=True, anchor='c')
c.restoreState()
c.save()