import multiprocessing
import time


# 多任务编程,默认主进程会等待子进程先运行完然后再结束
# 如何实现主进程结束,子进程立马结束, 进程守护
# ① 在启动子进程之前设置一个daemon属性,True 子进程对象名.daemon = True
# ② 在启动子进程之后调用 terminate() 子进程对象名.terminate()
def dance():
    for i in range(5):
        print('dancing...')
        time.sleep(0.5)


# 创建一个子进程实现多任务
if __name__ == '__main__':
    # 创建子进程对象
    # p1=multiprocessing.Process(target=dance,daemon=True)
    p1 = multiprocessing.Process(target=dance)
    # 在启动子进程之前,设置进程守护
    # p1.daemon=True
    # 启动子进程
    p1.start()
    time.sleep(1)
    # 在启动子进程之后,设置进程守护
    p1.terminate()
    print('结束主进程...')
    exit()
    pass
