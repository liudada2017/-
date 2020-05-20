import os
def read_file(file_path):
    fileNameList = os.listdir(file_path)
    for name in fileNameList:
        if name.split('.')[-1]=='txt':
             filename = file_path + '\\' + name
             with open(filename,'r+') as file:
                  lines = file.readlines()
                  file.seek(0) #清空文件内容
                  file.truncate() #清空文件内容
                  for i in lines:
                      file.write(i[2:]) #祛除文件中开头的2个字符
             file.close()

if __name__=="__main__":
    path = "D:\\样本\\ImageEasyTotal"  # 目标路径
    read_file(path)


