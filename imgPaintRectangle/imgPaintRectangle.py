import cv2
def paint_rectangle(path):
    dw = 0.00078125 #1.0/1280
    dh = 0.001388888888888889 #1.0/720
    file_path = path + '.txt'
    png_path = path + '.png'
    image = cv2.imread(png_path)
    with open(file_path, 'r') as file:
        lines = file.readlines()  # 整行读取数据
        for line in lines:
            zuo_biao_list = line.split()
            w = int(float(zuo_biao_list[2]) / dw)
            h = int(float(zuo_biao_list[3]) / dh)
            x = int(float(zuo_biao_list[0]) / dw)-int(w/2)
            y = int(float(zuo_biao_list[1]) / dh)-int(h/2)
            draw_1 = cv2.rectangle(image,(x,y),(x+w,y+h), (0,255,0), 2)
            cv2.imwrite("vertical_flip.jpg", draw_1)  # 将画过矩形框的图片保存到当前文件夹
        cv2.imshow("draw_0", draw_1)  # 显示画过矩形框的图片
        cv2.waitKey(0)
        cv2.destroyWindow("draw_0")
    file.close()

if __name__=="__main__":
    #path = 'D:\\sample\\CFM\\7_7960'
    path = 'D:\\sample\\CJZC\\unuse\\empty\\31_142'
    paint_rectangle(path)