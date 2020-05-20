# -*- coding:gb2312 -*-
import xlwt
#读取Log文件，并提前文件中的关键字
def read_log_data(filename):
    with open(filename, 'r') as file:
        frame_count_list = []#存放帧和局数列表
        time_list  = [] #存放时间列表
        first_win = True #是否存储win的时间
        save_frame_count = False#是否存储帧和局数
        all_count_dic = {}#总统计数据字典

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
def write_to_csv(file_name):
    style = xlwt.easyxf('font: name Times New Roman, color-index black, bold on')
    wb = xlwt.Workbook()  # 创建一个workbook
    ws = wb.add_sheet('agent_1')  # 创建一个sheet
    ws.write(0, 0, '胜利次数', style)  # 单元格坐标点x,单元格坐标点y,写入内容，样式
    ws.write(0, 1, '时间', style)
    ws.write(0, 2, '帧号', style)
    ws.write(0, 3, '局数', style)
    sum = read_log_data(file_name)
    for i in range(1,len(sum)+1):
        ws.write(i, 0, i)
        for j in range(1,4):
            ws.write(i,j,sum[i-1][j-1])
    wb.save('example.xls')

    # with open(file_road,'w') as file:
    #     for i in range(len(sum)):
    #         print('sum[i]',sum[i])
    #         s = str(sum[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
    #         s = s.replace("'", '')+'\n'  # 去除单引号，逗号，每行末尾追加换行符
    #         print('s',s)
    #         file.write(s)
    #     file.close()
    #     print("保存文件成功")


if __name__ == "__main__":
    file_name = 'F:\\游戏\\QQ飞车\\log_2020.4.28_1-4_6\\agent_9.log'
    #file_road = 'F:\\游戏\\QQ飞车\\log_2020.4.28_1-4_6\\agent_1.csv'
    write_to_csv(file_name)
