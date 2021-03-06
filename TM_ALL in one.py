#coding=utf-8
'''the who system have three part to make exce report'''
############################BAND WIDTH#####################
'''
The whole script inlcued three functions: getfiles() splitflagfun() and splittxt().
Getfiles() function is the main function to open file and excel table, 
extract text and write the values to the excel and close excel ,
the main function need variable like the location of the files which people want to extract
'''

import re
import xlwt
import os
import numpy as np

def splittxt(split_flag, file_path,flagnum,j,table): 
    '''
    Splittxt() function is defined to read the file and extract values in the file through regulars define by spliflagfun()
    this is a gerneral function.
    '''
    with open(file_path, 'r') as orfile:
        items=orfile.read()
        a=re.findall(split_flag,items)
        print len(a)
        table.write(0,j,str(flagnum))
        for i in xrange(1,len(a)+1):
            table.write(i,j,a[i-1])

def splittxt2(split_flag, file_path,flagnum,j,config_rate,table,rateflag):
    '''
    this function is used to find the field and caculate the traffic current
    '''
    with open(file_path, 'r') as orfile:
        items=orfile.read()
        a=re.findall(split_flag,items)
        print len(a)
        table.write(0,j,str(flagnum))
        table.write(0,j+4,str(rateflag))
        for i in xrange(1,len(a)+1):
            rate=1-round(int(a[i-1])/config_rate,3)
            #print rate
            table.write(i,j,a[i-1])
            if rate> 0.8:
                table.write(i,j+4,rate*100,style)# if the value is large than 0.8, the value will be red'''
            else:
                table.write(i,j+4,rate*100)





file1=xlwt.Workbook()
pattern=xlwt.Pattern()
pattern.pattern=xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour=2
style=xlwt.XFStyle()
style.pattern=pattern

def splitflagfun(file_path,table):
    '''
    Splitflagfun() function is defined to the input the regular expressions 
    like in line 64 to line 71 which can bedfined by the file style:
    '''
    split_flag1=r'"PON-(.*)::UPCIR.*?'
    split_flag2=r'.*?DNMAXMCBW=(.*):.*'
    split_flag3=r'.*?DNMAXMCBW=.*:(.*)"'
    split_flag4=r'.*?UPGBWAVAIL=(.*?),.*?'
    split_flag5=r'.*?DNGBWAVAIL=(.*?),.*?'
    split_flag6=r'.*?UPCIR=(.*?),.*'
    split_flag7=r'.*?UPAIR=(.*?),.*'
    split_flag8=r'.*?DNCIR=(.*?),.*'
    splittxt(split_flag1,file_path,'PON',0,table)
    splittxt(split_flag2,file_path,'DNMAXMCBW',6,table)
    splittxt(split_flag3,file_path,'STATUS',7,table)
    splittxt2(split_flag4,file_path,'UPGBWAVAIL',4,1200000.0,table,'UP_P-BW_Rate(%)')
    splittxt2(split_flag5,file_path,'DNGBWAVAIL',5,2400000.0,table,'DW_P-BW_Rate(%)')
    splittxt(split_flag6,file_path,'UPCIR',1,table)
    splittxt(split_flag7,file_path,'UPAIR',2,table)
    splittxt(split_flag8,file_path,'DNCIR',3,table)


def getFiles(path):
    '''
    通过os.walk遍历path下的所有文件夹和目录，每次遍历产生一个三元组
    第0个为当前目录，第1个为当前目录的子目录列表，第2个为当前目录下所有文件的列表
    '''
    for root,dirs,item in os.walk(path):
        #nm=0
        for file in item:
            file_path=root+str('\\')+file
            b=re.findall(r'.*\\(.*?).txt',str(file_path))
            print str(b[0])
            table=file1.add_sheet(str(b[0]))
            #nm+=1
            splitflagfun(file_path,table)
        file1.save('bandwidth.xls') #生成EXCEL表格的地方


getFiles('D:\Pycharm project\\test2') # 存放LOG文件的文件夹位置

###############################MULTICAST######################################
#coding=utf-8
import re
import xlwt
import os

def splittxt(split_flag, file_path,flagnum,j,table):
    with open(file_path, 'r') as orfile:
        items=orfile.read()
        a=re.findall(split_flag,items)
        print len(a)
        table.write(0,j,str(flagnum))
        for i in xrange(1,len(a)+1):
            table.write(i,j,a[i-1])




file1=xlwt.Workbook()
pattern=xlwt.Pattern()
pattern.pattern=xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour=7
style=xlwt.XFStyle()
style.pattern=pattern

def splitflagfun(file_path,table):
    split_flag1=r'"PONMCSRC-(.*)::.*?"'
    split_flag2=r'".*?:SRCNAME=\\"(.*?)\\",.*?'
    split_flag3=r'.*?SVCNAME=\\"(.*?)\\.*?"'
    split_flag4=r'.*?PEAKRATE=(.*?),.*?'
    split_flag5=r'.*?SUSTAINRATE=(.*?),VLAN.*?'
    split_flag6=r'.*?VLANID=(.*?),.*?'
    split_flag7=r'.*?MCTYPE=(.*?),.*?'
    split_flag8=r'.*?MEMBERSHIPDEC=\\"(.*?)\\",PR.*?'
    split_flag9=r'.*?PREVDUR=(.*?),.*?'
    split_flag10=r'.*?MAXPREV=(.*?),.*?'
    split_flag11=r'.*?BLKOUT=(.*?),.*?'
    split_flag12=r'.*?SRCIPADDR=(.*?)"'
    splittxt(split_flag1,file_path,'PONMCSRC',0,table)
    splittxt(split_flag2,file_path,'SRCNAME',1,table)
    #splittxt(split_flag3,file_path,'SVCNAME',2)
    splittxt(split_flag4,file_path,'PEAKRATE',3,table)
    splittxt(split_flag5,file_path,'SUSTAINRATE',4,table)
    splittxt(split_flag6,file_path,'VLANID',5,table)
    #splittxt(split_flag7,xml_file_path,'MCTYPE',6)
    #splittxt(split_flag8,xml_file_path,'MEMBERSHIPDEC',7)
    #print 'MEMBERSHIPDEC'
    #splittxt(split_flag9,xml_file_path,'PREVDUR',8)
    #splittxt(split_flag10,xml_file_path,'MAXPREV',9)
    #splittxt(split_flag11,xml_file_path,'BLKOUT',10)
    splittxt(split_flag12,file_path,'SRCIPADDR',6,table)

def getFiles(path):
    ''''''
    for root,dirs,item in os.walk(path):
        nm=0
        for file in item:
            file_path=root+str('\\')+file
            b=re.findall(r'.*\\(.*?).txt',str(file_path))
            print str(b[0])
            table=file1.add_sheet(str(b[0]))
            nm+=1
            splitflagfun(file_path,table)
        file1.save('chekmulticast.xls')


getFiles('D:\Pycharm project\\test')
########################################VLAN#############################################
# -*- coding: utf-8 -*-
#coding=utf-8
import re
import xlwt
import os
import numpy as np
import scipy as sp
from sklearn import tree
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
import xlrd
import xlwt



def floata(data22): #把列表中的文本信息全部换成数值
    data22=np.array(data22)
    data22[data22=='ENABLED']=1
    data22[data22=='DISABLED']=0
    data22[data22=='RBRIDGE']=1
    data22[data22=='XCONN']=0
    data22[data22=='MAXIS_HSI_Home']=1
    data22[data22=='MAXIS_HSI_SME']=2
    data22[data22=='MAXIS_TR069']=3
    data22[data22=='MAXIS_IPTV']=4
    data22[data22=='MAXIS_VOIP']=5
    data22[data22=='P1_HSI_Home']=6
    data22[data22=='P1_HSI_BUSINESS']=7
    data22[data22=='P1_VOIP']=8
    data22[data22=='CELCOM_HSI_Home']=9
    data22[data22=='CELCOM_VOIP']=10
    data22[data22=='Celcom_VOBB']=10
    data22[data22=='REDTONE_HSI_HOME']=11
    data22[data22=='REDTONE_VOIP']=12
    data22[data22=='HSI(HSBB)']=13
    data22[data22=='IPTV(HSBB)']=14
    data22[data22=='VOIP(HSBB)']=15
    data22[data22=='CCS']=16
    data22[data22=='EFM_1002']=17
    data22[data22=='TM_WIFI']=18
    data22[data22=='P1_HSI_SME']=19
    data22[data22=='FORMIS_HSI_Consumer']=20
    data22[data22=='HSI_VLAN621']=21
    data22[data22=='HSI_WiFi']=22
    data22[data22=='Celcom_HSI_Home']=-1
    data22[data22=='VOBB_VLAN821']=-2
    data22[data22=='VOBB_VLAN822']=-3
    return data22

def traintree(data22,table):#训练样本，并对新进入的数据进行分类
    ''''' 数据读入 '''
    data   = []
    labels = []
    with open("YZYB.txt") as ifile:#训练样本的位置
            for line in ifile:
                tokens = line.strip().split('	')
                data.append([float(tk) for tk in tokens[:-1]])
                labels.append(tokens[-1])
    x = np.array(data)
    labels = np.array(labels)
    y = np.zeros(labels.shape)
    #print x
    #print y

    ''''' 标签转换为0/1 '''
    y[labels=='OK']=1

    ''''' 拆分训练数据与测试数据 '''
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0)

    ''''' 使用信息熵作为划分标准，对决策树进行训练 '''
    clf = tree.DecisionTreeClassifier(criterion='entropy')
    #print(clf)
    clf.fit(x, y)

    ''''' 把决策树结构写入文件 '''
    #with open("tree.dot", 'w') as f:
    #    f = tree.export_graphviz(clf, out_file=f)

    ''''' 系数反映每个特征的影响力。越大表示该特征在分类中起到的作用越大 '''
    print(clf.feature_importances_)
    #clf = tree.DecisionTreeClassifier(criterion='entropy')
    data22=np.array(data22) #传入的数据的位置
    #print data22
    answer=clf.predict(data22)
    i=1
    for an in answer:
        if an==0:
            table.write(i,5,'NOK',style) #标示
        else:
            table.write(i,5,'OK')#table为需要写入的表格
        i+=1


def splittxt(split_flag, file_path,flagnum,j,table,data22):
    with open(file_path, 'r') as orfile:
        items=orfile.read()
        a=re.findall(split_flag,items)
        #print len(a)
        table.write(0,j,str(flagnum))
        #data22=np.zeros((len(a),5))#生成相应大小的零阵
        for i in xrange(1,len(a)+1):
            table.write(i,j,a[i-1])
            b=floata(a)
            data22[i-1,j]=b[i-1]#生成相应的暂存矩阵来存放数据
    return data22





file1=xlwt.Workbook()
pattern=xlwt.Pattern()
pattern.pattern=xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour=2
style=xlwt.XFStyle()
style.pattern=pattern

def splitflagfun(file_path,table):
    split_flag1=r'"PONVLAN-(.*)::MODE.*?'
    split_flag2=r'.*?:MODE=(.*?),.*'
    split_flag3=r'.*?NAME=\\"(.*)\\",.*?'
    split_flag4=r'.*?DHCPRELAY=(.*),TAG.*?'
    split_flag5=r'.*?PPPOERELAY=(.*?),.*?'
    data22=np.zeros((15,5))
    splittxt(split_flag1,file_path,'VLANID',0,table,data22)
    splittxt(split_flag2,file_path,'MODE',1,table,data22)
    splittxt(split_flag3,file_path,'NAME',2,table,data22)
    splittxt(split_flag4,file_path,'DHCPRELAY',3,table,data22)
    data22=splittxt(split_flag5,file_path,'PPPOERELAY',4,table,data22)
    traintree(data22,table)#增加了机器学习的代码片段

    #return data22


def getFiles(path):

    for root,dirs,item in os.walk(path):
        #nm=0
        for file in item:
            #print len(item)
            file_path=root+str('\\')+file
            b=re.findall(r'.*\\(.*?).txt',str(file_path))
            print str(b[0])
            table=file1.add_sheet(str(b[0]))
            #nm+=1
            splitflagfun(file_path,table)
            #answer = clf.predict(data22)


        file1.save('VLAN7342.xls')





if __name__ == '__main__':
    getFiles('D:\Pycharm project\\test3')






############################################################################################




