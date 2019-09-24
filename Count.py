import os
import sys
import re
from GUI import *


class Count():

    def __init__(self):
        #self.filepath=file     #文件名
        self.linecount=-1    #行数
        self.spacecount=0
        self.code=0
        self.zhushi=0

    def get_word(self,filepath):
        try:
            with open(filepath, 'r') as f:
                str="单词数为：{}".format(len([word for line in f for word in line.split()]))
                #print("单词数为：{}".format(len([word for line in f for word in line.split()])))
        except Exception as e:
            str="文件不存在"
        return str


    def get_line(self,filepath):
        try:
            for self.linecount, line in enumerate(open(filepath, 'r')):
                pass
            self.linecount+= 1
            str='行数为：{}'.format(self.linecount)
            #print('行数为：{}'.format(self.linecount))
        except:
            str="文件不存在"
        return str

    def get_char(self,filepath):
        try:
            with open(filepath,'r') as f:
                str="字符数为：{}".format(sum([len(word) for line in f for word in line.split()]))
                #print("字符数为：{}".format(sum([len(word) for line in f for word in line.split()])))
        except:
            str="文件不存在"
        return str

    def get_other(self,filepath):

        try:
            with open(filepath, 'r') as f:
                for i in f.readlines():
                    self.code += 1
                    if i.find('//') == 0 or i.find('//') == 1:
                        self.zhushi += 1
                    if len(i.strip()) <= 1:
                        self.spacecount += 1

            str = "空行为：{}".format(self.spacecount), "代码行为：{}".format(
                self.code - self.spacecount - self.zhushi), "注释行为：{}".format(self.zhushi)

        except:
            str="文件不存在"
        return str

    def get_allwj(self,filepath):
        if '/' in filepath:
            basepath=filepath[:filepath.rfind('/')+1]
        else:
            basepath=os.getcwd()
        filelist=os.listdir(basepath)
        #print(filelist)
        listf=[]
        for i in filelist:
            str=filepath[filepath.find('.')+1:]
            searchObj = re.search(r'(.*)\.'+str, i, re.M | re.I)
            if searchObj!=None:
                listf.append(basepath+i)
        return listf






