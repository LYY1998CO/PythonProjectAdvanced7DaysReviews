import multiprocessing
import time
import os # 可以获取进程编号

# 定义跳舞的方法
def dance():
    # 获取子进程编号
    id=os.getpid()
    print(f'当前子进程的编号为:{id}')
    # 获取子进程的父进程id
    parent_id=os.getppid()
    print(f'当前子进程的父进程的id是{parent_id}')
    for i in range(5):
        print('dancing....')
        time.sleep(0.5)

# 定义唱歌的方法
def sing():
    # 获取子进程编号
    id = os.getpid()
    print(f'当前子进程的编号为{id}')
    # 获取子进程的父进程id
    parent_id=os.getppid()
    print(f'当前子进程的父进程的id是{parent_id}')
    for i in range(5):
        print('singing....')
        time.sleep(0.5)
# 通过多进程实现多任务操作
if __name__ == '__main__':
    # 创建子进程
    dance_p=multiprocessing.Process(target=dance)
    sing_p=multiprocessing.Process(target=sing)
    # 启动子进程
    dance_p.start()
    sing_p.start()
    print(dance_p)
    print(sing_p)
    # 获取主进程编号
    id=os.getpid()
    parent_id=os.getppid()
    print(f'主进程的编号为{id},父进程的id是{parent_id}')
    pass