# 导入进程模块
import multiprocessing
import time


# 需求:定义一个跳舞的方法和唱歌方法,通过多进程实现同时运行
# 定义跳舞方法
def dance():
    for i in range(5):
        print(f'大爷大妈在跳舞....{i}')
        time.sleep(1)


# 定义唱歌方法
def sing():
    for i in range(5):
        print(f'大爷大妈在唱歌....{i}')
        time.sleep(1)


# 非多进程的实现
# dance()
# sing()
# 多任务实现,创建进程和线程都是在主函数中
if __name__ == '__main__':
    # group:进程组,当前只能设置为None,默认不写
    # target:要执行的目标的任务 函数的函数名,不要加括号
    # name:修改进程的名字,默认 Process-N N从1递增, 可以手动修改
    # args:以元组的方式进行传参
    # kwargs:以字典的方式进行传参
    # 创建子进程
    dance_p = multiprocessing.Process(target=dance, name='dance_p')
    sing_p = multiprocessing.Process(target=sing)
    print(dance_p)
    print(sing_p)
    # 获取name值
    print(dance_p.name)
    # 启动子进程
    dance_p.start()
    sing_p.start()
    pass
