import os
import multiprocessing
import random
import time

'''
因为进程间不共享全局变量，故操作系统对多进程使用queue进行通信
'''
def copy_file(queue,file_name,souce_folder_name,dest_folder_name):
    f_read = open(souce_folder_name+'/'+file_name,'rb')
    f_write = open(dest_folder_name+'/'+file_name,'wb')
    while True:
        time.sleep(random.random())
        content = f_read.read(1024)
        if content:
            f_write.write(content)
        else:
            break
    f_read.close()
    f_write.close()
    queue.put(file_name)

def main():
    souce_folder_name = input('请输入要复制的文件夹名字：')
    dest_folder_name = souce_folder_name + '副本'
    try:
        os.makedirs(dest_folder_name)
    except Exception as e:
        pass
    file_names = os.listdir(souce_folder_name)#获取目录下的所有文件

    #创建队列
    queue = multiprocessing.Manager().Queue()
    #创建进程池
    pool = multiprocessing.Pool(3)


    for file_name in file_names:
        #向进程池中添加任务
        pool.apply_async(copy_file,args=(queue,file_name,souce_folder_name,dest_folder_name))

    pool.close()

    all_file_num = len(file_names)

    while True:
        file_name = queue.get()
        if file_name in file_names:
            file_names.remove(file_name)

        copy_rate = (all_file_num - len(file_names)) * 100 / all_file_num
        print("\r%.2f...(%s)" % (copy_rate, file_name) + " " * 50, end="")
        if copy_rate >= 100:
            break
    print()




