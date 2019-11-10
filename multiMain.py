import multiprocessing
from common.MailTemplate import *
import main
devices_list = ['baea68220004', '30120ca00704']  # 启动多个模拟器
devicesName_list = ['小米4X','4X测试机']

def devices_start_sync():
    print("=====并发启动设备=====")
    desired_process = []
    # 加载desired进程
    for i in range(len(devices_list)):
        port = 4723 + 2 * i  # 第一个端口号是4723，第二个是4725
        desired = multiprocessing.Process(target=main.run_test, args=(devices_list[i], devicesName_list[i], port))
        desired_process.append(desired)
    # 同时启动多设备执行测试
    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()


if __name__ == '__main__':

    devices_start_sync()

