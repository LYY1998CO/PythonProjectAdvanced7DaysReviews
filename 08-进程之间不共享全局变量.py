import multiprocessing
list1=[]
def add():
    for i in range(5):
        list1.append(i)
    print(f'add进程中的list的值为:{list1}')

def read():
    for i in range(3):
        list1.append(i)
    print(f'read进程中的list的值为:{list1}')
if __name__ == '__main__':
    p1=multiprocessing.Process(target=add)
    p2=multiprocessing.Process(target=read)
    p1.start()
    p2.start()
    print(f'主进程中读取到的数据为:{list1}')
    pass