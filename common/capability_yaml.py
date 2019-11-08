from appium import webdriver
import yaml
import logging
import logging.config
import os
from time import ctime
import multiprocessing

# devices_list=['30120ca00704','S002170030154']  #启动多个模拟器
def desired_caps():
    desired_caps_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\config\desired_caps.yaml')
    chrome_driver = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..\config\chromedriver76.exe')
    with open(desired_caps_path,'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.Loader)
     # 文件可能被占用状态，导致后面不能读取,with 可以避免此问题

    desired_caps = {}

    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['udid']=data['udid']
    desired_caps['deviceName']=data['deviceName']
    # desired_caps['appPackage']=data['appPackage']
    # desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']
    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']
    desired_caps['chromedriverExecutable'] = chrome_driver
    desired_caps['browserName'] = data['browserName']

    logging.info("start app...")
    driver =webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
    return driver
#构建desired进程组，由于有多个进行，所以进程定义成李列表
# desired_process=[]
# #加载desired进程
# for i in range(len(devices_list)):
#     port=4723+2*i #第一个端口号是4723，第二个是4725
# ##创建进程
#     desired=multiprocessing.Process(target=desired_caps,args=(devices_list[i],port))
#     desired_process.append(desired) #添加进程队列

if __name__ == "__main__":
     desired_caps()
     # 同时启动多设备执行测试
     # for desired in desired_process:
     #     desired.start()  # 每个进程去启动
     # for desired in desired_process:
     #     desired.join()  # 等所有子进程都执行完后再去关闭
