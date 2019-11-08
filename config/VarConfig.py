import os
from common.ParseExcel import ParseExcel
# 当前文件所在目录的父目录的绝对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 异常截图存放路径绝对值
screenPicturesDir = parentDirPath +"\\screenshots\\"

# 测试数据文件存放绝对路径
work_dir = parentDirPath + "\\data"


# 读取路径中的所有文件
all_files = []
for parent,dirnames,filenames in os.walk(work_dir):
    for filename in filenames:
        file = os.path.join(parent,filename)
        all_files.append(file)

# 提取路径中的所有Excel文件
global excel_files
excel_files = []
for excel in all_files:
    if excel.endswith('xlsx'):
        excel_files.append(excel)

# 创建解析Excel对象--zjq:多个文件共享变量，可以采用此种方法
excelObj = ParseExcel()


# 测试数据文件中，测试用例表中部分列对应的数字序号

testCase_testCaseName = 1
testCase_frameWorkName = 3
testCase_testStepSheetName = 4
testCase_dataSourceSheetName = 5
testCase_isExecute = 6
testCase_runTime = 7
testCase_testResult =8

# 用例步骤表中，部分列对应的数字序号
testStep_testStepDescribe =1
testStep_keyWords = 2
testStep_locationType=3
testStep_locatorExpression = 4
testStep_operateValue = 5
testStep_runTime = 6
testStep_testResult = 7
testStep_errorInfo = 8
testStep_errorPic = 9

# 数据源表中，是否执行列对应的数字编号
dataSource_username = 1
dataSource_isExecute = 4

dataSource_runtime = 5
dataSource_result = 6
#测试报告存放路径
test_report = parentDirPath + "\\report\\"