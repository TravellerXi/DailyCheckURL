#!/usr/bin/env python3
# coding:utf-8
import requests
import os

"""
URLs: 自动化晨检得网站地址
Proxy：代理地址
SendTo:手机号

"""

URls=['网址1','网址2']
proxy = {'http': 'http://10.188.X.x:端口', 'https': 'http://10.188.X.x:端口'}
SendTo='手机号'
Subject="晨检结果"

def CheckIfOk(URL:str,proxy):
    GetResponse = requests.get(URL,proxies=proxy)
    if GetResponse.status_code == 200:
        return 0
    else:
        return GetResponse.status_code


def SendMsg(SendTo:str,Subject:str,Message):
    """
    Subject不重要，Content重要
    :param SenderTo:
    :param Subject:
    :param Message:
    :return:
    """
    os.system('短信脚本所在路径 '+SendTo+" "+Subject+" "+Message)
    return 0

if __name__ =="__main__":

    Message='晨检结果:'
    for URL in URls:
        Result=CheckIfOk(URL,proxy)
        if Result ==0:
            Results="normal,200OK"
        else:
            Results ="error"+Result
        Subject='每日自动化晨检结果'
        Message=Message+URL+">>"+Results
    SendMsg(SendTo,Subject,Message)


