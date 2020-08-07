from tkinter import *
import xlrd
import matplotlib.pyplot as plt
import codecs

wb = xlrd.open_workbook('students.xlsx')
table = wb.sheets()[0]
id_list = table.col_values(2, start_rowx=1, end_rowx=None)
name_list = table.col_values(1, start_rowx=1, end_rowx=None)

def Creat_Window():
    tk = Tk()
    btn1 = Button(tk, text="学生来源信息统计（区域）", fg='black', bg='yellow', command=Region)
    btn2 = Button(tk, text="学生来源信息统计（省）", fg='black', bg='yellow', command=Province)
    btn3 = Button(tk, text="学生性别信息统计", fg='black', bg='yellow', command=Sex)
    btn4 = Button(tk, text="学生姓氏信息统计", fg='black', bg='yellow', command=Name)
    btn5 = Button(tk, text="学生年龄信息统计", fg='black', bg='yellow', command=Age)
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack()
    btn5.pack()
    tk.mainloop()

def Province():
    count = {}  
    data = getData('data.txt')
    for id in id_list:
        try:
            count[data[id[:2]]] += 1
        except:
            count[data[id[:2]]] = 1
    province_list = count.keys()
    num_list = count.values()
    data = [x/len(id_list)*100 for x in num_list]
    labels = province_list
    plt.pie(data, labels=labels, colors='rgbymc', autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('\n各省生源数比率图\n')
    plt.show()

def Region():
    count = {}
    region_list = ['其他地区', '华北地区', '东北地区', '华东地区', '中南地区', '西南地区', '西北地区','台湾省', '港澳地区']
    for id in id_list:
        try:
            count[region_list[int(id[0])]] += 1
        except:
            count[region_list[int(id[0])]] = 1
    province_list = count.keys()
    num_list = count.values()
    data = [x/len(id_list)*100 for x in num_list]
    labels = province_list
    plt.pie(data, labels=labels, colors='rgbymc', autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('\n各区域生源数比率图\n')
    plt.show()

def Sex():
    m, f = 0, 0
    for id in id_list:
        if int(id[16]) % 2 != 0:
            m += 1
        else:
            f += 1
    data = [m/len(id_list)*100, f/len(id_list)*100]
    labels = ['男生', '女生']
    sjxl = plt.bar(range(len(data)), data, tick_label=labels, color='rgbycm')
    for sj in sjxl:
        height = sj.get_height()
        plt.text(sj.get_x()+sj.get_width()/2., 1.03*height, '%1.1f' % float(height) + '%')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.xlabel('性别（男/女）')
    plt.ylabel('男女生人数比率（%）')
    plt.title('\n男女生人数比率图\n')
    plt.ylim(0, 100)
    plt.show()

def Name():
    count = {}
    for name in name_list:
        first_name = name[0]
        try:
            count[first_name] += 1
        except:
            count[first_name] = 1
    print(sorted(count.items(), key = lambda kv:(kv[1], kv[0]))) 

def Age():
    count = {}
    data, labels = [], []
    for id in id_list:
        year = int(id[6:10])
        try:
            count[year] += 1
        except:
            count[year] = 1
    for i in sorted(count): 
        labels.append(i)
        data.append(count[i])
    sjxl = plt.bar(range(len(data)), data, tick_label=labels, color='rgbycm')
    for sj in sjxl:
        height = sj.get_height()
        plt.text(sj.get_x()+sj.get_width()/2., 1.03*height, '%d' % int(height))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.xlabel('出生年份')
    plt.ylabel('人数')
    plt.title('\n出生年份分布图\n')
    plt.ylim(0, 50)
    plt.show()

def getData(filename):
    data = {}
    with codecs.open(filename, 'r', 'utf-8') as f:
        lines = f.readlines()
        for line in lines:
            code, province = line.split()
            data[code] = province
    f.close()
    return data

if __name__ == "__main__":
    Creat_Window()
