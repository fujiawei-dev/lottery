'''
Date: 2021.09.01 13:41
Description : Omit
LastEditors: Rustle Karl
LastEditTime: 2021.09.01 15:09:20
'''
import requests

history_api = 'http://www.cwl.gov.cn/cwl_admin/kjxx/findDrawNotice?' \
              'name=ssq&issueCount&issueStart=2013001&issueEnd=2021099&' \
              'dayStart&dayEnd&pageNo=%d'

session = requests.session()
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'DNT': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://www.cwl.gov.cn/kjxx/wqkj/',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ca;q=0.7',
    'Content-Type': 'application/x-www-form-urlencoded',
}

lotteries = []

for page in range(1, 15):
    json = session.get(history_api % page).json()
    for item in json['result']:
        lotteries.append(';'.join([item['code'], item['red'], item['blue']]))

with open('assests/records.txt', 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(lotteries))
