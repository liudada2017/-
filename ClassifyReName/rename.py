import os
from shutil import move
def SeparateFile(path):
    fileNameList = os.listdir(path)
    for i in range(0,len(fileNameList)):
         name = fileNameList[i].split(')')[-1]
         if name == '.png': #判断是否是原图
             if os.path.isdir(path + '\\' + 'images'):#判断指定路径下是否有images文件夹
                move(path + '\\' + fileNameList[i], path + '\\' + 'images')
             else:
                 os.mkdir(path + '\\' + 'images')
                 move(path + '\\' + fileNameList[i], path + '\\' + 'images')
         elif name == '_1.png': #判断是否是修改后的图像
             if os.path.isdir(path + '\\' + 'changeImages'):#判断指定路径下是否有changeIamges文件夹
                move(path + '\\' + fileNameList[i], path + '\\' + 'changeImages')
             else:
                 os.mkdir(path + '\\' + 'changeImages')
                 move(path + '\\' + fileNameList[i], path + '\\' + 'changeImages')
    return path + '\\' + 'changeImages'

def ReName(src):
    fileNameList = os.listdir(src)
    for i in range(0,len(fileNameList)):
         used_name = src + '\\' + fileNameList[i]
         new_name = src + '\\' + fileNameList[i].split(')')[0] + ').png'
         os.rename(used_name,new_name)
    print('重命名完成！')

if __name__ == "__main__":
    path = "C:\\Users\\v_liupliu\\Documents\\Images_out5"  # 目标路径
    ChangeImgSrc = SeparateFile(path)
    print(ChangeImgSrc)
    ReName(ChangeImgSrc)
