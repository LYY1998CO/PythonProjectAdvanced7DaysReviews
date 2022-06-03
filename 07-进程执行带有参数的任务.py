# 导入进程模块
import multiprocessing
import time


# 需求:定义两个方法跳舞和唱歌,实现输入谁跳舞和唱歌,用多进程实现多任务
# 定义跳舞方法
def dance(name):
    print(f'{name}在跳舞...')


# 定义唱歌方法
def sing(name):
    print(f'{name}在唱歌...')


# 实现多进程多任务
if __name__ == '__main__':
    # 创建子进程
    # args:接收的是一个元组类型 元组中只有一个参数,一定要加逗号
    # kwargs:接收的是一个字典类型 key:value, key的值一定是方法中的形参
    p1 = multiprocessing.Process(target=dance, args=('大爷大妈',))
    p2 = multiprocessing.Process(target=sing, kwargs={'name': '大爷大妈'})
    # 启动子进程
    p1.start()
    p2.start()
    pass
