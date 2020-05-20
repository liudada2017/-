# -*- coding:gb2312 -*-
import xlwt
#��ȡLog�ļ�������ǰ�ļ��еĹؼ���
def read_log_data(filename):
    with open(filename, 'r') as file:
        frame_count_list = []#���֡�;����б�
        time_list  = [] #���ʱ���б�
        first_win = True #�Ƿ�洢win��ʱ��
        save_frame_count = False#�Ƿ�洢֡�;���
        all_count_dic = {}#��ͳ�������ֵ�

        while True:
            lines = file.readline()  # ���ж�ȡ����
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

#����������д����csv�ļ���
def write_to_csv(file_name):
    style = xlwt.easyxf('font: name Times New Roman, color-index black, bold on')
    wb = xlwt.Workbook()  # ����һ��workbook
    ws = wb.add_sheet('agent_1')  # ����һ��sheet
    ws.write(0, 0, 'ʤ������', style)  # ��Ԫ�������x,��Ԫ�������y,д�����ݣ���ʽ
    ws.write(0, 1, 'ʱ��', style)
    ws.write(0, 2, '֡��', style)
    ws.write(0, 3, '����', style)
    sum = read_log_data(file_name)
    for i in range(1,len(sum)+1):
        ws.write(i, 0, i)
        for j in range(1,4):
            ws.write(i,j,sum[i-1][j-1])
    wb.save('example.xls')

    # with open(file_road,'w') as file:
    #     for i in range(len(sum)):
    #         print('sum[i]',sum[i])
    #         s = str(sum[i]).replace('[', '').replace(']', '')  # ȥ��[],�����а����ݲ�ͬ������ѡ��
    #         s = s.replace("'", '')+'\n'  # ȥ�������ţ����ţ�ÿ��ĩβ׷�ӻ��з�
    #         print('s',s)
    #         file.write(s)
    #     file.close()
    #     print("�����ļ��ɹ�")


if __name__ == "__main__":
    file_name = 'F:\\��Ϸ\\QQ�ɳ�\\log_2020.4.28_1-4_6\\agent_9.log'
    #file_road = 'F:\\��Ϸ\\QQ�ɳ�\\log_2020.4.28_1-4_6\\agent_1.csv'
    write_to_csv(file_name)
