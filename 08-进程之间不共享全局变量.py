import multiprocessing

# 进程之间不共享全局变量: 将全局变量拷贝N份,每个进程操作的都是自己的这一份
# 需求:定义一个全局变量空列表list1,通过多进程任务方式,实现一个方法在向列表添加0,1,2三个数字,另外一个方法实现读取列表的操作
# 定义一个列表 全局变量
list1 = []


# 定义添加列表的方法
def add():
    for i in range(5):
        list1.append(i)
    print(f'add进程中的list的值为:{list1}')


# 定义读取列表的方法
def read():
    for i in range(3):
        list1.append(i)
    print(f'read进程中的list的值为:{list1}')


# 多进程方式实现多任务
if __name__ == '__main__':
    # 创建子进程
    p1 = multiprocessing.Process(target=add)
    p2 = multiprocessing.Process(target=read)
    # 启动子进程
    p1.start()
    p2.start()
    # 在主进程中获取列表中的数据
    print(f'主进程中读取到的数据为:{list1}')
    pass
