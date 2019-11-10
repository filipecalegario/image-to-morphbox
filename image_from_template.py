import cv2

columns = 7
rows = 5

image = cv2.imread(filename = "sources/icons-bg.jpg")

subimg_width = 437
subimg_height = 304
initial_p_x = 0
initial_p_y = 514

for y in range(5):
    for x in range(7):
        cur_x = (initial_p_x + subimg_width * x)
        cur_y = (initial_p_y + subimg_height * y)
        print(cur_x,cur_y)
        end_x = cur_x + subimg_width
        end_y = cur_y + subimg_height
        clip = image[cur_y:end_y, cur_x:end_x, :]
        cv2.imwrite(filename = f'clip{x}_{y}.jpg', img = clip)      

# clip = image[514:818, 0:437, :]


