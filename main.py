from config.VarConfig import *
from business.TestKeywordAndData import *
from common.MailTemplate import *


class runObject:
    udid = None
    deviceName = None
    port = None

def run_test(udid, deviceName, port):
    runObject.udid = udid
    runObject.deviceName = deviceName
    runObject.port = port
    get_excel_files(work_dir+"\\"+deviceName)

    reportTemplate = ReportTemplate()
    # 每读取到一个Excel文件执行一遍循环
    for dataFilePath in excel_files:
        TestKeywordAndData(dataFilePath)

    reportTemplate.reportTemplate_2(reportTemplate.statistics(excel_files), reportTemplate.getResult_2(excel_files), deviceName)


if __name__=='__main__':
    reportTemplate = ReportTemplate()
    # 每读取到一个Excel文件执行一遍循环
    for dataFilePath in excel_files:
        TestKeywordAndData(dataFilePath)

    reportTemplate.reportTemplate_2(reportTemplate.statistics(excel_files), reportTemplate.getResult_2(excel_files))
