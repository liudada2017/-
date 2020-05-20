import os
def remove_file(path):
    fileNameList = os.listdir(path)
    retainList = [] #保存需要的图片名
    for name in fileNameList:
        if name.split('.')[-1] == 'txt':
            retainList.append(name.split('.')[0])

    for imgName in fileNameList:
        # if imgName.split('.')[-1] =='xml':
        #     os.remove(path +'\\' + imgName)
        if imgName.split('.')[0] in retainList:
            continue
        else:
            os.remove(path + '\\' + imgName)

if __name__=="__main__":
    path = 'D:\\sample\\CJZC\\unuse\\empty'
    remove_file(path)