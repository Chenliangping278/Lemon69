# -coding: UTF-8 -*-
# @Time  : 2020/06/24 20:01
# @Author: Liangping_Chen
# @E-mail: chenliangping_2018@foxmail.com

import requests
def http_request(url,data,token=None,method='post'):
    header = {'X-Lemonban-Media-Type': 'lemonban.v2',
                'Authorization':token}
    #判断是get请求还是post请求
    if method=='get':
        # 发起注册&登录
        result = requests.get(url, json=data, headers=header)
    else:
        result = requests.post(url, json=data, headers=header)

    return result.json()#return返回指定的结果
if __name__ == '__main__':

    login_url='http://120.78.128.25:8766/futureloan/member/login'
    login_data={'mobile_phone':13665929730,'pwd':'12345678'}
    response=http_request(login_url,login_data)
    print('登录的结果是：{}'.format(response))

    #充值
    token=response['data']['token_info']['token']
    rec_url='http://120.78.128.25:8766/futureloan/member/recharge'
    rec_data = {'member_id': 200170, 'amount': 123456}
    print(http_request(rec_url,rec_data,"bearer "+token))