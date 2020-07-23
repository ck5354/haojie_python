import configparser
import os
# 获取当前文件的路径
proDir = os.path.split(os.path.realpath(__file__))[0]
# print("当前文件路径"+proDir)


current_path = os.path.abspath("evn.in")
# print("evn.ini绝对路径："+current_path)
#
father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
# print("evn.ini父路径："+father_path)

# os.walk()遍历文件夹下的所有文件
#  os.walk()获得三组数据(rootdir, dirname,filnames)


def get_file_path(file_name):
    current_path = os.path.abspath(__file__)
    # file_path :文件的绝对路径
    file_path = os.path.join(os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".."), file_name)
    # print(file_name+"文件当前绝对路径："+file_path)
    # 根据file_name长度截取掉文件名，得到父路径
    father_path = file_path[:-(len(file_name))]
    # print(file_name+"文件当前路径："+father_path)
    return file_path

# print(get_file_path("算法.py"))



def write_file(file_name, type,content):
    """
    写文件
    :param file_name: 文件名称
    :param type:  参数类型
    :param content: 写入内容
    :return:
    备注：
        #  'r':读 'w':写 'a'：追加
        #  r+: == r+w (可读可写，文件若不存在就报错(IOError)
        #  w+: == w+r (可读可写，文件不存在就创建)
        #  a+ == a+r （可追加可写，文件若不存在就创建）
    """

    file_path = get_file_path(file_name)
    # fileHandle = open(file_path, type)
    # fileHandle.write(content)
    with open(file_path,type) as f:
        f.write(content)

def empty_file(file_name):
    """
    清空文件内容
    :param file_name: 文件名称
    :return:
    """
    file_path = get_file_path(file_name)
    file = open(file_path, "w")
    file.truncate()



"""遍历文件夹"""
dir = "/Users/iss/PycharmProjects/study_python/features"  # 指明被遍历的文件夹

def traverse_folder(dir):
    for parent, dirnames, filenames in os.walk(dir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for dirname in dirnames:  # 输出文件夹信息
            # print("当前目录:" + parent)
            # print("找到的文件名称：" + dirname)
            for filename in filenames:  # 输出文件信息
                print("当前目录:" + parent)
                print("文件名称:" + filename)
                print( "文件全路径:" + os.path.join(parent, filename))


            # 输出文件路径信息
def read_file(file_name):
    """
    整个读取文件
    :param file_path: 文件路径
    :return:

    备注：函数open返回一个表示文件的对象，对象存储在f中

关键字with在不需要访问文件时将其自动关闭。

读取出的内容以字符串形式保存在contents里
    """
    file_path = get_file_path(file_name)
    with open(file_path) as f:
        contents = f.read()
        print(contents)


def read_line_file(file_name):
    """
    按行读取文件
    :param file_name: 文件名称
    :return:
    备注 发现行间距比读取整个文件时大了很多，因为每一行都有末尾都有一个看不见的换行符，而print语句也会加上换行符。要消除这些多余空白行，可以在print语句中使用rstrip()
    """
    file_path = get_file_path(file_name)
    with open(file_path) as f:
        for line in f:
            print(line.strip())

def read_line_file2(file_name):
    """
    可以把文件内容以list形式存起来
    :param file_name:
    :return:
    """
    file_path = get_file_path(file_name)
    with open(file_path) as f:
        lines = f.readlines()
    for line in lines:
        print(line.strip())
"""
read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中。如果文件大于可用内存，为了保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
readlines() 之间的差异是后者一次读取整个文件，象 .read() 一样。.readlines() 自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for ... in ... 结构进行处理。
readline() 每次只读取一行，通常比readlines() 慢得多。仅当没有足够内存可以一次读取整个文件时，才应该使用 readline()
"""

# if __name__ == '__main__':
#     # write_file(file_name = "autotest_log.txt",type = "a", content = "我是陈阔啦啦啦2\n")
#     # empty_file("autotest_log.txt")
#     # read_file("autotest_log.txt")
#     # read_line_file("autotest_log.txt")
#     read_line_file2("autotest_log.txt")