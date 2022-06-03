import multiprocessing


# 定义跳舞的方法
def dance():
    print(f'当前的进程的名称为:{multiprocessing.current_process().name}')


# 多进程实现多任务
if __name__ == '__main__':
    # 创建5个子进程对象
    for i in range(5):
        p1 = multiprocessing.Process(target=dance)
        # 启动子进程
        p1.start()
