# -coding: UTF-8 -*-
# @Time  : 2020/06/24 20:01
# @Author: Liangping_Chen
# @E-mail: chenliangping_2018@foxmail.com
from python_auto.R_W_excel import read_data
from python_auto.R_W_excel import write_data
from python_auto.http_request import http_request
from openpyxl  import load_workbook
Token=None#全局变量，初始值为None

def run(file_name,sheet_name,c1,c2):
    global Token#申明全局变量，函数外的Token和函数内的Token是同一个值
    all_case=read_data(file_name,sheet_name)#在http_request进行请求的时候，判断是否是登录请求
    print('获取的测试数据是：',all_case)
    for test_data in all_case:

        #if test_data[0]==1
        #if test_data[1]=='登录'，判断两边是否相等，比较运算符
        ip='http://120.78.128.25:8766'
        #response=http_request(ip + test_data[4],eval(test_data[5]),token=Token,method=test_data[3])
        response = http_request(ip + test_data[4], eval(test_data[5]), token=Token, method=test_data[3])
        if 'login' in test_data[4]:

            Token="Bearer "+response['data']['token_info']['token']
        expected=eval(test_data[6])#期望值在第6列
        print('最后的结果值：',response)


        #开始写入结果
        write_data(file_name,sheet_name,test_data[0]+1,c1,str(response))

        #进行判断，期望值与实际值是否相等，判断用例是否执行通过
        actual={'code':response['code'],'msg':response['msg']}
        if eval(test_data[6])==actual:
            print('测试用例执行通过')
            write_data(file_name,sheet_name,test_data[0]+1,c2,'PASS')
        else:
            print('测试用例执行不通过')
            write_data(file_name,sheet_name,test_data[0]+1,c2,'FAIL')
        #保存
#run('test_case.xlsx','recharge',8,9)

run('test_case.xlsx','withdraw',8,9)