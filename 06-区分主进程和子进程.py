import multiprocessing


# print(multiprocessing.current_process())
# 定义两个函数，唱歌和跳舞，通过多进程方式实现多任务
# 定义跳舞的方法
def dance():
    print(f'当前dance子进程的信息为{multiprocessing.current_process()}')
    print('dancing....')


# 定义唱歌方法
def sing():
    print(f'当前sing子进程的信息为{multiprocessing.current_process()}')
    print('singing...')


# 通过多进程实现多任务
if __name__ == '__main__':
    # 创建子进程
    p1 = multiprocessing.Process(target=dance)
    p2 = multiprocessing.Process(target=sing)
    # 启动子进程
    p1.start()
    p2.start()
    print(f'当前的线程信息为{multiprocessing.current_process()}')
    pass
