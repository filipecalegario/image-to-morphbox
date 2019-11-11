import cv2
import math

def convert_dimension_pdf_img(num_pdf):
    return int(math.ceil((3086/841.89)*num_pdf))

def convert_dimension_img_pdf(num_img):
    return (841.89/3086)*num_img

def slice_main_template():
    columns = 7
    rows = 5

    image = cv2.imread(filename = "sources/icons-bg.jpg")

    subimg_width = convert_dimension_pdf_img(120.27)
    subimg_height = convert_dimension_pdf_img(84.206)
    initial_p_x = convert_dimension_pdf_img(0)
    initial_p_y = convert_dimension_pdf_img(139.075)

    counter = 0

    for y in range(5):
        for x in range(7):  
            cur_x = (initial_p_x + subimg_width * x)
            cur_y = (initial_p_y + subimg_height * y)
            print(cur_x,cur_y)
            end_x = cur_x + subimg_width
            end_y = cur_y + subimg_height
            clip = image[cur_y:end_y, cur_x:end_x, :]
            cv2.imwrite(filename = f'processed/clip{counter}_{x}_{y}.jpg', img = clip)      
            counter = counter + 1

slice_main_template()