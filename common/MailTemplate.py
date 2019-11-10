from config.VarConfig import *
from common.ParseExcel import ParseExcel
import time


colorDict = {"pass":"green","failed":"red","none":"orange"}
class ReportTemplate(object):
    
    #测试报告模板
    def reportTemplate(self,statisticsStr,trData):
        htmlStr = '''<!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <title>测试报告</title>
        <style>
        body {
            width: 80%;
            margin: 40px auto;
            font-weight: bold;
            font-family: 'trebuchet MS','Lucida sans','SimSun';
            font-size: 18px;
            color: #000;
        }
        table{
            *border-collapse: collapse; /*合并表格边框*/
            border-spacing: 0;
            width: 100%;
        }
        .tableStyle{
            border-style: outset;
            border-width: 2px;
            border-color: blue;
        }
        .tableStyle tr:hover{
            background: rgb(173, 216, 230);/*鼠标滑过时，动态显示颜色*/
        }
        .tableStyle td,.tableStyle th{
            border-left: solid 1px rgb(146, 208, 80);
            border-top: 1px solid rgb(146,208,80);
            padding: 15px;
            text-align: center;
        }
        .tableStyle th{
            padding: 15px;
            background-color: rgb(146, 208, 80);
            background-image: -webkit-gradient(linear,left top,left bottom,from(#92d050),to(#a2d668))
        }
        #distance{
            height: 100px;
        }
        #logo{
            margin-right:10px;
            position: absolute;
            bottom: 30px;
            right: 0px;
            color: #3c3c3c;
            font-family: "KaiTi";
            font-weight: bold;
        }
        </style>
        </head>
        <body>
        <center><h1>H5自动化测试报告</h1></center>
        '''
        endStr = '''
                <div id="distance"></div> 
                        <div id="logo">联云科技·质控部
                            <br/>
                            %s
                        </div>        
                    </div>  
                </body>
                </html>''' % (time.strftime("%Y-%m-%d"))
        html = htmlStr + statisticsStr + trData + endStr
        with open(parentDirPath+"//report//testReport_H5_"+time.strftime("%Y%m%d_%H%M%S")+".html","w",encoding="utf-8") as fp:
            fp.write(html)
        return html
    
    #获取结果表格
    def getResult(self,excel_files):
        global colorDict
        trDatas = []
        trData = ''
        for excel in excel_files:
            excelObj.loadWorkBook(excel)
            caseSheet = excelObj.getSheetByName("测试用例")
            excel_name = excel.split('\\')[-1].split('.')[0]
            tbHead = '''
            <center><h3>%s测试报告</h3></center>
            <table class="tableStyle">
                <thead>
                <tr>
                    <th>用例名称</th>
                    <th>用例描述</th>
                    <th>是否执行</th>
                    <th>执行结束时间</th>
                    <th>结果</th>
                </tr>
                </thead>
                '''%(excel_name)
            trData += tbHead
            for rowNo in range(2,excelObj.getRowsNumber(caseSheet)+1):
                trDatas.append('''
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td style="color:%s">%s</td>
                </tr> 
                '''% (str(excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_testCaseName)),\
                        str(excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_testCaseName+1)),\
                        str(excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_isExecute)),\
                        str(excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_runTime)),\
                        colorDict[excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_testResult)],\
                        str(excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_testResult)))
                        )
            for data in trDatas:
                trData += data
            trDatas.clear()
            trData += "</table>"
        return trData

    #测试报告模板模板2
    def reportTemplate_2(self,statisticsStr,trData, deviceName):
        htmlStr = '''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="utf-8">
        <title>测试报告</title>
        <style>
        *{
            margin: 0px;
            padding: 0px;
        }
        body{  
             background-color:#CCCC99;
            /* rgba(0, 0, 0, 0.767); */
            background-size: 100%,100%;
            /* opacity: 0.9; */
        }
        #body_style {   
            width: 60%;
            height: 100%;
            margin: 0 auto;
            position:absolute;
            left:20%;
            border-left: solid; border-width: 5px;
            border-right: solid; border-width: 5px;
            border-color:#EECFA1;
            background-color: rgba(51, 51, 0, 0.2);
        }
        h1{
            text-align:center;
            color: #3c3c3c;
            font-family: 微软雅黑;
            letter-spacing: 12px;
            padding-top: 40px;
        }
        table{
            *border-collapse: collapse; /*合并表格边框*/
            border-spacing: 0;
            width: 100%;
            border-style: inset;
            border-width: 2px;
            border-color: #ffffff;
            background-color: #ffffff;
            opacity: 0.9;
        }
        /* 表头样式 */
        .spread{
            background-color: rgb(169,209,141);
            font-family: "Times New Roman"
            text-align:left;
        }
        .spread:hover{
            cursor: pointer;
            background-color: rgb(110,168,70);
        }
        .hide{
            display: none;
        }
        /* 标题样式 */
        .td_title{
            margin-left:10px;
            color: #333;
            font-size: 25px;
            display:inline;
        }
        /* 副标题样式 */
        .detail{
            color: #990033;
            font-family: arial;
            font-size: 15px;
            margin-top: 5px;
            display:inline;
        }
        table td,table th{
            border-left: solid 1px  #ccc;
            border-top: 1px solid  #ccc;
            padding: 15px;
            text-align: center;
            font-family: "Courier New";
        }
        /* 下拉标题样式 */
        .title{
            padding: 15px;
            background-color: rgb(169,209,141);
        }
        #distance{
            height: 100px;
        }
        #logo{
            margin-right:10px;
            position: absolute;
            bottom: 30px;
            right: 0px;
            color: #3c3c3c;
            font-family: "KaiTi";
            font-weight: bold;
        }
        </style>
        <script>
            window.onload=function(){
                //获取窗口大小
                var window_h=document.documentElement.clientHeight;
                function addWindowHeight() {
                    //获取当前窗口可视操作区域高度
                    var h =document.documentElement.scrollHeight;
                    //自适应窗口
                    document.getElementById("body_style").style.height=h+"px";
                }
                function minusWindowHeight(){
                    //获取当前内容的高度
                    var h=document.getElementById("distance").offsetTop+100;
                    //获取body_style盒子的高度
                    var body= document.getElementById("body_style");
                    //自适应窗口
                    window_h>h?body.style.height=window_h+"px":body.style.height=h+"px";
                }
                function spread_click(){
                    //判断当前状态为隐藏时操作
                    if(this.getAttribute("flag")=="true"){
                        var hidelist=this.parentNode.parentNode.childNodes;
                        // 从第一个隐藏节点开始，过滤text节点
                        for(var i=2;i<hidelist.length;i+=2){
                            hidelist[i].style.display="table-row";
                        }
                        this.setAttribute("flag","flase");
                        this.style.background="rgb(110,168,70)";
                        addWindowHeight();
                    }
                    else{
                        var hidelist=this.parentNode.parentNode.childNodes;
                        for(var i=2;i<hidelist.length;i+=2){
                            hidelist[i].style.display="none";
                        }
                        this.setAttribute("flag","true");
                        minusWindowHeight(); 
                    }    
                }
                var list=document.getElementsByClassName("spread");
                var hideContent=document.getElementsByClassName("hide");
                for(var i=0;i<list.length;i++){
                    list[i].onclick=spread_click;
                    list[i].setAttribute("flag","true");
                }
            };
        </script>
        </head>
        <body>
            <div id="body_style">
                <h1>H5自动化测试报告</h1>
                <br>
        '''
        endStr = '''
        <div id="distance"></div> 
                <div id="logo">联云科技·质控部
                    <br/>
                    %s
                </div>        
            </div>  
        </body>
        </html>'''%(time.strftime("%Y-%m-%d"))
        html = htmlStr + statisticsStr + trData + endStr
        t = time.strftime('%Y%m%d_%H%M%S',time.localtime())
        newTestReport = test_report+'//testReport_H5_'+t+"_"+deviceName+'.html'
        with open(newTestReport,"w",encoding="utf-8") as fp:
            fp.write(html)
        return html
    
    #获取结果表格模板2
    def getResult_2(self,excel_files):
        global colorDict
        global excelObj
        trDatas = []
        trData = ''
        for excel in excel_files:
            excelObj.loadWorkBook(excel)
            caseSheet = excelObj.getSheetByName("测试用例")
            tableTotal = 0
            tableExecuteNum = 0
            tablePassNum = 0
            passRate = ''
            tableTotal += excelObj.getRowsNumber(caseSheet)-1
            resultCols = excelObj.getColumn(caseSheet,testCase_testResult)
            executeCols = excelObj.getColumn(caseSheet,testCase_isExecute)
            for idx,result in enumerate(resultCols[1:]):
                if result.value == "pass":
                    tablePassNum += 1
            for idx,execute in enumerate(executeCols[1:]):
                if execute.value == "y":
                    tableExecuteNum += 1
            if tableExecuteNum != 0:
                # passRate = str(tablePassNum/tableExecuteNum*100)+'%'
                passRate = str(round(tablePassNum / tableExecuteNum * 100, 2)) + '%'
            else:
                passRate = '0%'
            excel_name = excel.split('\\')[-1].split('.')[0]
            tbHead = '''
            <table class="part">
                    <tr>
                        <td colspan="5" class="spread">
                            <div class="td_title ">
                                %s测试报告
                            </div>&emsp;&emsp;
                            <div class="detail">
                                (总用例数：%s&emsp;&emsp;执行用例总数：%s&emsp;&emsp;通过用例：%s&emsp;&emsp;通过率：%s)
                            </div>
                        </td>
                        <!-- <td class="spread result_col" colspan="1">展开</td> -->
                    </tr>                
                    <tr class="title hide">
                            <td>名称</td>
                            <td>用例描述</td>
                            <td>是否执行</td>
                            <td>执行结束时间</td>
                            <td>结果</td>
                    </tr>
                '''%(excel_name,tableTotal,tableExecuteNum,tablePassNum,passRate)
            trData += tbHead
            for rowNo in range(2,excelObj.getRowsNumber(caseSheet)+1):
                # res = excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_testResult)
                # if not res or (res == ""):
                #     res = 'none'
                trDatas.append('''
                <tr class="hide">
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td style="color:%s">%s</td>
                </tr> 
                '''% (str(excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_testCaseName)),\
                        str(excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_testCaseName+1)),\
                        str(excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_isExecute)),\
                        str(excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_runTime)),\
                        colorDict[excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_testResult)],\
                        str(excelObj.getCellOfValue(caseSheet,rowNo=rowNo,colsNo=testCase_testResult)))
                        )
            for data in trDatas:
                trData += data
            trDatas.clear()
            trData += "</table>"
        return trData
    
    #统计用例执行情况
    def statistics(self,excel_files):
        global colorDict
        global excelObj
        total = 0
        executeNum = 0
        passNum = 0
        for excel in excel_files:
            excelObj.loadWorkBook(excel)
            caseSheet = excelObj.getSheetByName("测试用例")
            total += excelObj.getRowsNumber(caseSheet)-1
            resultCols = excelObj.getColumn(caseSheet,testCase_testResult)
            executeCols = excelObj.getColumn(caseSheet,testCase_isExecute)
            for idx,result in enumerate(resultCols[1:]):
                if result.value == "pass":
                    passNum += 1
            for idx,execute in enumerate(executeCols[1:]):
                if execute.value == "y":
                    executeNum += 1
        statisticsStr = '''
        <p style="text-align:center;color: #990033;">用例总数：%s&emsp;&emsp;执行用例数：%s&emsp;&emsp;成功用例数：%s&emsp;&emsp;通过率：%s</p>
        <br>
        '''%(total,executeNum,passNum,str(round(passNum/executeNum*100,2))+'%')
        return statisticsStr