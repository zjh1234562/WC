import sys
from GUI import *
from Count import *

def main():
    argv=sys.argv[1:]
    windows = Windows()
    count = Count()
    files=[]

    if '-x' in argv[:]:
        windows.gui()
    else:

        if '-s' in argv[:]:
            files=count.get_allwj(argv[-1])
        else:
            files.append(argv[-1])

        print(files)

        for file in files:
            print("现在处理" + file)
            count.zhushi=0
            count.spacecount=0
            count.code=0
            count.linecount=-1
            if '-c' in argv[:]:
                print(count.get_char(file))
            if '-w' in argv[:]:
                print(count.get_word(file))
            if '-l' in argv[:]:
                print(count.get_line(file))
            if '-a' in argv[:]:
                print(count.get_other(file))

if __name__ == '__main__':
    main()