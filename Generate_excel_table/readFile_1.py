# -*- coding:gb2312 -*-
import os
import re
import openpyxl
from openpyxl.styles import Font
#读取Log文件，并提取文件中的关键字
def read_log_data(filename):
    with open(filename, 'r') as file:
        frame_count_list = []#存放帧和局数列表
        time_list  = [] #存放时间列表
        first_win = True #是否存储win的时间
        save_frame_count = False#是否存储帧和局数

        while True:
            lines = file.readline()  # 整行读取数据
            if not lines:
                break
            item_win = [i for i in lines.split(']')]
            item_over = [i for i in lines.split(':')]

            if len(item_over)!=1 and item_over[-1]!='\n':
                if item_over[-1].split(',')[-1].split()[-1].find('win')!=-1:
                    if first_win:
                        time_list.append(item_win[0].split(',')[0].split()[-1])
                        first_win = False
                        save_frame_count = True

                elif item_over[len(item_over)-2].find('episode over')!= -1:
                   if save_frame_count:
                       index = item_over[-1].split(',')[0].split('=')[-1]
                       count = item_over[-1].split(',')[1].split('=')[-1]
                       frame_count_list.append([index,count])
                       first_win = False
                       save_frame_count = False

                elif item_over[-1].find('Epsiode over')!=-1:
                    first_win = False
                else:
                    first_win = True
    file.close()
    for i in range(0,len(time_list)):
        frame_count_list[i].insert(0,time_list[i])
    return frame_count_list

#将所有数据写出到csv文件中
def write_to_csv(fileList, dir_path):
    n = 0 #建表格的位置
    wb = openpyxl.Workbook()#新建一个工作薄
    for file_name in fileList:
        sheet_name = file_name.split('\\')[-1].split('.')[0]#获取表格名称
        ws = wb.create_sheet(title= sheet_name, index=n) #创建一个表格
        ws['A1'].font = Font(bold=True)
        ws['B1'].font = Font(bold=True)
        ws['C1'].font = Font(bold=True)
        ws['D1'].font = Font(bold=True)
        ws['A1'].value = '胜利次数'
        ws['B1'].value = '时间'
        ws['C1'].value = '帧号'
        ws['D1'].value = '局数'
        sum = read_log_data(file_name)
        for i in range(1,len(sum)+1):#往单元格中填写数据
            ws.cell(i+1, 1).value = i
            for j in range(1,4):
                ws.cell(i+1, j+1).value = sum[i-1][j-1]
        n = n+1
    new_count_table(n, wb)
    wb.save(dir_path + '\\' + 'result.xls')#保存excel文件
    print('保存成功,保存地址为：',dir_path + '\\' + 'result.xls')

#新建表格table,并填写表格标题
def new_count_table(n, wb):
    ws = wb.create_sheet(title='Count', index=n)
    ws['A1'].font = Font(bold=True)
    ws['B1'].font = Font(bold=True)
    ws['C1'].font = Font(bold=True)
    ws['D1'].font = Font(bold=True)
    ws['E1'].font = Font(bold=True)
    ws['F1'].font = Font(bold=True)
    ws['G1'].font = Font(bold=True)
    ws['A1'].value = 'id'
    ws['B1'].value = '时间'
    ws['C1'].value = '帧号'
    ws['D1'].value = '局数'
    ws['E1'].value = '手机序号'
    ws['F1'].value = '赢的时间'
    ws['G1'].value = '开始测试时间'


#获取文件夹下的所有日志文件
def get_files(dir_path):
    fileList = []#存放所有日志文件
    files = os.listdir(dir_path)#获取所有文件
    ptn = re.compile('.*\.log') #log结尾的文件正则表达式
    for f in files: #遍历所有文件，提取log结尾的日志文件
        if (os.path.isfile(dir_path + '\\' + f)):
            res = ptn.match(f)
            if (res != None) and f != 'train.log':
                fileList.append(dir_path + '\\' + res.group())
        else:
            print('无效文件')
    return fileList


if __name__ == "__main__":
    dir_path = 'F:\\New_Game\\QQ飞车\\log_2020.5.13_1-4_6' #存放日志的文件夹
    fileList = get_files(dir_path)
    write_to_csv(fileList, dir_path)
